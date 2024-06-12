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
    options.add_argument("--headless")  # 선택사항: 브라우저를 표시하지 않고 실행
    driver = webdriver.Chrome(service=service, options=options)
    
    # 폴더가 없으면 생성
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    search_url = f"https://duckduckgo.com/?q={keywords}&t=h_&iax=images&ia=images"
    driver.get(search_url)
    
    time.sleep(2)  # 페이지가 로드될 때까지 대기
    
    # 더 많은 이미지를 로드하기 위해 스크롤 다운
    for _ in range(5):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(1)
    
    images = driver.find_elements(By.CSS_SELECTOR, "img.tile--img__img")
    
    count = 0
    for img in images:
        if count >= max_results:
            break
        src = img.get_attribute('src')
        if src and src.startswith('http'):
            download_image(src, download_path, f"{keywords}_{count+1}.jpg")
            count += 1
        else:
            print(f"잘못된 src를 가진 이미지 스킵: {src}")
    
    driver.quit()

# 퍼스널 컬러와 해당하는 연예인 목록
tones = {
    '봄 웜톤': [
        '아이유', '배수지', '유인나','김세정', '윤아', '혜리',  
    ],
    '가을 웜톤': [
         '고준희', '정유미', '김희선', '이연희', '한가인', '문지인',   
    ],
    '여름 쿨톤': [
        '아이린',  '하니', '박시연', '태연', '김수현', '김고은', 
    ],
    '겨울 쿨톤': [
        '현아', '티파니', '이나영', '김혜수', '김소연', '김하늘',  
    ]
}

path = 'PersonalColor' 
max_results = 10  

for tone, names in tones.items():
    label = tone 
    folder_path = os.path.join(path, label)
    
    for name in names:
        keywords = name  # 검색 키워드
        print(f"{label}에서 {keywords}의 이미지 검색 중")
        duckduckgo_image_search(keywords, max_results, folder_path)
