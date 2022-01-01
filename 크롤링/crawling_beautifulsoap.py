# %%
pip install bs4

# %% [markdown]
# 
# 라이브러리 페이지 : 
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# 
# 공식문서 : 
# http://omz-software.com/pythonista/docs/ios/beautifulsoup_guide.html

# %%
pip install requests

# %% [markdown]
# requests 모듈이란?
# requests는 python사용자들을 위해 만들어진 간단한 Python용 HTTP 라이브러리이며, 간단하게는 HTTP, HTTPS 웹 사이트에 요청하기 위해 자주 사용되는 모듈 중 하나이고
# 
# Crawling 과정에서 requests모듈을 이용해 웹 사이트의 소스코드를 가져온 다음 파싱을 하는 경우가 많습니다.
# 
# https://github.com/psf/requests
# https://docs.python-requests.org/en/latest/
# 
# 
# 출처: 
# https://me2nuk.com/Python-requests-module-example/
# 

# %%
import requests 
from bs4 import BeautifulSoup

res = requests.get('https://news.v.daum.net/v/20170615203441266')

#html 페이지 파싱 (html데이터, 파싱방법)
soup = BeautifulSoup(res.content, 'html.parser')

#필요한 데이터 검색 
#find : 가장 먼저 검색되는 태그 반환 
#find_all() : 전체 태그 반환 
all = soup.find_all('p')
title = soup.find('title')
contents = soup.find('p')


#태그나 아이디가 아닌 문자열 자체로 검색 
#문자열 정규 표현식 등등으로 검색가능 
print(1, soup.find_all(string='집단'))

#필요 데이터 추출 
print(title.string)
print(contents.string)
for i in range(0, 7):
    print(all[i])


# %% [markdown]
# 예제 
# 다음 사이트에서 링크가 되어있는 모든 제목을 가져와서 출력합니다. 
# https://news.daum.net/digital#1
# 
# 

# %%
import requests 
from bs4 import BeautifulSoup

res = requests.get('https://news.daum.net/digital#1')

#html 페이지 파싱 (html데이터, 파싱방법)
soup = BeautifulSoup(res.content, 'html.parser')

#필요한 데이터 검색 
#find : 가장 먼저 검색되는 태그 반환 
#find_all() : 전체 태그 반환 
allTitle = soup.find_all('strong', class_='tit_thumb')

for i in range(len(allTitle)):
    print(allTitle[i].get_text())

# %% [markdown]
# 풀이 방법 
# 가지고 오고 싶은 정보를 가진 웹페이지 구성요소에
# 개발자 도구를 활용하여 공통된 태그, 클래스, 아이디, 스트링을 확인함 


