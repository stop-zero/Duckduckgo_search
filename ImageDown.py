from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import requests

def download_image(url, folder_path, image_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder_path, image_name), 'wb') as f:
                f.write(response.content)
        else:
            print(f"다운로드 실패: {url}")
    except Exception as e:
        print(f"이미지 다운로드 에러 발생: {url}: {e}")

def duckduckgo_image_search(keywords, max_results, download_path):
    # Chrome 드라이버 설정
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 선택 사항: 헤드리스 모드로 실행
    driver = webdriver.Chrome(service=service, options=options)
    
    # 폴더가 존재하지 않으면 생성
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # DuckDuckGo 이미지 검색 URL
    search_url = f"https://duckduckgo.com/?q={keywords}&t=h_&iax=images&ia=images"
    driver.get(search_url)
    
    time.sleep(2)  # 페이지 로드를 기다림
    
    # 더 많은 이미지를 로드하기 위해 페이지를 스크롤
    for _ in range(5):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(1)
    
    # 이미지 요소 선택
    images = driver.find_elements(By.CSS_SELECTOR, "img.tile--img__img")
    
    count = 0
    for img in images:
        if count >= max_results:
            break
        src = img.get_attribute('src')
        if src and src.startswith('http'):
            # 이미지 다운로드
            download_image(src, download_path, f"{keywords}_{count+1}.jpg")
            count += 1
        else:
            print(f"Skipping image with invalid src: {src}")
    
    driver.quit()

keywords = "푸바오"
max_results = 10
download_path = "DownloadFile"

duckduckgo_image_search(keywords, max_results, download_path)
