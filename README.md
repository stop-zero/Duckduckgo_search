# 이미지 크롤링 스크립트

Selenium을 사용하여 DuckDuckGo에서 이미지를 검색하고 다운로드하는 기능 제공


## 사용법

1. 라이브러리 설치

   ```
   pip install selenium webdriver-manager requests
   ```
 
    1.1 문제 해결

      - 만약 `ModuleNotFoundError: No module named 'selenium'` 오류가 발생하면, 

          ```sh
          python -m pip install selenium webdriver-manager requests
          ```

   - 만약 `pip` 명령어가 작동하지 않으면, `pip`를 최신 버전으로 업그레이드 
        
        ```sh
        python -m pip install --upgrade pip
        ```

2. `search_images.py` 파일을 실행하여 이미지를 검색하고 다운로드

   ```sh
   python search_images.py
   ```

3. 검색 키워드 및 다운로드할 이미지 수를 수정 가능



## 파일 구조

- `search_images.py`: 이미지 검색 및 다운로드
- `README.md`



## 스크립트 설명

- `search_images.py`: DuckDuckGo에서 이미지를 검색하고 다운로드
  - `duckduckgo_image_search`: 이미지 검색 및 다운로드 함수
  - `download_image`: 이미지 다운로드 함수
 

## 주의사항

- 이 스크립트는 DuckDuckGo의 이미지 검색을 사용한다.
- [DuckDuckGo의 이용 약관](https://chromewebstore.google.com/detail/duckduckgo-privacy-essent/bkdgflcldnnnapblkhphbgpggdiikppg?hl=ko&pli=1)
