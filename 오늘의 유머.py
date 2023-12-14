# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 주소
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        #URL주소
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

        # <td class="subject">
        #     <a href="/board/view.php?table=bestofbest&amp;no=472421&amp;s_no=472421&amp;page=1" target="_top">카페인에 너무 의존하면 생기는 일</a>

        for item in list:
                try:
                        title = item.find("a").text.strip()
                        # print(title)
                        if (re.search('미국', title)):
                                print(title)
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
