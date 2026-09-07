
# 文本生成（Gemini）

使用 Gemini 原生 generateContent 格式生成文本

`POST` `[https://api.tokenbyte.ai/v1beta/models/{model}:generateContent`

流式输出将操作名改为 `streamGenerateContent`。模型 ID 是路径的一部分，请从[模型列表](https://tokenbyte.ai/models/)复制。



## Header 参数
| 参数 | 必填 | 说明 |
| :--- | :--- | :--- |
| `x-goog-api-key` | 是 | TokenByte API Key |
| `Content-Type` | 是 | application/json |

## 路径参数
| 参数 | 说明 |
| :--- | :--- |
| `model` | 支持 Gemini 协议的完整模型 ID |
| `action` | 	generateContent 或 streamGenerateContent |

## Body 参数
| 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `contents` | array | 是 | 多轮消息，每项包含 `role` 与 `parts` |
| `systemInstruction` | object | 否 | 系统指令内容 |
| `generationConfig` | object | 否 | 温度、Top-P、Top-K、最大输出与停止序列 | 
| `tools` | array | 否 | 函数声明等工具 |
| `toolConfig` | object | 否 | 工具调用策略 |
| `safetySettings` | array | 否 | 模型支持时使用的安全阈值 |

`contents[].role` 通常为 `user` 或 `model`。`parts` 可包含 `text`、`inlineData`、`fileData`、`functionCall` 或 `functionResponse`。内联媒体的 `data` 使用 `Base64` 编码，并同时提供 `mimeType`。

## 响应
结果位于 `candidates[].content.parts`。文本 Part 使用 `text`，工具调用 Part 使用 `functionCall`。`finishReason` 表示停止原因，`usageMetadata` 包含提示词、候选输出和总 Token 数。


## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl "https://api.tokenbyte.ai/v1beta/models/<model-id>:generateContent" \
  -H "x-goog-api-key: $TOKENBYTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"role":"user","parts":[{"text":"Hello"}]}]}'
```
</details>

<details open>
<summary><b>Python</b></summary>

```bash
from google import genai

client = genai.Client(
    api_key="YOUR_KEY",
    http_options={"base_url": "https://api.tokenbyte.ai"},
)
response = client.models.generate_content(model="<model-id>", contents="Hello")
print(response.text)
```
</details>

<details open>
<summary><b>JavaScript</b></summary>

```bash
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  apiKey: "YOUR_KEY",
  httpOptions: { baseUrl: "https://api.tokenbyte.ai" },
});
const response = await ai.models.generateContent({
  model: "<model-id>",
  contents: "Hello",
});
console.log(response.text);
```
</details>


<details open>
<summary><b>200</b></summary>

```bash
{
  "candidates": [
    {
      "content": { "role": "model", "parts": [{ "text": "你好！" }] },
      "finishReason": "STOP",
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 8,
    "candidatesTokenCount": 4,
    "totalTokenCount": 12
  }
}
```
</details>
