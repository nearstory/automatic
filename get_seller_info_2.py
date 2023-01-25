from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #키 제어 기능 불러오기
from selenium.common.exceptions import NoSuchElementException #스크롤 내림 기능, Element 없을 경우
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time #시간 제어

#크롬브라우저 Open Options
options = webdriver.ChromeOptions() #옵션 설정 선언
#options.add_argument("headless")
options.add_argument('window-size=1920x1080') #창 사이즈 조절 옵션
options.add_experimental_option("detach", True) #창 안닫히게 하는 옵션
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #드라이버 설치 필요 생략

seller_name = []
seller_number = []
seller_email = []
search_keyword = ["파파 LED와이드스탠드 800S (블랙) / 학습용 사무용"]
search_box = driver.find_element(By.CSS_SELECTOR,"#__next > input")
search_button = driver.find_element(By.CSS_SELECTOR,"#__next > button._searchInput_button_search_h79Dk > svg > path")

#함수 정의
def get_seller_info() :
    driver.get("https://shopping.naver.com/home")
    # driver.implicitly_wait(10)
    # search_box.send_keys(search_keyword)
    # search_button.click()
    # driver.implicitly_wait(10)
    # driver.find_element(By.CSS_SELECTOR,"div:nth-child(1) > a.basicList_mall__BC5Xu").click()
    # driver.implicitly_wait(10)
    # driver.find_element(By.CSS_SELECTOR,"#pc-categoryMenuWidget > li._1LxaYKFeLm.color_black.N\=a\:lmn\.sellerinfo > a").click()
    # driver.implicitly_wait(10)
    # html = driver.page_source
    # bsObj = BeautifulSoup(html,"lxml")
    # seller_name.append(bsObj.select("div:nth-child(1) > div._2PXb_kpdRh")[0].text)
    # seller_number.append(bsObj.select("div:nth-child(3) > div._2PXb_kpdRh > div")[0].text)
    # seller_email.append(bsObj.select("div:nth-child(4) > div._2PXb_kpdRh")[0].text)
    # print(seller_name,",",seller_number,",",seller_email)
    driver.close()

get_seller_info()