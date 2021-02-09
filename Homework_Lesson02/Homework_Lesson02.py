import requests
from bs4 import BeautifulSoup
import pandas as pd

#封装成函数
def get_page_content(request_url):
    #得到页面内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10) #headers=headers不懂？
    content=html.text #中间码转为字符串
    soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8') #'html.parser'，from_encoding='utf-8'分别是什么作用？
    return soup

#分析当前页面投诉信息
def analysis(soup):
    df=pd.DataFrame(columns=['id','brand','car_model','type', 'desc', 'problem', 'datetime', 'status'])
    # 找到完整的信息框，'div'是标签，
    temp=soup.find('div',class_='tslb_b') #网页上是class='tslb_b'，区别于class_='tslb_b'，怎么解释？
    # 找出所有的tr，即行
    tr_list=temp.find_all('tr') #怎么解读？
    for tr in tr_list:
        td_list=tr.find_all('td')
        if len(td_list)>0:
            id, brand, car_model, type, desc, problem, datetime, status = \
                td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, \
                td_list[5].text, td_list[6].text, td_list[7].text
            print(id, brand, car_model, type, desc, problem, datetime, status)
            temp={} #这里变量名必须是temp吗？
            temp['id'] = id
            temp['brand'] = brand
            temp['car_model'] = car_model
            temp['type'] = type
            temp['desc'] = desc
            temp['problem'] = problem
            temp['datetime'] = datetime
            temp['status'] = status
            df=df.append(temp,ignore_index=True) #ignore_index=False什么意思？
    return df

result=pd.DataFrame(columns=['id','brand','car_model','type', 'desc', 'problem', 'datetime', 'status'])

#请求URL
first_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
page_num=10
for i in range(page_num):
    #拼接当前页面url
    request_url=first_url+str(i+1)+'.shtml'
    #得到soup解析
    soup=get_page_content(request_url)
    #得到当前页面的df
    df=analysis(soup) #这里df和前面的df数组变量名重复没有影响吗？
    result=result.append(df)

print(result)
result.to_excel('Homework_Lesson02.xlsx')


