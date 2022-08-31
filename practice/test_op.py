# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup
#创建会话。
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
}
#添加请求头，避免被反爬虫。

# 获取数据
res_foods = requests.get('https://webstatic.mihoyo.com/hk4e/event/e20190909gacha/index.html?authkey_ver=1&sign_type=2&auth_appid=webview_gacha&init_type=301&gacha_id=4a53d8a25d19df7717af99fea4b46319ec6b57&timestamp=1653954959&lang=zh-cn&device_type=mobile&ext=%7b%22loc%22%3a%7b%22x%22%3a-6379.912109375%2c%22y%22%3a254.108154296875%2c%22z%22%3a-2765.590576171875%7d%2c%22platform%22%3a%22Android%22%7d&game_version=CNRELAndroid2.7.0_R8029328_S8227893_D8227893&plat_type=android&region=cn_gf01&authkey=CIKtVqOB3Q9nnpahjFMGQNyW6iqN%2bM9XABwoYIKKpztwCQU%2bG7d%2fs0NsgsFOTLMHwfzqFDeZavw2ML%2fhOSR%2bWMPsr5xyCbfDr5k96Rtjcp0wUugk1QMJAUYkt7oZkQ5Oj35R06SbHdhkvh%2b1L0z%2f0L7HPL2mSQh%2bymBs6Koij4uqy%2bE5nrZo5bN9sf8PcUO3LU9QdED%2f12ojFksI%2bnfrz8SgtbmsePwHYR93NsQw3YowqqWPTH%2fY9yOclaU6Axo0f9uzjFzQA%2fTC8t%2bFpTszRegbHV%2bQojgtYiZNiF01h4lsnjLbtMm874m8%2bE%2bSEGLq6w2jsUj8z3UWdAFy%2flmjCesrEHHBPoWj7eq6WjkaXdLb0SYOlx%2frrjhdUUsK96zsFYg3ZhoEl3KSmup6lBJqf2UssLgnat8K4WwZCLrzCiHVqHzx5T7fWp%2fNgLhBDXaWJE1gAwlo6VHqRJ2SPBKDkvfANRIrNqEniqFZg8oyIh5i3fJerS2Iub%2bkAGnEhXeqKiDi9CmyNYhgr5cTiJsWU%2bZjF%2bOJK%2fcjflIzA%2f54ksHasmxvzQHWbzjpd4vwx2klDOJKw89xQl9s91nANEL4LHBB0EJSc7xwyuyQEqqDcPF4V%2boUMokZbmOxWFx8Na2f7vSDojjjngizsLrRITQpxDJ%2bZ3aGzgIWIMdqS5yNtGQk9bNtFZbvess%2fdSHN72Fl7sTukC2Yn9ploWpeKJO1qrHP9ovajJq4%2f3UibLHhVp6M%2fYyBjymDbKZFF5S8f3LkQpSxSje8Sp4N8NZqV0QxPpXA0wyxfhH53fRwSAxap2GHaAoT7fY5r93jKldE%2ffZMlRobAZkLxKu82zx%2f0hbQxO%2bkrZacv27D5KXPj3eWvgmKBInU7hWroh9s5aFIJxnrG5yLLZNb%2fvzaVt3Ld15MiokVh52eWYPsnhQSRbVJVThA5aOngtw30oHlHenSi276D0uVMHskTC4e%2fjzZjM3pOvH4FSn9sGNh0P5TMWVcIwUA52RIFrrIEMXfGTu38apFx9Q6OcDoBkjPp0NKWS%2fsrWWn2MU1HCY8cXwkcAjh2QVdV56TsP9YpYFf%2fwO8fOo0%2b0wHSiJRmPKvDbnr7TwCLhdmyZ4nfQDYv2FIdmfNn4H9EljFaCV%2btCEEsCZE23VP4ARNKl5%2b%2fBBFlu6QONz8AOqpKucRaqlUZ99CoaUFHnvePS59U8O84Api6tIXFZlLzmJTHQRRJ98k4u19y5aqY%2bhRbRzuUQQ8hvvvaJXONxbscdhl4OVXyZhJKQ97Ad3V5lGi5cR2XRVZbGASHoR5O9AhvXqky5schLut2PX1vIdom0yMz%2fKhZcjZP7%2bDGu1IowErjJ1%2b1OQnrZbSOLKs1Q%3d%3d&game_biz=hk4e_cn#/log')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')

# # 查找包含菜名和URL的<p>标签
# tag_name = bs_foods.find_all('p',class_='name')
# # 查找包含食材的<p>标签
# tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
# # 创建一个空列表，用于存储信息
# list_all = []
# # 启动一个循环，次数等于菜名的数量
# for x in range(len(tag_name)):
#     # 提取信息，封装为列表。注意此处使用的是<p>标签，而之前是<a>
#     list_food = [tag_name[x].text.strip(),tag_name[x].find('a')['href'],tag_ingredients[x].text.strip()]
#     # 将信息添加进list_all    
#     list_all.append(list_food)
# # 打印
# print(list_all)

# 以下是另外一种解法

# 查找最小父级标签
list_foods = bs_foods.find_all('div',class_='table-content')
# 创建一个空列表，用于存储信息
list_all = []

for food in list_foods:
    # 提取第0个父级标签中的<a>标签
    tag_a = food.find('span',attrs={"class":'cell name item_3'})
    # 菜名，使用strip()函数去掉了多余的空格
    name = tag_a.text
    # 提取第0个父级标签中的<p>标签
    tag_p = food.find('span',attrs={"class":'cell time'})
    # 食材，使用strip()函数去掉了多余的空格
    ingredients = tag_p.text
    # 将菜名、URL、食材，封装为列表，添加进list_all
    list_all.append([name,ingredients])

# 打印
print(list_all)
