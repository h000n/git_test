import re
import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import os 
import time

def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def print_news(index, title, link):
    print("{}. {}".format(index+1, title,0))
    if link==0:
        print(" ")
    else:
        print("  (링크 : {})".format(link))

##################################



def molit(n,m):
    print("국토교통부")
    print()
    url = "http://www.molit.go.kr/USR/NEWS/m_35045/lst.jsp"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "bd_lst_ul bd_thum_row bd_toon"}).find_all(
        "li", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        titl = news.find_all("strong")[0]
        title = titl.get_text().strip()
        link = a_tag["href"]
        if m==0:
            print_news(index, title, "http://www.molit.go.kr/USR/NEWS/m_35045/"+link)
        else:
            print_news(index, title,0)

def cha(n,m):
    print("문화재청")
    print()
    url = "https://www.cha.go.kr/cop/bbs/selectBoardList.do?bbsId=BBSMSTR_1002&mn=NS_01_03"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "photo_board"}).find_all(
        "li", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        titl = news.find_all("strong")[0]
        title = titl.get_text().strip()
        link = a_tag["href"]
        if m==0:
            print_news(index, title, "https://www.cha.go.kr/"+link)
        else:
            print_news(index, title,0)

def moel(n,m):
    print("고용 노동부")
    print()
    url = "http://www.moel.go.kr/news/cardinfo/list.do"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "gallery mt_30"}).find_all(
        "li", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        titl = news.find_all("strong")[0]
        title = titl.get_text().replace(" ","")
        title = " ".join(re.split("\s+", title, flags=re.UNICODE))
        link = a_tag["href"]
        if m==0:
            print_news(index, title, "www.moel.go.kr/news/cardinfo/"+link)
        else:
            print_news(index, title,0)

def mafra(n,m):
    print("농림 축산 식품부")
    print()
    url = "https://www.mafra.go.kr/mafra/292/subview.do"
    soup = create_soup(url)
    news_list = soup.find("div", attrs={"class": "list"}).find_all(
        "a", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        title = news.get_text().strip().replace("새글","")
        title = " ".join(re.split("\s+", title, flags=re.UNICODE))
        link = news["href"]
        if m==0:
            print_news(index, title, "https://www.mafra.go.kr"+link)
        else:
            print_news(index, title,0)

def moleg(n,m):
    print("법제처")
    print()
    url = "https://www.moleg.go.kr/board.es?mid=a10501000000&bid=0048"
    soup = create_soup(url)
    news_list = soup.find("div", attrs={"class": "wrap title"}).find_all(
        "li", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        title = a_tag.get_text().strip().replace("새글 ","")
        link = a_tag["href"]
        if m==0:
            print_news(index, title, "https://www.moleg.go.kr"+link)
        else:
            print_news(index, title,0)

################################

def humanrights(n,m):
    print("국가 인권 위원회")
    print()
    url = "https://www.humanrights.go.kr/site/program/board/basicboard/list?boardtypeid=9&menuid=001004001001"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("p", attrs={"class": "txt"})[i].find_all(
            "a", limit=n)  # 6개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"].replace("./v","")
            if m==0:
                print_news(index+i, title, "https://www.humanrights.go.kr/site/program/board/basicboard/v"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def kipo(n,m):
    print("특허청")
    print()
    url = "https://www.kipo.go.kr/ko/kpoBultnMgmt.do?menuCd=SCD0200618&parntMenuCd2=SCD0200052"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("td", attrs={"class": "bbs_tit"})[i].find_all(
            "a", limit=n)  # 6개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.kipo.go.kr/kpo/BoardApp/UnewNotiApp"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def forest(n,m):
    print("산림청")
    print()
    url = "https://www.forest.go.kr/kfsweb/cop/bbs/selectBoardList.do?bbsId=BBSMSTR_1031&mn=NKFS_04_01_01"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("td", attrs={"class": "left"})[i].find_all(
            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.forest.go.kr/"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def mcst(n,m):
    print("문화 체육 관광부")
    print()
    url = "https://www.mcst.go.kr/kor/s_notice/notice/noticeList.jsp"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("tr", attrs={"class": "ac"})[i].find_all(
            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.mcst.go.kr/kor/s_notice/notice/"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def nfa(n,m):
    print("소방청")
    print()
    url = "https://www.nfa.go.kr/nfa/news/firenews/disasterNews/"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("td", attrs={"class": "title"})[i].find_all(
            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.nfa.go.kr/nfa/news/firenews/disasterNews/"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def dapa(n,m):
    print("방위 사업청")
    print()
    url = "http://www.dapa.go.kr/dapa/na/ntt/selectNttList.do;jsessionid=9PrWATGtSWY1fO3Qa9nJ7WMYwRFY16rGTAJr32gjDJCFJlwrpnZjuEvsZd6iGhsU.homewas2_servlet_engine1?bbsId=443&menuId=356"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("td", attrs={"class": "ta_l"})[i].find_all(
            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            if m==0:
                print_news(index+i, title, "http://www.dapa.go.kr"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def mois(n,m):
    print("행정 안전부")
    print()
    url = "https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardList.do?bbsId=BBSMSTR_000000000008"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("td", attrs={"class": "l"})[i].find_all(
            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.mois.go.kr"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def mma(n,m):
    print("병무청")
    print()
    url = "https://www.mma.go.kr/board/boardList.do?mc=usr0000379&gesipan_id=2"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("td", attrs={"class": "text_left"})[i].find_all(
            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            title = " ".join(re.split("\s+", title, flags=re.UNICODE))
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.mma.go.kr/board/"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def moj(n,m):
    print("법무부")
    print()
    url = "https://www.moj.go.kr/moj/223/subview.do"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("td", attrs={"class": "_artclTdTitle"})[i].find_all(
            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            title = " ".join(re.split("\s+", title, flags=re.UNICODE))
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.moj.go.kr"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def unikorea(n,m):
    print("통일부")
    print()
    url = "https://www.unikorea.go.kr/unikorea/news/notice/"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("td", attrs={"class": "title"})[i].find_all(
            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.unikorea.go.kr/unikorea/news/notice/"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def mofa(n,m):
    print("외교부")
    print()
    url = "https://www.mofa.go.kr/www/brd/m_4075/list.do"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find("td", {"data-before": "제목"})
        #[i].find_all(            "a", limit=n)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"].replace("./v","")
            if m==0:
                print_news(index+i, title, "https://www.mofa.go.kr/www/brd/m_4075/v"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def mfds(n,m):
    print("식품 의약품 안전처")
    print()
    url = "https://www.mfds.go.kr/brd/m_74/list.do"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("div", attrs={"class": "center_column"})[10+i].find_all(
            "a", limit=1)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"].replace("./v","")
            if m==0:
                print_news(index+i, title, "https://www.mfds.go.kr/brd/m_74/v"+link)
            else:
                print_news(index+i, title,0)
        i+=1

def opm(n,m):
    print("국무조정실 국무총리비서실")
    print()
    url = "https://www.opm.go.kr/opm/news/press-release.do"
    soup = create_soup(url)
    i=0
    while i<n:
        news_list = soup.find_all("div", attrs={"class": "c-board-title-wrap"})[i].find_all(
            "a", limit=1)  # n개까지만 가져오기
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            if m==0:
                print_news(index+i, title, "https://www.opm.go.kr/opm/news/press-release.do"+link)
            else:
                print_news(index+i, title,0)
        i+=1


#########################

n = int(input("how many?:"))
m = int(input("link?(yes=0):"))
functions= [opm,molit,mfds,unikorea,moj,mma,mois,dapa,nfa,mcst,mafra,forest,kipo,cha,humanrights,moleg,moel]
for i in range(len(functions)):
    functions[i](n,m)
    time.sleep(n/4)