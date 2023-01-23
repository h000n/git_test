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



def times(n,m):
    print("카이스트신문")
    print()
    url = "https://times.kaist.ac.kr/news/articleList.html?view_type=sm"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "type2"}).find_all(
        "li", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        titl = news.find("h4", attrs={"class": "titles"})
        title = titl.get_text().strip()
        link = a_tag["href"]
        if m==0:
            print_news(index, title, "https://times.kaist.ac.kr"+link)
        else:
            print_news(index, title,0)

def nkds(n,m):
    print("KAIST 생활관")
    print()
    url = "https://nkds.kaist.ac.kr/board/notice/noticeList.do?lang=ko"
    soup = create_soup(url)
    news_list = soup.find("tbody").find_all(
        "tr", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        titl = news.find_all("em")[0]
        title = titl.get_text().strip()
        link = a_tag["href"]
        if m==0:
            print_news(index, title,0)#link no access
        else:
            print_news(index, title,0)

def clinic(n,m):
    print("KAIST Clinic Pappalardo Center")
    print()
    url = "https://clinic.kaist.ac.kr/boards/lst/notice"
    soup = create_soup(url)
    news_list = soup.find("tbody").find_all(
        "tr", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        if m==0:
            print_news(index, title,"https://clinic.kaist.ac.kr"+link)#link no access
        else:
            print_news(index, title,0)

def herald(n,m):
    print(" The KAIST Herald ")
    print()
    url = "http://herald.kaist.ac.kr/news/articleList.html?sc_section_code=S1N1&view_type=sm"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "type2"}).find_all(
        "h4", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        if m==0:
            print_news(index, title, "http://herald.kaist.ac.kr"+link)
        else:
            print_news(index, title,0)


def heraldop(n,m):
    print(" The KAIST Herald ")
    print()
    url = "http://herald.kaist.ac.kr/news/articleList.html?sc_section_code=S1N12&view_type=sm"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "type2"}).find_all(
        "h4", limit=n)  # 6개까지만 가져오기
    for index, news in enumerate(news_list):
        a_tag = news.find_all("a")[0]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        if m==0:
            print_news(index, title, "http://herald.kaist.ac.kr"+link)
        else:
            print_news(index, title,0)
################################

n = int(input("how many?:"))
m = int(input("link?(yes=0):"))
functions= [heraldop,herald,clinic,nkds,times]
for i in range(len(functions)):
    functions[i](n,m)
    print("-------------------------------------------")
    time.sleep(4*n)