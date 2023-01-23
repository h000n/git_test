import re
import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import os 
import time

def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (링크 : {})".format(link))


def navern():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=228"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "type06_headline"}).find_all(
        "li", limit=6)  # 3개까지만 가져오기
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1  # img 태그가 있으면 1번째 a 태그의 정보를 사용
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()


def donga():
    print("[Donga 뉴스]")
    url = "http://dongascience.donga.com/news.php?dsNews=on"
    soup = create_soup(url)
    news_list = soup.find_all("span", attrs={"class": "tit"})
    news_list_2 = soup.find(
        "ul", attrs={"id": "newslist"}).find_all("li", limit=10)
    for index, news in enumerate(news_list):
        print("{}.{}".format(index+1, news_list[index].get_text()))
        link = url.replace("?dsNews=on", "") + \
            news_list_2[index].find("a")["href"]
        print("( link: {} )".format(link))


def samsung():
    print("[samsung 뉴스]")
    url = "https://news.samsung.com/kr/latest/"
    soup = create_soup(url)
    news_list = soup.find_all("span", attrs={"class": "title ellipsis"})
    news_list_2 = soup.find(
        "ul", attrs={"class": "item"}).find_all("li", limit=10)
    for index, news in enumerate(news_list):
        print("{}.{}".format(index+1, news_list[index].get_text()))
        link = news_list_2[index].find("a")["href"]
        print("( link: {} )".format(link))
        
# def kaist(): #서버에서 막음
#     print("[kaist 뉴스]")
#     url = "https://news.kaist.ac.kr/news/html/news/?skey=category&sval=%EC%97%B0%EA%B5%AC"
#     soup = create_soup(url)
#     news_list = soup.find_all("strong", attrs={"class":"tis"})
#     ul = soup.find("div", attrs={"class":"board col_3"}).find("ul")
#     news_list_2 = ul.find_all("li", limit=10)
#     for index, news in enumerate(news_list):
#         print("{}.{}".format(index+1,news_list[index].get_text()))
#         link = news_list_2[index].find("a")["href"]
#         print("( link: {} )".format(link))


def seoul():
    print("[seoul 뉴스]")
    url = "https://www.snu.ac.kr/research/highlights"
    soup = create_soup(url)
    news_list = soup.find_all("span", attrs={"class": "txt"})
    ul = soup.find("div", attrs={"class": "board-research"}).find("tbody")
    news_list_2 = ul.find_all("tr", limit=10)
    for index, news in enumerate(news_list):
        print("{}.{}".format(index+1, news_list[index].get_text()))
        link = "https://www.snu.ac.kr/" + news_list_2[index].find("a")["href"]
        print("( link: {} )".format(link))
def physi():
    print("[physi 뉴스]")
    url = "https://phys.org/physics-news/"
    soup = create_soup(url)
    news_list = soup.find_all("a", attrs={"class": "news-link"}, limit=10)
    for index, news in enumerate(news_list):
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
        print("{}.{} (trans: {})".format(index+1, title ,result))
        link = news_list[index]["href"]
        print("( link: {} )".format(link))

def nature():
    print("[nature 뉴스]")
    url = "https://www.nature.com/nature/articles/?type=review,news-and-views,perspective,hypothesis,analysis"
    soup = create_soup(url)
    news_list = soup.find_all("a", attrs={"data-track-action": "view article"}, limit=10)
    for index, news in enumerate(news_list):
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
        print("{}.{} (trans: {})".format(index+1, title ,result))
        link = "https://www.nature.com"+news_list[index]["href"]
        print("( link: {} )".format(link))

def science():
    print("[science 뉴스]")
    url = "https://www.sciencemag.org/news/latest-news"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "headline-list"}).find_all("li", limit=10)
    for index, news in enumerate(news_list):
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
        link = "https://www.sciencemag.org" + news.find("a")["href"]
        print("{}. {} (trans: {} )".format(index+1,title,result))
        print("( link: {} )".format(link))
if __name__ == "__main__":
    navern()
    donga()
    samsung()
    seoul()
    physi()
    nature()
    science()
    time.sleep(100)
    os.system("pause")