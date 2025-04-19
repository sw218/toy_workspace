import random

titles = [
    "Python 초보도 가능한 자동화!",
    "AI 활용 실전 프로젝트!",
    "업무를 10배 빠르게 하는 자동화 팁!"
]

tags = ["Python", "자동화", "AI", "업무효율화", "초보자"]

title = random.choice(titles)
selected_tags = random.sample(tags, 3)

print(f"추천 제목: {title}")
print(f"추천 태그: {', '.join(selected_tags)}")



