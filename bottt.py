from flask import Flask, jsonify, request
import sys
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


def north(num):
    print("          카이마루(북측카페테리아)")
    print()
    url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=fclt"
    soup = create_soup(url)
    menu_list = soup.find_all("ul", attrs={"class": "list-1st"})
    names = ['조식 8:00~9:30', '중식 11:30~14:00', '석식 17:30~19:00']
    menu_br = str(soup.find_all("tr")[1]).split("/td")[num]
    strs = str(names[num])+"\n"+str(tize(menu_br).replace("Kcal",""))
    return strs

def east(num):
    print("          동맛골(동측학생식당)")
    print()
    url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=east1"
    soup = create_soup(url)
    menu_list = soup.find_all("ul", attrs={"class": "list-1st"})
    names = ['조식 8:00~10:00', '중식 11:30~14:00', '석식 17:30~19:00']
    menu_br = str(soup.find_all("tr")[1]).split("/td")[num]
    strs = str(names[num])+"\n"+str(tize(menu_br).replace("Kcal","").replace("구세트","3구세트"))
    return strs


application = Flask(__name__)

@application.route("/bf_N", methods=["POST"])
def bf_N():
    request_data = json.loads(request.get_data().decode('utf-8'))
   # print(request_data)
    params = request_data['action']['params']
    blockinfo= request_data['intent']['name']
    print(blockinfo)
    if blockinfo =="북측아침_block":
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": str(north(0))
                        }
                    }
                ]
            }
        }
    elif blockinfo == "동측아침_block":
    	response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": str(east(0))
                        }
                    }
                ]
            }
        }
    elif blockinfo =="북측점심_block":
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": str(north(1))
                        }
                    }
                ]
            }
        }
    elif blockinfo == "동측점심_block":
    	response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": str(east(1))
                        }
                    }
                ]
            }
        }
    elif blockinfo =="북측저녁_block":
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": str(north(2))
                        }
                    }
                ]
            }
        }
    elif blockinfo == "동측저녁_block":
    	response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": str(east(2))
                        }
                    }
                ]
            }
        }
    elif blockinfo == "저녁_all":
    	response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": str(north(2)+"\n"+east(2))
                        }
                    }
                ]
            }
        }
    elif blockinfo =="그외":
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "제작중..."
                        }
                    }
                ]
            }
        }
    else:
            	response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "Error"
                        }
                    }
                ]
            }
        }
    return jsonify(response)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)