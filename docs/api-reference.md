
# API 参考
TokenByte 使用一个 API Key 提供多协议 AI 能力。模型名称请从获取[模型列表](https://tokenbyte.ai/models/)读取，不要根据厂商官网名称自行推测。

## 接入地址

| 协议 | Base URL | 用途 |
| :--- | :---: | ---: |
| OpenAI 兼容 | [https://api.tokenbyte.ai/v1](https://api.tokenbyte.ai/v1) | 文本、GPT Image、Codex |
| Anthropic Messages | [https://api.tokenbyte.ai](https://api.tokenbyte.ai) | Claude Code |
| Gemini 原生 | [https://api.tokenbyte.ai](https://api.tokenbyte.ai) | Gemini 文本与图像 |
| TokenByte 任务接口 | [https://api.tokenbyte.ai/api/v1](https://api.tokenbyte.ai/api/v1) | ArtsDance 与异步任务 |

## 鉴权方式

| 协议 | Header |
| :--- | :--- |
| OpenAI / TokenByte | Authorization: Bearer <API_KEY> |
| Claude Code Gateway | Authorization: Bearer <API_KEY> |
| Gemini 原生 | x-goog-api-key: <API_KEY> |
