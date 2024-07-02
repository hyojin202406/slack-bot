# Slack 채널 자동 알림 프로그램
특정 웹 페이지를 주기적으로 크롤링하여 지정된 키워드가 포함된 내용을 감지하면 슬랙(Slack) 채널에 알림을 보내는 프로그램

## 라이브러리 설치
```pip install requests beautifulsoup4 schedule slack_sdk```

# BeautifulSoup
파이썬에서 HTML 및 XML 문서를 구문 분석하고, 데이터를 추출하는 데 사용되는 라이브러리

### 기본 사용법

#### 웹 페이지 요청
```
url = 'http://example.com'
response = requests.get(url)
```

#### HTML 파싱
```
soup = BeautifulSoup(response.text, 'html.parser')
```

##### 제목 태그 추출
```
title = soup.title
print(f"Title: {title.string}")
```

##### 모든 링크 추출
```links = soup.find_all('a')
for link in links:
    print(link.get('href'))```