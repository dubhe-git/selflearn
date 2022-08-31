from sched import scheduler
from unittest import result
import requests
import schedule
import time
# from APScheduler.schedulers.blocking import BlockingSchedul
# myCompany 服务报 403


url = 'https://wx.batar.cn/account/login'
headers = {
'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36 Edg/104.0.1293.63'
}
data = {
'loginName': 'dlc', 
'password': '123456', 
}


a = 0
b = 0



def job():
    print(a)
    print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
    login_in = requests.post(url,headers=headers,data=data)
    res_result =  login_in.status_code
    if res_result == 200:
        pass
    elif res_result == 403:
        # b = b+1
        # print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        # print(b)
        params = {
            "msg_type": "text",
            "content": {"text": '这老六，特么系统又崩了。报错 403'},
        }
        resp = requests.post(url='https://open.feishu.cn/open-apis/bot/v2/hook/22dde80b-ed31-4878-8eed-82ad2913e3e9', json=params)
    else:
        pass
# BlockingScheduler
schedule.every(10).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)