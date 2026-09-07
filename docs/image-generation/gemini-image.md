# Gemini Image

使用 Gemini 原生内容格式生成与编辑图片

`POST` `https://api.tokenbyte.ai/v1beta/models/{model}:generateContent`

Gemini Image 使用 `contents[].parts` 同时承载文本和图片。鉴权 Header 为 `x-goog-api-key`，模型 ID 从 Gemini 模型列表获取。


## 生成参数
| 状态 | 类型 | 说明 |
| :--- | :--- | :--- |
| `contents` | array | 输入内容 |
| `parts[].text` | string | 生图提示词 |
| `generationConfig.responseModalities` | array | 请求图片输出时包含 `IMAGE` |
| `generationConfig.imageConfig.aspectRatio` | string | 画幅，如 `1:1`、`16:9` |
| `generationConfig.imageConfig.imageSize` | string | 模型支持时选择 `1K`、`2K`、`4K` |


## 图片编辑与参考图
在 `parts` 中加入 `inlineData`，其中 `mimeType` 为图片 MIME，`data` 为纯 Base64 数据。多参考图上限、分辨率和支持格式取决于模型。

返回结果位于 `candidates[].content.parts[]`；图片块包含 `inlineData`，文本块包含 `text`。

## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl "https://api.tokenbyte.ai/v1beta/models/<gemini-image-model-id>:generateContent" \
  -H "x-goog-api-key: $TOKENBYTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents":[{"parts":[{"text":"生成一张极简科技产品海报"}]}],
    "generationConfig":{
      "responseModalities":["TEXT","IMAGE"],
      "imageConfig":{"aspectRatio":"16:9","imageSize":"2K"}
    }
  }'
```
```bash
{
  "candidates": [
    {
      "content": {
        "parts": [
          { "text": "已生成图片" },
          { "inlineData": { "mimeType": "image/png", "data": "iVBOR..." } }
        ]
      }
    }
  ]
}
```
</details>
