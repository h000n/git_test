import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup
def image():
    print("s")
    # Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
    driver = webdriver.Chrome(r'C:/Users/hoon/Desktop/pr/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(3)
    # driver.get('https://nid.naver.com/nidlogin.login')
    # driver.find_element_by_name('id').send_keys('naver_id')
    # driver.find_element_by_name('pw').send_keys('mypassword1234')
    # driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    driver.get('http://211.56.5.130:8080/SynapDocViewServer/viewer/doc.html?key=0b4d8b7851434aa5a5fd637c3253c7e6&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    news_list = soup.find_all("div", attrs={"class": "contents-page"})
    print(news_list)
    # for index, news in enumerate(news_list):
    #     print("{}.{}".format(index+1, news_list[index].get_text()))
image()