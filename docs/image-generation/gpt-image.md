# GPT Image

使用 OpenAI 图像格式生成与编辑图片

`POST` `https://api.tokenbyte.ai/v1/images/generations`

使用模型列表中可用的 GPT Image 模型生成图片。图片编辑使用 `/v1/images/edits`，采用 `multipart/form-data` 上传参考图。


## 生成参数
| 状态 | 说明 | 说明 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | 是 | GPT Image 模型 ID |
| `prompt` | string | 是 | 图片内容、风格与构图说明 |
| `size` | string | 否 | 输出尺寸，枚举取决于模型 |
| `quality` | string | 否 | 质量档位 |
| `background` | string | 否 | `auto`、`transparent` 或 `opaque` |
| `output_format` | string | 否 | `png`、`jpeg` 或 `webp` |
| `n` | integer | 否 | 图片数量，取决于模型与渠道限制 |


## 编辑图片
调用 `/v1/images/edits` 时传入 `image`、`prompt` 与 `model`。多参考图是否可用、最多张数和文件大小以模型能力为准。

## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl https://api.tokenbyte.ai/v1/images/generations \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model":"<gpt-image-model-id>",
    "prompt":"雨夜霓虹街道，电影感广角镜头",
    "size":"1024x1024"
  }'
```
```bash
{
  "created": 1770000000,
  "data": [{ "url": "https://.../image.png" }],
  "usage": { "total_tokens": 0 }
}
```
</details>

<details open>
<summary><b>Python</b></summary>

```bash
result = client.images.generate(
    model="<gpt-image-model-id>",
    prompt="雨夜霓虹街道，电影感广角镜头",
    size="1024x1024",
)
print(result.data[0].b64_json or result.data[0].url)
```
```bash
{
  "created": 1770000000,
  "data": [{ "url": "https://.../image.png" }],
  "usage": { "total_tokens": 0 }
}
```
</details>

<details open>
<summary><b>JavaScript</b></summary>

```bash
const result = await client.images.generate({
  model: "<gpt-image-model-id>",
  prompt: "雨夜霓虹街道，电影感广角镜头",
  size: "1024x1024",
});
```
```bash
{
  "created": 1770000000,
  "data": [{ "url": "https://.../image.png" }],
  "usage": { "total_tokens": 0 }
}
```
</details>
