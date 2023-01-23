import requests
from bs4 import BeautifulSoup
import time
now = time


def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def tize(list):
    text = list.strip().replace("<br/>", "\n").replace('0원', '').replace(',', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '').replace('<tr>', '').replace('<td>', '').replace('<!-- <ul class="list-st"> -->','').replace('<ul class="list-st">', '').replace('</ul>', '').replace('<', '').replace('>', '').replace('<', '').replace('>', '').replace('!', '').replace('--', '').replace('amp;', '').replace('amp;', '').replace('&lt;', '').replace('&gt;', '').replace('//', '').replace('()', '').replace('Kcal', '').strip()
    return text

##################################################


def north(num):
    print("          카이마루(북측카페테리아)")
    print()
    url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=fclt"
    soup = create_soup(url)
    names = ['조식 8:00~9:00', '중식 11:30~13:30', '석식 17:30~19:00']
    print(names[num])
    print()
    menu_br = str(soup.find_all("tr")[1]).split("/td")[num]
    print(tize(menu_br).replace('Kcal:', ''))

def west(num):
    print("          서맛골(서측식당)")
    print()
    url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=west"
    soup = create_soup(url)
    names = ['조식 8:00~9:30', '중식 11:30~14:00', '석식 17:30~19:00']
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
    names = ['조식 8:00~10:00', '중식 11:30~14:00', '석식 17:30~19:00']
    print(names[num])
    print()
    menu_br = str(soup.find_all("tr")[1]).split("/td")[num]
    print(tize(menu_br))
    print()


n = input("what time?(breakfast=0,lunch =1,dinner= 2):")
functions = [north, east, west]
time_h = now.localtime().tm_hour
time_m = now.localtime().tm_min

if n != '':
    n = int(n)
    for i in range(len(functions)):
        functions[i](n)
        print("-------------------------------------------")
else:
    if  time_h <=9:
        north(0)
    elif time_h<=13 and  time_m <= 30:
        north(1)
    elif time_h<=19:
        north(2)
    else:
        print("Not available")