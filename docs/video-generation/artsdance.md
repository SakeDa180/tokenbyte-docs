# ArtsDance 视频生成

提交 ArtsDance 文生视频或图生视频任务

`GET` `https://api.tokenbyte.ai/api/v1/video/generation`

ArtsDance 采用异步任务模式：本接口提交任务并返回 task_id，随后调用[查询视频任务](/docs/common/video-task.md)获取结果。模型列表请查看TokenByte支持的所有[AI 模型](https://tokenbyte.ai/models/)。


## Header 参数
| 参数 | 必填 | 说明 |
| :--- | :--- | :--- |
| `Authorization` | 是 | Bearer <TOKENBYTE_API_KEY> |
| `Content-Type` | 是 | application/json |

## Body 参数
| 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | 是 | 模型列表中的 ArtsDance 模型 ID |
| `prompt` | string | 是 | 场景、运动、镜头与风格描述 |
| `image` | string | 否 | 图生视频参考图 URL 或 Base64；文生视频不传 |
| `duration` | integer | 否 | 视频时长，支持值取决于模型 |
| `aspect_ratio` | string | 否 | 如 `16:9`、`9:16`、`1:1` |
| `resolution` | string | 否 | 输出分辨率档位 |
| `seed` | integer | 否 | 渠道支持时控制随机种子 |
| `generate_audio` | boolean | 否 | 模型支持时控制音频生成 |


### 提示词建议
按“主体动作 + 环境变化 + 镜头运动 + 光线风格”组织提示词。图生视频时避免描述与参考图主体明显冲突的外观细节。
> [!WARNING]
> 参数枚举会随 ArtsDance 模型版本变化。模型不支持的时长、分辨率或音频选项会返回参数错误，请以模型卡片和错误信息为准。


## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl https://api.tokenbyte.ai/api/v1/video/generation \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model":"<artsdance-model-id>",
    "prompt":"无人机穿过晨雾中的峡谷，缓慢前推，电影感",
    "duration":5,
    "aspect_ratio":"16:9"
  }'
```
</details>

<details open>
<summary><b>图生视频</b></summary>

```bash
{
  "model": "<artsdance-model-id>",
  "prompt": "人物转身看向镜头，头发随风摆动",
  "image": "https://example.com/reference.png",
  "duration": 5,
  "aspect_ratio": "9:16"
}
```
</details>

<details open>
<summary><b>Python</b></summary>

```bash
import requests

result = requests.post(
    "https://api.tokenbyte.ai/api/v1/video/generation",
    headers={"Authorization": "Bearer YOUR_KEY"},
    json={"model": "<artsdance-model-id>", "prompt": "云海日出"},
).json()
print(result["data"]["task_id"])
```
</details>

<details open>
<summary><b>200</b></summary>

```bash
{
  "code": 0,
  "data": { "task_id": "video_xxx", "task_status": "pending" },
  "message": "success"
}
```
</details>

