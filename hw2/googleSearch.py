from googlesearch import search

query = "美國第35任總統，是美國頗具影響力的甘迺迪政治家族成員，被視為美國自由派的代表"

import requests
from bs4 import BeautifulSoup

# 下載 Yahoo 首頁內容
# r = requests.get('https://www.google.com/search?q=%E7%BE%8E%E5%9C%8B%E7%AC%AC35%E4%BB%BB%E7%B8%BD%E7%B5%B1%EF%BC%8C%E6%98%AF%E7%BE%8E%E5%9C%8B%E9%A0%97%E5%85%B7%E5%BD%B1%E9%9F%BF%E5%8A%9B%E7%9A%84%E7%94%98%E8%BF%BA%E8%BF%AA%E6%94%BF%E6%B2%BB%E5%AE%B6%E6%97%8F%E6%88%90%E5%93%A1%EF%BC%8C%E8%A2%AB%E8%A6%96%E7%82%BA%E7%BE%8E%E5%9C%8B%E8%87%AA%E7%94%B1%E6%B4%BE%E7%9A%84%E4%BB%A3%E8%A1%A8&rlz=1C5CHFA_enTW895TW895&oq=%E7%BE%8E%E5%9C%8B%E7%AC%AC35%E4%BB%BB%E7%B8%BD%E7%B5%B1%EF%BC%8C%E6%98%AF%E7%BE%8E%E5%9C%8B%E9%A0%97%E5%85%B7%E5%BD%B1%E9%9F%BF%E5%8A%9B%E7%9A%84%E7%94%98%E8%BF%BA%E8%BF%AA%E6%94%BF%E6%B2%BB%E5%AE%B6%E6%97%8F%E6%88%90%E5%93%A1%EF%BC%8C%E8%A2%AB%E8%A6%96%E7%82%BA%E7%BE%8E%E5%9C%8B%E8%87%AA%E7%94%B1%E6%B4%BE%E7%9A%84%E4%BB%A3%E8%A1%A8&aqs=chrome..69i57.794j0j4&sourceid=chrome&ie=UTF-8')
_headers = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'cookie':'CGIC=IocBdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45; 1P_JAR=2020-12-04-04; NID=204=wN7wT7ib3IEaOfrU5gG0a84aJyxUD5rfWn-LmYjlasr9H0MQodVfhpdY2SrS4kCrZr-NYVbH3VRK3horBOCQl_q6aZ0Cc18keRJSj5E_PRdUjexCgRi96_8ET9rA1qx5EI-ze7Bf_lNgRCgcQmsCWVkgicvW7bHYxTKPBtaIrkM'
        }

question = '下列何種不是俠盜獵車手V的三個主要角色?'
r = requests.get('https://www.google.com/search?q=' + question + '&#hl=zh-TW&lr=lang_zh-TW',
headers=_headers)

arr = []
# 確認是否下載成功
if r.status_code == requests.codes.ok:
    print('123')
    # 以 BeautifulSoup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    # 以 CSS 的 class 抓出各類頭條新聞
    stories = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    for s in stories:
        print(s.text)
        arr.append(s.text)
      # # 新聞標題
      # print("標題：" + s.text)
      # # 新聞網址
      # print("網址：" + s.get('href'))

    with open('test.html', 'w') as f:
        f.write(str(soup))

