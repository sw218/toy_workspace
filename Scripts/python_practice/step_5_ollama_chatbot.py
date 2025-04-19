import subprocess

model = "gemma3:1b"

def chatbot(prompt):
    response = subprocess.run(
        f"ollama run {model} {prompt}",
        shell=True,
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return response.stdout

print("Notice >> exit를 입력하면 종료합니다.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ollama 챗봇을 종료합니다.")
        break
    print("Bot:", chatbot(user_input))
