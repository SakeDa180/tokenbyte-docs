import requests
import json
import logging
import time
from typing import Optional, Dict, Any

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TokenByteClient:
    """TokenByte API 客户端，包含生产级错误处理与重试机制"""
    
    def __init__(self, api_key: str, base_url: str = "https://api.tokenbyte.ai/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.max_retries = 3
        self.retry_delay = 1  # 初始重试延迟（秒）
        
    def chat_completion(self, 
                       model: str, 
                       messages: list, 
                       temperature: float = 0.7, 
                       max_tokens: int = 1000) -> Optional[Dict[str, Any]]:
        """
        发送聊天补全请求，包含完整的错误处理和重试逻辑
        
        Args:
            model: 模型名称，如 "gpt-4", "claude-3-opus", "qwen-max"
            messages: 消息列表，格式同 OpenAI
            temperature: 温度参数
            max_tokens: 最大生成 token 数
            
        Returns:
            API 响应字典，失败时返回 None
        """
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        for attempt in range(self.max_retries):
            try:
                logger.info(f"尝试第 {attempt + 1} 次请求，模型: {model}")
                
                # 发送请求，设置超时时间
                response = requests.post(url, headers=headers, json=data, timeout=30)
                response.raise_for_status()  # 检查 HTTP 状态码
                
                result = response.json()
                
                # 检查 API 级别的错误
                if "error" in result:
                    error_msg = result.get("error", {}).get("message", "未知错误")
                    error_code = result.get("error", {}).get("code", "unknown")
                    logger.error(f"API 返回错误: {error_msg} (代码: {error_code})")
                    self._handle_api_error(error_code, error_msg)
                    return None
                
                # 记录成功响应
                logger.info(f"请求成功，模型: {model}, 响应时间: {response.elapsed.total_seconds():.2f}秒")
                return result
                
            except requests.exceptions.Timeout:
                logger.warning(f"请求超时 (尝试 {attempt + 1}/{self.max_retries})")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))  # 指数退避
                else:
                    logger.error("达到最大重试次数，请求失败")
                    return None
                    
            except requests.exceptions.ConnectionError as e:
                logger.error(f"网络连接错误: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))
                else:
                    logger.error("网络连接持续失败")
                    return None
                    
            except requests.exceptions.HTTPError as e:
                status_code = e.response.status_code if e.response else "unknown"
                logger.error(f"HTTP 错误 (状态码 {status_code}): {e}")
                
                # 根据状态码处理
                if status_code == 401:
                    logger.error("API 密钥无效或过期，请检查配置")
                    return None
                elif status_code == 429:
                    logger.warning("请求频率超限，尝试退避重试")
                    if attempt < self.max_retries - 1:
                        time.sleep(5)  # 频率限制时延长等待
                    else:
                        logger.error("持续遇到频率限制")
                        return None
                elif status_code >= 500:
                    logger.warning(f"服务器错误 ({status_code})，尝试重试")
                    if attempt < self.max_retries - 1:
                        time.sleep(self.retry_delay * (attempt + 1))
                    else:
                        logger.error("服务器持续错误")
                        return None
                else:
                    logger.error(f"不可重试的 HTTP 错误: {status_code}")
                    return None
                    
            except json.JSONDecodeError as e:
                logger.error(f"响应 JSON 解析失败: {e}")
                return None
                
            except Exception as e:
                logger.error(f"未知错误: {e}", exc_info=True)
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))
                else:
                    return None
        
        return None
    
    def _handle_api_error(self, error_code: str, error_message: str):
        """处理特定的 API 错误码"""
        error_handlers = {
            "invalid_api_key": "API 密钥无效，请检查并更新",
            "insufficient_quota": "额度不足，请充值或检查使用量",
            "model_not_found": "请求的模型不存在或未授权",
            "rate_limit_exceeded": "请求频率超限，请稍后重试",
            "context_length_exceeded": "上下文长度超限，请减少输入",
        }
        
        handler = error_handlers.get(error_code)
        if handler:
            logger.error(f"API 错误处理建议: {handler}")
        else:
            logger.error(f"未知 API 错误码: {error_code}, 消息: {error_message}")

# 使用示例
if __name__ == "__main__":
    # 替换为你的 TokenByte API Key
    API_KEY = "YOUR_TOKENBYTE_API_KEY"
    
    client = TokenByteClient(api_key=API_KEY)
    
    # 准备请求消息
    messages = [
        {"role": "user", "content": "请用中文介绍一下 TokenByte 平台"}
    ]
    
    # 调用 API
    result = client.chat_completion(
        model="gpt-4",  # 可替换为 claude-3-opus、qwen-max 等
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )
    
    # 处理结果
    if result:
        content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
        print("API 调用成功！")
        print(f"响应内容: {content[:200]}...")  # 只打印前200字符
        print(f"总 Token 消耗: {result.get('usage', {}).get('total_tokens', 'N/A')}")
    else:
        print("API 调用失败，请检查日志和网络连接")
