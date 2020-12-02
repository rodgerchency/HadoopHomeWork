from googlesearch import search

query = "美國第35任總統，是美國頗具影響力的甘迺迪政治家族成員，被視為美國自由派的代表"

import requests
from bs4 import BeautifulSoup

# 下載 Yahoo 首頁內容
# r = requests.get('https://www.google.com/search?q=%E7%BE%8E%E5%9C%8B%E7%AC%AC35%E4%BB%BB%E7%B8%BD%E7%B5%B1%EF%BC%8C%E6%98%AF%E7%BE%8E%E5%9C%8B%E9%A0%97%E5%85%B7%E5%BD%B1%E9%9F%BF%E5%8A%9B%E7%9A%84%E7%94%98%E8%BF%BA%E8%BF%AA%E6%94%BF%E6%B2%BB%E5%AE%B6%E6%97%8F%E6%88%90%E5%93%A1%EF%BC%8C%E8%A2%AB%E8%A6%96%E7%82%BA%E7%BE%8E%E5%9C%8B%E8%87%AA%E7%94%B1%E6%B4%BE%E7%9A%84%E4%BB%A3%E8%A1%A8&rlz=1C5CHFA_enTW895TW895&oq=%E7%BE%8E%E5%9C%8B%E7%AC%AC35%E4%BB%BB%E7%B8%BD%E7%B5%B1%EF%BC%8C%E6%98%AF%E7%BE%8E%E5%9C%8B%E9%A0%97%E5%85%B7%E5%BD%B1%E9%9F%BF%E5%8A%9B%E7%9A%84%E7%94%98%E8%BF%BA%E8%BF%AA%E6%94%BF%E6%B2%BB%E5%AE%B6%E6%97%8F%E6%88%90%E5%93%A1%EF%BC%8C%E8%A2%AB%E8%A6%96%E7%82%BA%E7%BE%8E%E5%9C%8B%E8%87%AA%E7%94%B1%E6%B4%BE%E7%9A%84%E4%BB%A3%E8%A1%A8&aqs=chrome..69i57.794j0j4&sourceid=chrome&ie=UTF-8')

# # 確認是否下載成功
# if r.status_code == requests.codes.ok:
#     print('123')
#     # 以 BeautifulSoup 解析 HTML 程式碼
#     soup = BeautifulSoup(r.text, 'html.parser')

#     # 以 CSS 的 class 抓出各類頭條新聞
#     stories = soup.find_all('div')
#     for s in stories:
#       # 新聞標題
#       print("標題：" + s.text)
#       # 新聞網址
#       print("網址：" + s.get('href'))

#一個非常簡單的Google爬蟲

def Google_Run(keyword):#函式只要輸入關鍵字就行
    url = "https://www.google.com/search?q={}".format(keyword)#組合網址
    rs = requests.get(url)#請求連結
    print(rs.text)
    fp = open("google_rs.txt",'w',encoding="utf-8")#保存資料
    fp.write(rs.text)
    fp.close()
# Google_Run("proxy list filetype:txt")#觸發函式
import json #引用json
from pyquery import PyQuery as pq #引用pyquery 並且採用css 選擇器來進行資料抓取 ，安裝請下 pip install pyquery
def Decode_Result(google_data):
    pq_data = pq(google_data) #初始化py_query
    result_list = pq_data.find(".kCrYT") #透過這個標記 會發現 一共抓到21個結果
    #實際上 google 一頁只會提供10個結果
    end = [] #保存結果的陣列
    for item in result_list:
        link = pq(item).find("a").attr('href')
        #簡單抓取每個內容裡面的連結，會發現不是確的 kCrYT div，會沒有link，所以做以下的判斷
        if link is None: #link == 空值 就跳過
            continue
        print("link:{}".format(link))
        title = pq(item).find("a").text()
        if "瞭解原因" in title:#過濾掉 Google 的雜訊
            continue
        pack = {"title": title, "link": link} #將結果包裝成dict
        end.append(pack)
    return end


fp = open("untitled.html",'r',encoding="utf-8")#為了避免不斷查詢在Google被擋ip 所以用讀取的方式來進行測試
google_data = fp.read()
fp.close()
Google_rs = Decode_Result(google_data)
print(json.dumps(Google_rs))