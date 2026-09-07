

# 文本生成（Claude）

使用 Anthropic Messages 兼容格式生成文本

`GET` `https://api.tokenbyte.ai/v1/messages`

返回当前 API Key 所属分组、模型白名单和账号权限 共同允许的模型。后续请求中的 `model` 必须使用响应中的完整 `id`，模型列表请查看TokenByte支持的所有[AI 模型](https://tokenbyte.ai/)。



## Body 参数
| 参数 | 必填 | 说明 |
| :--- | :--- | :--- |
| `Authorization` | 是 | Bearer <TOKENBYTE_API_KEY> |
| `anthropic-version` | 是 | 例如`2023-06-01` |
| `Content-Type` | 是 | application/json |

## Body 参数
| 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | 是 | 支持 Messages 协议的完整模型 ID |
| `messages` | array | 是 | `user` 与 `assistant` 对话消息 |
| `max_tokens` | integer | 是 | 最大输出 Token 数 |
| `system` | string/array | 否 | 系统指令，不放入 `messages` |
| `stream` | boolean | 否 | 是否返回 SSE 事件 |
| `temperature` | number | 否 | 采样随机度 |
| `top_p` | number | 否 | 核采样概率阈值 |
| `top_k` | integer | 否 | 候选 Token 数量 |
| `stop_sequences` | array | 否 | 自定义停止序列 |
| `tools` | array | 否 | Anthropic 工具定义 |
| `tool_choice` | object | 否 | 自动、任意、指定工具或禁用工具 |
| `thinking` | object | 否 | 模型支持时启用扩展思考及设置 Token 预算 |
| `metadata` | object | 否 | 请求元数据 |

`messages[].content` 可以是字符串或内容块数组。常见内容块包括 `text`、`image`、`tool_use` 和 `tool_result`。

## 响应

非流式响应的 `content` 是内容块数组，文本通常位于 `content[].text`。`stop_reason` 表示停止原因，`usage` 包含输入、输出及缓存 Token 用量。

流式请求设置 `stream: true`，按顺序处理 `message_start`、`content_block_delta`、`message_delta` 和 `message_stop` 等 SSE 事件。


## Body 参数
设置 `stream: true` 后，接口通过 SSE 返回 `chat.completion.chunk`。逐块读取 `choices[0].delta`，收到 `data: [DONE]` 后结束。需要在最后一个数据块获取用量时，可设置 `stream_options.include_usage: true`。


## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl https://api.tokenbyte.ai/v1/messages \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"model":"<model-id>","max_tokens":1024,"messages":[{"role":"user","content":"你好"}]}'
```
</details>

<details open>
<summary><b>Python</b></summary>

```bash
from anthropic import Anthropic

client = Anthropic(base_url="https://api.tokenbyte.ai", api_key="YOUR_KEY")
message = client.messages.create(
    model="<model-id>", max_tokens=1024,
    messages=[{"role": "user", "content": "你好"}],
)
print(message.content[0].text)
```
</details>

<details open>
<summary><b>JavaScript</b></summary>

```bash
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://api.tokenbyte.ai",
  apiKey: "YOUR_KEY",
});
const message = await client.messages.create({
  model: "<model-id>",
  max_tokens: 1024,
  messages: [{ role: "user", content: "你好" }],
});
```
</details>


<details open>
<summary><b>200</b></summary>

```bash
{
  "id": "msg_xxx",
  "type": "message",
  "role": "assistant",
  "model": "<model-id>",
  "content": [{ "type": "text", "text": "你好！" }],
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": { "input_tokens": 8, "output_tokens": 4 }
}
```
</details>

