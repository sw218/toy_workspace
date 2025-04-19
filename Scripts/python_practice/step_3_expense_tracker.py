import pandas as pd
import datetime

# pip install openpyxl (필수 패키지)

spendings = []

while True:
    item = input("지출 항목 (종료하려면 'exit' 입력): ")
    if item.lower() == "exit":
        break
    amount = input("금액: ")
    spendings.append({"항목": item, "금액": int(amount)})

# 날짜 기반 파일명 생성
date_str = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"spending_{date_str}.xlsx"

pd.DataFrame(spendings).to_excel(filename, index=False)
print(f"가계부가 '{filename}'로 저장되었습니다!")
