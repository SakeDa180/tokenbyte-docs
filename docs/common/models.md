# 获取模型列表

获取当前账号可调用的模型

`GET` `https://api.tokenbyte.ai/v1/models`

返回当前 API Key 所属分组、模型白名单和账号权限共同允许的模型。后续请求中的 `model` 必须使用响应中的完整 `id`。

## 请求头

| 名称 | 必填 | 说明 |
| :--- | :--- | :--- |
| `Authorization` | 是 | `Bearer <TOKENBYTE_API_KEY>` |


## 响应字段
| 字段 | 类型 | 说明 |
| :--- | :--- | :--- |
| `object` | string | 固定为`list` |
| `data` | array | 模型集合 |
| `data[].id` | string | 调用接口时使用的模型 ID |
| `data[].owned_by` | string | 模型提供方或路由分组 |


## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl [https://api.tokenbyte.ai/v1/models](https://api.tokenbyte.ai/v1/models) \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY"
```
</details>

<details open>
<summary><b>Python</b></summary>

```bash
import requests

headers = {
    "Authorization": "Bearer $TOKENBYTE_API_KEY"
}

response = requests.get("[https://api.tokenbyte.ai/v1/models](https://api.tokenbyte.ai/v1/models)", headers=headers)
print(response.json())
```
</details>

<details open>
<summary><b>JavaScript</b></summary>

```bash
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.tokenbyte.ai/v1",
  apiKey: process.env.TOKENBYTE_API_KEY,
});
console.log((await client.models.list()).data);
```
</details>


<details open>
<summary><b>200</b></summary>

```bash
{
  "object": "list",
  "data": [{ "id": "<model-id>", "object": "model", "owned_by": "tokenbyte" }]
}
```
</details>



