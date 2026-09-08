# 图片生成

使用 TokenByte 调用 即梦 图片生成接口

`POST` `https://api.tokenbyte.ai/api/v1/image/generation`

使用 TokenByte 统一图像任务接口调用 Jimeng 的图片生成能力。模型名称请从模型市场复制，不要根据厂商官网名称自行推测。


## Header 参数
| 状态 | 说明 | 说明 |
| :--- | :--- | :--- |
| `Authorization` | 是 | `Bearer <TOKENBYTE_API_KEY>` |
| `Content-Type` | 是 | `application/json` |


## Body 参数
| 状态 | 说明 | 说明 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | 是 | Jimeng 模型的完整 ID |
| `_action` | string | 视模型 | 当前模式使用 `generate` |
| `prompt` | string | 视模型 | 生成或编辑提示词 |
| `image` | string/object/array | 否 | 参考图 URL、Base64 或厂商结构化图片对象 |
| `size` | string | 否 | 输出尺寸或分辨率 |
| `seed` | integer | 否 | 模型支持时控制随机种子 |


## 模式说明
即梦模型通过动作类型区分生成模式，参考素材必须使用可公开访问的 URL。

仅传入模型明确支持的字段；不支持的参数可能被忽略或返回参数错误。


## 示例代码
<details open>
<summary><b>请求</b></summary>

```bash
curl https://api.tokenbyte.ai/api/v1/image/generation \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "_action": "generate",
  "model": "<model-id>",
  "prompt": "描述画面主体、构图、光线和风格",
  "size": "1024x1024"
}'
```

</details>

<details open>
<summary><b>响应</b></summary>

```bash
{
  "code": 0,
  "data": {
    "task_id": "image_xxx",
    "task_status": "pending",
    "urls": []
  },
  "message": "success",
  "request_id": "req_xxx"
}
```
</details>

若响应直接包含 `urls`，可立即读取结果；若返回 `task_id`，请调用 [查询图像任务](/docs/common/image-task.md) 直到进入成功或失败终态。
