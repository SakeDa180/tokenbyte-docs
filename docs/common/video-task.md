
# 查询视频任务

查询异步视频生成结果

`GET` `https://api.tokenbyte.ai/api/v1/video/task/{task_id}`

视频生成通常是异步任务。提交成功后保存 `task_id`，通过本接口读取进度和最终视频地址。


## 响应字段
| 字段 | 类型 | 说明 |
| :--- | :--- | :--- |
| `task_status` | string | `pending`、`processing`、`succeeded`、`failed` |
| `progress` | number | 渠道提供时返回的百分比 |
| `url` | string | 成功后的视频地址 |
| `message` | string | 失败原因或状态说明 |


## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl "https://api.tokenbyte.ai/api/v1/video/task/$TASK_ID" \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY"
```
</details>

<details open>
<summary><b>200</b></summary>

```bash
{
  "code": 0,
  "data": {
    "task_id": "video_xxx",
    "task_status": "succeeded",
    "url": "https://.../result.mp4"
  },
  "message": "success"
}
```
</details>

