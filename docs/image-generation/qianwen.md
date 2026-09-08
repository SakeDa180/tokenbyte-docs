# 图像生成同步调用

使用 TokenByte 调用 千问 图像生成同步调用接口

`POST` `https://api.tokenbyte.ai/api/v1/image/generation`

使用 TokenByte 统一图像任务接口调用 Qwen 的图像生成同步调用能力。模型名称请从模型市场复制，不要根据厂商官网名称自行推测。


## Header 参数
| 状态 | 说明 | 说明 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | 是 | GPT Image 模型 ID |
| `prompt` | string | 是 | 图片内容、风格与构图说明 |
| `size` | string | 否 | 输出尺寸，枚举取决于模型 |
| `quality` | string | 否 | 质量档位 |
| `background` | string | 否 | `auto`、`transparent` 或 `opaque` |
| `output_format` | string | 否 | `png`、`jpeg` 或 `webp` |
| `n` | integer | 否 | 图片数量，取决于模型与渠道限制 |


## Header 参数
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
</details>

若响应直接包含 `urls`，可立即读取结果；若返回 `task_id`，请调用查询图像任务直到进入成功或失败终态。


