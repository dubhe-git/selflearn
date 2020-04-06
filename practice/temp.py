import requests
# 引用csv
import csv
# 调用open()函数打开csv文件，传入参数：文件名“articles.csv”、写入模式“w”、newline=''。
csv_file=open('articles.csv','w',newline='',encoding='utf-8')
# 用csv.writer()函数创建一个writer对象。
writer = csv.writer(csv_file)
# 创建一个列表
list2=['标题','链接','摘要']
# 调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “标题”和“链接”和"摘要"。
writer.writerow(list2)
# 使用headers是一种习惯
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 设置offset的起始值为10
offset=10

while True:
    # 封装参数
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':str(offset),
        'limit':'10',
        'sort_by':'voteups',
        }
    # 发送请求，并把响应内容赋值到变量res里面
    res=requests.get(url,headers=headers,params=params)
    # 确认这个response对象状态正确 
    print(res.status_code)
    # 如果响应成功，继续
    if int(res.status_code) == 200:
        articles=res.json()
        print(articles)
        # 定位数据
        data=articles['data']
    
        for i in data:
            # 把目标数据封装成一个列表
            list1=[i['title'],i['url'],i['excerpt']]
            # 调用writerow()方法，把列表list1的内容写入
            writer.writerow(list1)  
        # 在while循环内部，offset的值每次增加20
        offset=offset+20
        if offset > 30:
            break

# 写入完成后，关闭文件就大功告成
csv_file.close()
print('okay') 