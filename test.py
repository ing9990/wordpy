from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from collections import Counter
from wordcloud import WordCloud
import random as rd

page = 1
page = min(page,35)

object = []
cloud = dict()

for i in range(1,page+1):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="+str(i)

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    list = soup.find_all("tr")

    for i in list[7:86]:
        if len(i)==1 :continue
        ob = dict()
        t = i.text.split()
        #ob[t[1]] = t
        cloud[t[1]] = int(int(re.sub("[.,%]","",t[9]))/10000)

        ob["순위"] = int(t[0])
        ob["종목이름"] = t[1]
        ob["가격"] = int(re.sub(",","",t[2]))
        ob["전일비"] = int(re.sub("[,%]","",t[3]))
        ob["등락률"] = float(re.sub("[+,%]","",t[4]))
        ob["시가총액"] = int(re.sub(",","",t[6]))
        ob["거래량"] = int(re.sub(",","",t[9]))
        
        object.append(ob)

c = Counter(cloud)
tag = c.most_common(50)

path = "C:/Users/Taewoo/Anaconda3/Lib/site-packages/wordcloud/abc.ttf"
wc = WordCloud(font_path=path , background_color="white", width=1000,height=700, max_words=60, max_font_size=200)

#wc = WordCloud( background_color="white", width=1000,height=700, max_words=60, max_font_size=200)
wc.generate_from_frequencies(dict(tag))
wc.to_file(str('./images/cloudImage' + str(rd.randint(0,999)) +'.png'))