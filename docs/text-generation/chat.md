
# 文本生成（Chat）

获取当前账号可调用的模型

`GET` `https://api.tokenbyte.ai/v1/models`

返回当前 API Key 所属分组、模型白名单和账号权限 共同允许的模型。后续请求中的 `model` 必须使用响应中的完整 `id`。模型列表请查看TokenByte支持的所有[AI 模型](https://tokenbyte.ai/)。



## Body 参数
| 参数 | 必填 | 说明 |
| :--- | :--- | :--- |
| `Authorization` | 是 | Bearer <TOKENBYTE_API_KEY> |
| `Content-Type` | 是 | application/json |

## Body 参数
| 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | 是 | 模型完整 ID |
| `messages` | array | 是 | 按时间顺序排列的消息 |
| `stream` | boolean | 否 | 是否使用 SSE 增量响应 |
| `temperature` | number | 否 | 采样随机度，支持范围取决于模型 |
| `max_tokens` | integer | 否 | 最大输出 Token 数 |
| `max_completion_tokens` | integer | 否 | 新版模型的最大输出 Token 数 |
| `top_p` | integer | 否 | 核采样概率阈值 |
| `stop` | string/array | 否 | 停止生成的字符串 |
| `response_format` | object | 否 | 文本、JSON 对象或 JSON Schema |
| `tools` | array | 否 | OpenAI 函数工具声明 |
| `tool_choice` | string/object | 否 | 工具选择方式 |

### messages

每条消息至少包含 role 和 content。支持的多模态内容与特殊字段以模型专题页为准。
role 可为 system、user、assistant 或 tool。工具结果使用 tool_call_id 与助手消息中的调用关联。


## Body 参数
设置 `stream: true` 后，接口通过 SSE 返回 `chat.completion.chunk`。逐块读取 `choices[0].delta`，收到 `data: [DONE]` 后结束。需要在最后一个数据块获取用量时，可设置 `stream_options.include_usage: true`。


## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl https://api.tokenbyte.ai/v1/chat/completions \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<model-id>",
    "messages": [{"role":"user","content":"Hello"}]
  }'
```
</details>

<details open>
<summary><b>Python</b></summary>

```bash
from openai import OpenAI

client = OpenAI(base_url="https://api.tokenbyte.ai/v1", api_key="YOUR_KEY")
result = client.chat.completions.create(
    model="<model-id>",
    messages=[{"role": "user", "content": "Hello"}],
)
print(result.choices[0].message.content)
```
</details>

<details open>
<summary><b>JavaScript</b></summary>

```bash
const result = await client.chat.completions.create({
  model: "<model-id>",
  messages: [{ role: "user", content: "Hello" }],
});
```
</details>


<details open>
<summary><b>200</b></summary>

```bash
{
  "id": "chatcmpl_xxx",
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "message": { "role": "assistant", "content": "Hello" },
      "finish_reason": "stop"
    }
  ],
  "usage": { "prompt_tokens": 8, "completion_tokens": 4, "total_tokens": 12 }
}
```
</details>

