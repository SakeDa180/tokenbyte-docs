
# 查询图像任务

查询异步图像生成结果

`GET` `https://api.tokenbyte.ai/api/v1/image/task/{task_id}`

部分图像生成与编辑渠道异步返回 `task_id`。使用该 ID 查询状态，直到任务进入终态。

## 请求头

| Path 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `task_id` | string | 是 | 提交图像任务时返回的任务 ID |


## 响应列表
| 状态 | 说明 |
| :--- | :--- |
| `pending` | 等待调度 |
| `processing` | 正在生成 |
| `succeeded` | 生成完成，读取 `data.urls` |
| `failed` | 生成失败，读取 `message` |
建议使用 2、4、8 秒递增间隔轮询，终态后立即停止。

## 示例代码
<details open>
<summary><b>cURL</b></summary>

```bash
curl "https://api.tokenbyte.ai/api/v1/image/task/$TASK_ID" \
  -H "Authorization: Bearer $TOKENBYTE_API_KEY"
```
</details>

<details open>
<summary><b>200</b></summary>

```bash
{
  "code": 0,
  "data": {
    "task_id": "img_xxx",
    "task_status": "succeeded",
    "urls": ["https://.../result.png"]
  },
  "message": "success"
}
```
</details>

