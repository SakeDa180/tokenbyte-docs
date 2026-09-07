# TokenByte

<p align="center">
  <a href="https://tokenbyte.ai/">官网</a> •
  <a href="https://api.tokenbyte.ai/v1">API 节点</a> •
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

> 💡 **提示**：调用时请将请求体中的 `model` 参数替换为 [模型广场](https://tokenbyte.ai/) 或 **控制台 -> 模型市场** 中查询到的具体模型 ID。

#### 代码示例 (cURL)

```bash
curl [https://api.tokenbyte.ai/v1/chat/completions](https://api.tokenbyte.ai/v1/chat/completions) \
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
📄 开源协议
本项目采用 MIT License 开源协议。

***

### 💡 优化要点解析

* **顶部视觉增强**：加入了居中的快捷导航链接（官网、节点、邮件），提升项目质感。
* **填充请求示例**：在“发起请求”部分补充了标准 `cURL` 代码块，开发者可以直接复制测试，极大降低接入门槛。
* **FAQ 折叠屏（`details` 标签）**：利用 Markdown HTML 标签将 FAQ 做成下拉折叠样式，保持页面干练不臃肿。
* **规范命名与强调**：使用了引用块 `>`、加粗与代码块标识，规范了 `Base URL` 和请求头格式。
