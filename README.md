# TokenByte

<p align="center">
  <a href="https://tokenbyte.ai/">官网</a> •
  <a href="https://tokenbyte.ai/models/"> AI 模型列表 </a>•
  <a href="mailto:support@tokenbyte.ai">联系支持</a>
</p>

TokenByte 是一个高效、稳定的 AI 模型聚合与分发平台。本文档旨在帮助开发者快速了解并接入 TokenByte 服务。

---

## 📖 快速开始

### 1. 环境准备

使用 TokenByte API 前，请确认你的开发环境符合以下要求：

* **操作系统**：Windows / macOS / Linux
* **推荐浏览器**：Google Chrome / Microsoft Edge / Mozilla Firefox
* **支持语言/工具**：Python、Node.js、Go、cURL 等任意支持 HTTP 请求的语言环境

---

## ⚙️ 使用说明

### 步骤 1：创建账号
前往 [TokenByte 官网](https://tokenbyte.ai/) 注册账号。支持以下登录方式：
* 邮箱注册 / 登录
* GitHub / Discord 快捷登录
* 通行密钥（Passkey）无密码安全登录

### 步骤 2：创建 API Key
1. 登录后进入 **控制台** -> **API 密钥管理**。
2. 点击 **新建 API 密钥**。
3. *建议：为每个独立的应用或开发环境单独创建 Key，并配置相应的速率限制以保障安全。*

### 步骤 3：发起 API 请求
TokenByte 兼容 OpenAI 格式标准。基础 Endpoint 如下：

* **Base URL**: `https://api.tokenbyte.ai/v1`

> 💡 **提示**：调用时请将请求体中的 `model` 参数替换为 [模型广场](https://tokenbyte.ai/models/) 或 **控制台 -> 模型市场** 中查询到的具体模型 ID。

#### 代码示例 (cURL)

```bash
curl https://api.tokenbyte.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": "Hello, TokenByte!"
      }
    ]
  }'
```

## ❓ 常见问题 (FAQ)
### Q1: API Key 提示 401 Unauthorized 或 Invalid API Key 怎么处理？

请检查请求头 Authorization 中是否包含 Bearer  前缀（注意 Bearer 与 Key 之间须有空格）。

检查 API Key 是否已在控制台中被禁用或删除。

确保在控制台中创建 Key 时分配了对应的模型访问权限。

### Q2: 如何查看各 AI 模型的具体 ID 和价格？
请访问 [AI 模型列表](https://tokenbyte.ai/models/) 或登录控制台查看 模型市场。

模型 ID 需填入请求参数中的 "model" 字段（例如 gpt-4o、claude-3-5-sonnet）。

### Q3: TokenByte 是否完全兼容 OpenAI SDK？
完全兼容。在使用 Python/Node.js 的 OpenAI 官方 SDK 时，只需将 base_url 改为 `https://api.tokenbyte.ai/v1`，并将 api_key 替换为 TokenByte 生成的 Key 即可直接运行。

### Q4: 请求遇到 429 Too Many Requests 或频率限制怎么办？
出现该错误通常是因为触发了该 API Key 配置的 Rate Limit（每分钟请求数/Token 限制）或账户余额不足。

请在控制台检查该 Key 的速率配置，或尝试在代码中加入重试与指数退避（Exponential Backoff）逻辑。

### Q5: 支持流式输出（Streaming）吗？
支持。只需在请求 JSON 体中添加 "stream": true 参数即可开启 SSE（Server-Sent Events）流式响应。

### Q6: 请求超时（Timeout）或网络连通性差怎么办？
TokenByte 节点覆盖全球多种网络环境。若遭遇连接超时，请先检查本地代理设置，或尝试在 SDK 中调整超时参数（例如将 timeout 设为 30s 以上）。
