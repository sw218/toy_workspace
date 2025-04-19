# 요일별 일정표 자동 생성기

days = ["월", "화", "수", "목", "금"]
schedule = []

print("요일별 일정을 입력하세요. (건너뛰려면 Enter)")

for day in days:
    plan = input(f"{day}요일 일정: ") or "없음"
    schedule.append(f"{day}요일: {plan}")

# 파일로 저장
with open("weekly_schedule.txt", "w", encoding="utf-8") as f:
    f.write("주간 일정표\n")
    for item in schedule:
        f.write(item + "\n")

print("'weekly_schedule.txt' 파일에 저장되었습니다.")
