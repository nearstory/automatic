from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#크롬브라우저 Open Options
options = webdriver.ChromeOptions() #옵션 설정하겠다 했다
options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #드라이버 설치 필요없이 옵션 적용한 채로

#함수 시작, 리스트 정의
seller_name = []
seller_number = []
seller_email = []
seller_list = ["nscsh1102","foodasb"]

#함수 정의
def get_seller_info() :
    num = 0
    for i in seller_list :
        #창 오픈
        driver.get("https://smartstore.naver.com/" + i + "/profile?cp=2")
        driver.implicitly_wait(10)
        #수집 및 파싱
        html = driver.page_source
        bsObj = BeautifulSoup(html,"lxml")
        seller_name.append(bsObj.select("div:nth-child(1) > div._2PXb_kpdRh")[0].text)
        seller_number.append(bsObj.select("div:nth-child(3) > div._2PXb_kpdRh > div")[0].text)
        seller_email.append(bsObj.select("div:nth-child(4) > div._2PXb_kpdRh")[0].text)
        print(seller_name[num],",",seller_number[num],",",seller_email[num])
        num += 1
    driver.close()

get_seller_info()