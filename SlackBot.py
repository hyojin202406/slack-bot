import requests
from bs4 import BeautifulSoup
import schedule
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# 슬랙 관련 정보
slack_token = 'slack_token'
slack_channel = 'slack_channel'
client = WebClient(token=slack_token)

# 크롤링 정보
crawl_url = 'crawl_url'

# Select 정보
selectEl = ".ellipsis"

# 키워드 정보
keyword = "keyword"

def job():
    print("====== 작업 시작 ======")
    fetch_and_check_emails()
    print("====== 작업 완료 ======")
    
def fetch_and_check_emails():
    try:
        # 웹 페이지 요청
        response = requests.get(crawl_url)
        print(f"페이지 응답 코드: {response.status_code}")
        if response.status_code == 200:
            print("페이지 로드 성공")
            soup = BeautifulSoup(response.text, 'html.parser')
            print("페이지 텍스트 내용:")
            items = soup.select(selectEl)
            print(f"items: {items}")
            print("")
            
            if items:
                for item in items:
                    print(f"item: {item}")
                    
                    if keyword in item.text:
                        print(f'keyword 단어가 포함됨: {item.text}')
                        send_slack_alert()
                    else:
                        print('keyword 단어가 포함되지 않음.')   
            else:
                print('items 섹션을 찾을 수 없습니다.')
        else:
            print("페이지 로드 실패")
    except SlackApiError as e:
        assert e.response["error"]

def send_slack_alert():
    print("슬랙 알림 전송")
    try:
        response = client.chat_postMessage(
            channel=slack_channel,
            text="keyword가 감지되었습니다!"
        )
        print("슬랙 알림 전송 성공")
    except SlackApiError as e:
        print(f"슬랙 알림 전송 실패: {e.response['error']}")

# 5분마다 작업 실행
schedule.every(5).minutes.do(job)

# 스케줄러 시작 및 초기 작업 실행
print("스케줄러 시작 및 초기 작업 실행")
job()  # 초기 실행
while True:
    try:
        schedule.run_pending()
    except Exception as e:
        print(f"오류 발생: {e}")
    time.sleep(1)
