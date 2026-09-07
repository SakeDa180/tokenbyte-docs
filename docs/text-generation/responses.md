# 文本生成（Responses）

使用 OpenAI Responses 格式生成文本与调用工具

`POST` `https://api.tokenbyte.ai/v1/responses`

模型列表请查看TokenByte支持的所有[AI 模型](https://tokenbyte.ai/)页


## Header 参数
| 参数 | 必填 | 说明 |
| :--- | :--- | :--- |
| `Authorization` | 是 | Bearer <TOKENBYTE_API_KEY> |
| `Content-Type` | 是 | application/json |

## Body 参数
| 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | 是 | 支持 Responses 协议的完整模型 ID |
| `input` | string/array | 是 | 纯文本或结构化消息与工具结果 |
| `instructions` | string | 否 | 本次请求的系统级指令 |
| `previous_response_id` | string | 否 | 关联上一响应以继续对话 |
| `stream` | boolean | 否 | 是否返回语义化 SSE 事件 |
| `store` | boolean | 否 | 是否保存响应以供后续引用 |
| `tools` | array | 否 | 可用工具，取决于模型与渠道 |
| `tool_choice` | string/object | 否 | 控制模型是否及如何调用工具 |
| `temperature` | number | 否 | 采样随机度 |
| `top_p` | number | 否 | 核采样概率阈值 |
| `reasoning` | object | 否 | 模型支持时设置推理强度 |

`input` 使用数组时可承载 `message`、`function_call_output` 等结构化项目。工具调用通常在 `output` 中以 `function_call` 项返回，应用执行后将结果作为下一次请求的输入。

## 响应

非流式响应的 `output` 是有序输出项数组。最终文本通常位于 `output[].content[]` 中的 `output_text` 项；请不要假设 `output[0]` 一定是文本。

流式请求设置 `stream: true`。常见事件包括 `response.created`、`response.output_text.delta`、`response.completed` 和 `error`。


## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl https://api.tokenbyte.ai/v1/responses \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"<model-id>","input":"Hello"}'
```
</details>

<details open>
<summary><b>Python</b></summary>

```bash
from openai import OpenAI

client = OpenAI(base_url="https://api.tokenbyte.ai/v1", api_key="YOUR_KEY")
response = client.responses.create(model="<model-id>", input="Hello")
print(response.output_text)
```
</details>

<details open>
<summary><b>JavaScript</b></summary>

```bash
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.tokenbyte.ai/v1",
  apiKey: "YOUR_KEY",
});
const response = await client.responses.create({
  model: "<model-id>",
  input: "Hello",
});
console.log(response.output_text);
```
</details>


<details open>
<summary><b>200</b></summary>

```bash
{
  "id": "resp_xxx",
  "object": "response",
  "status": "completed",
  "model": "<model-id>",
  "output": [
    {
      "id": "msg_xxx",
      "type": "message",
      "role": "assistant",
      "status": "completed",
      "content": [
        { "type": "output_text", "text": "你好！", "annotations": [] }
      ]
    }
  ],
  "usage": { "input_tokens": 8, "output_tokens": 4, "total_tokens": 12 }
}
```
</details>

