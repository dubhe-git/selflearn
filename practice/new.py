import requests

params = {
            "msg_type": "text",
            "content": {"text": '这是一条提醒消息，用于 python 自动任务测试。作者：Dubhe'},
        }
resp = requests.post(url='https://open.feishu.cn/open-apis/bot/v2/hook/22dde80b-ed31-4878-8eed-82ad2913e3e9', json=params)
  