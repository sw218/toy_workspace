import requests

url = "https://raw.githubusercontent.com/kojeomstudio/toy_workspace/main/Resources/sample_drawing.JPG"
response = requests.get(url)

if response.status_code == 200:
    with open("sample_drawing.jpg", "wb") as file:
        file.write(response.content)
    print("이미지가 'sample_drawing.jpg'로 저장되었습니다.")
else:
    print(f"다운로드 실패: {response.status_code}")
