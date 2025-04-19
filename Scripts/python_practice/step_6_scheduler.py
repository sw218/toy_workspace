import schedule
import time

def job():
    print("출근 체크! 지금은 오전 9시!")

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
