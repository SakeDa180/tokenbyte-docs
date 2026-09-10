# ArtsDance 文生视频

使用 TokenByte 调用 AiSphere 文生视频接口

`POST` `https://api.tokenbyte.ai/api/v1/video/generation`

使用 TokenByte 统一视频任务接口调用 AiSphere 的文生视频能力。模型名称请查看TokenByte支持的所有[AI 模型](https://tokenbyte.ai/models/)，不要根据厂商官网名称自行推测。

## Header 参数
| 参数 | 必填 | 说明 |
| :--- | :--- | :--- |
| `Authorization` | 是 | Bearer <TOKENBYTE_API_KEY> |
| `Content-Type` | 是 | application/json |

## Body 参数
| 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | 是 | AiSphere 模型的完整 ID |
| `_action` | string | 视模型 | 当前模式使用 `t2v` |
| `prompt` | string | 视模型 | 生成或编辑提示词 |
| `image` | string/object/array | 否 | 参考图 URL、Base64 或厂商结构化图片对象 |
| `headtailImages` | object | 首尾帧模式 | 首帧与尾帧图片 |
| `characterImages` | array | 参考模式 | 主体或风格参考图片 |
| `duration` | integer | 否 | 视频时长，枚举取决于模型 |
| `resolution` | string | 否 | 输出尺寸或分辨率 |
| `seed` | integer | 否 | 模型支持时控制随机种子 |

## Body 参数
AiSphere 支持文生、单图、首尾帧及部分版本的主体参考模式。
仅传入模型明确支持的字段；不支持的参数可能被忽略或返回参数错误。

## 请求示例
<details open>
<summary><b>cURL</b></summary>

```bash
curl https://api.tokenbyte.ai/api/v1/video/generation \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "_action": "t2v",
  "model": "<model-id>",
  "prompt": "描述主体、动作、场景和镜头",
  "duration": 5,
  "resolution": "720p"
}'
```
</details>

<details open>
<summary><b>200</b></summary>

```bash
{
  "code": 0,
  "data": {
    "task_id": "video_xxx",
    "task_status": "pending",
    "urls": []
  },
  "message": "success",
  "request_id": "req_xxx"
}
```
</details>

若响应直接包含 `urls`，可立即读取结果；若返回 `task_id`，请调用[查询视频任务](/docs/common/video-task.md)直到进入成功或失败终态。
