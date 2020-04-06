# import openpyxl 
# wb=openpyxl.Workbook() 
# sheet=wb.active
# sheet.title='new title'
# sheet['A1'] = '漫威宇宙'
# rows= [['美国队长','钢铁侠','蜘蛛侠'],['是','漫威','宇宙', '经典','人物']]
# for i in rows:
#     sheet.append(i)
# print(sheet)
# wb.save('Marvel.xlsx')

# 添加依赖库
import openpyxl
import requests

# 伪装请求头
headers = {
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }

# 爬虫阶段
# url = 'https://www.zhihu.com/people/zhang-jia-wei/posts'
url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'


for i in range(55):
    p = i+1*20
    params ={

        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':p,
        'limit':'10',
        'sort_by':'created',

    }
    res = requests.get(url,headers=headers,params=params)
    json_article = res.json()
    print(json_article)
    page_list = json_article['data']
    for nums in page_list:
        a = nums['title']
        b = nums['id']
        rows=[a,b]
        list1 = []
        list1.append(rows)
        print(rows)


# 写入
wb = openpyxl.Workbook()   
sheet = wb.active
sheet.title = 'article'
sheet['A1']='ID'
sheet['B1']='Article'
for article_nums in list1:
    sheet.append(article_nums)
wb.save('hirme.xlsx')
