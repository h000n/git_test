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

def tize(list):
    text = list.strip().replace("<br/>", "\n").replace('0원', '').replace(',', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '').replace('<tr>', '').replace('<td>', '').replace('<!-- <ul class="list-st"> -->', '').replace('<ul class="list-st">', '').replace('</ul>', '').replace('<', '').replace('>', '').replace('<', '').replace('>', '').replace('!', '').replace('--', '').replace('amp;', '').replace('amp;', '').replace('&lt;', '').replace('&gt;', '').replace('()', '').strip()
    return text

##################################################

def north(num):
    print("          카이마루(북측카페테리아)")
    print()
    url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=fclt"
    soup = create_soup(url)
    menu_list = soup.find_all("ul", attrs={"class": "list-1st"})
    names = ['조식 8:00~9:30', '중식 11:30~14:00', '석식 17:30~19:00']
    # for q in range(len(menu_list)+1):
    #     print(names[q])
    #     print()
    #     menu_br = str(soup.find_all("tr")[1]).split("/td")[q]
    #     print(tize(menu_br))
    #     print()
    print(names[num])
    print()
    menu_br = str(soup.find_all("tr")[1]).split("/td")[num]
    print(tize(menu_br))
    print()


def west(num):
    print("          서맛골(서측식당)")
    print()
    url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=west"
    soup = create_soup(url)
    menu_list = soup.find_all("ul", attrs={"class": "list-1st"})
    names = ['조식 8:00~9:30', '중식 11:30~14:00', '석식 17:30~19:00']
    # for q in range(len(menu_list)+1):
    #     print(names[q])
    #     print()
    #     menu_br = str(soup.find_all("tr")[1]).split("/td")[q]
    #     print(tize(menu_br))
    #     print()
    print(names[num])
    print()
    menu_br = str(soup.find_all("tr")[1]).split("/td")[num]
    print(tize(menu_br))
    print()


def east(num):
    print("          동맛골(동측학생식당)")
    print()
    url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=east1"
    soup = create_soup(url)
    menu_list = soup.find_all("ul", attrs={"class": "list-1st"})
    names = ['조식 8:00~10:00', '중식 11:30~14:00', '석식 17:30~19:00']
    # for q in range(len(menu_list)+1):
    #     print(names[q])
    #     print()
    #     menu_br = str(soup.find_all("tr")[1]).split("/td")[q]
    #     print(tize(menu_br))
    #     print()
    print(names[num])
    print()
    menu_br = str(soup.find_all("tr")[1]).split("/td")[num]
    print(tize(menu_br))
    print()

n = int(input("what time?(breakfast=0,lunch =1,dinner= 2):"))
functions = [north, east, west]
for i in range(len(functions)):
    functions[i](n)
    print("-------------------------------------------")
    time.sleep(4*n)
time.sleep(100)
