import re
import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import time

def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def navern():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=228"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "type06_headline"}).find_all(
        "li", limit=10)  # 3개까지만 가져오기
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1  # img 태그가 있으면 1번째 a 태그의 정보를 사용
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        print("{}. {}\n".format(index+1, title))
    print()


def donga():
    print("[Donga 뉴스]")
    url = "http://dongascience.donga.com/news.php?dsNews=on"
    soup = create_soup(url)
    news_list = soup.find_all("span", attrs={"class": "tit"})
    for index in range(len(news_list)):
        print("{}.{}\n".format(index+1, news_list[index].get_text()))


def samsung():
    print("[samsung 뉴스]")
    url = "https://news.samsung.com/kr/latest/"
    soup = create_soup(url)
    news_list = soup.find_all("span", attrs={"class": "title ellipsis"})
    for index in range(len(news_list)):
        print("{}.{}\n".format(index+1, news_list[index].get_text()))


def seoul():
    print("[seoul 뉴스]")
    url = "https://www.snu.ac.kr/research/highlights"
    soup = create_soup(url)
    news_list = soup.find_all("div", attrs={"class": "title"})
    for index in range(len(news_list)):
        print("{}.{}\n".format(index+1, news_list[index].get_text()))

def physi():
    print("[physi 뉴스]")
    url = "https://phys.org/physics-news/"
    soup = create_soup(url)
    news_list = soup.find_all("a", attrs={"class": "news-link"}, limit=10)
    for index in range(len(news_list)):
        title = news_list[index].get_text()
        result = ""
        client_id = "jIS6lUO8XFEk49xSyoDC"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "dZXsKl6acA"  # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(title)
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            result = json.loads(response_body)['message']['result']['translatedText']
        print("{}.{} \n(trans: {})\n".format(index+1, title ,result))

def nature():
    print("[nature 뉴스]")
    url = "https://www.nature.com/nature/articles/?type=review,news-and-views,perspective,hypothesis,analysis"
    soup = create_soup(url)
    news_list = soup.find_all("a", attrs={"data-track-action": "view article"}, limit=10)
    for index in range(len(news_list)):
        title = news_list[index].get_text().replace(" ","").replace("\n","")
        result = ""
        client_id = "F2bmQndPnttgzPDQG3XB"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "YJ3zLPkygL"  # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(title)
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            result = json.loads(response_body)['message']['result']['translatedText']
        print("{}.{} \n(trans: {})\n".format(index+1, title ,result))

def science():
    print("[science 뉴스]")
    url = "https://www.sciencemag.org/news/latest-news"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "headline-list"}).find_all("li", limit=10)
    for index in range(len(news_list)):
        title = news_list[index].find_all("a")[1].get_text().strip()
        client_id = "wY32gmhcHn_imArMcLWs"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "MGnmqZxmJF"  # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(title)
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            result = json.loads(response_body)['message']['result']['translatedText']
        print("{}.{} \n(trans: {} )\n".format(index+1,title,result))
        
functions= [navern,donga,samsung,seoul,physi,nature,science]
if __name__ == "__main__":
    for i in range(len(functions)):
        functions[i]()
        time.sleep(15)
    time.sleep(10)
