import os

# 대상 디렉토리 설정
directory = "your_directory_path_here"

def convert_crlf_to_lf(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    
    # CRLF -> LF 변환
    content = content.replace(b'\r\n', b'\n')
    
    with open(file_path, 'wb') as file:
        file.write(content)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            convert_crlf_to_lf(file_path)
            print(f"Converted: {file_path}")

if __name__ == "__main__":
    process_directory(directory)
    print("CRLF to LF conversion completed.")

///////////////////////////////////

-> 프로그래밍 언어를 새롭게 배운다.

 0) chat gpt 
   - 프롬프트를 최대한 잘 작성해서 질의. ( 핵심 / 가치 / 철학/ 아키텍처 )
   - 실무 관련 키워드 ()
   -

-> 정보 수집 / 요약 / 전체 그림을 그려보는 것.


 1) 책 ->  유명한 /근본 있는 서적 / effective c++ c# / d
 2) 인터넷 강의 ~> 실무 쿡북
 3) 유튜브 ~> 실무 쿡북

 4) 아는 분 한테 핵심만 물어본다.

 5) 구글링

==> 입문 -> 적응 -> 숙달 (반복) -> 구조 -> 마스터


-> 
( ㄴㄴㄴ )  (   ) ( ㅁㅇㄴㅁㅇㅁㄴㅇ  ) (    ) (ㄴㄴㄴㄴ) (   )(   )( ㄴㅇ  )(   )(12   )
 ~> c++ / python 

/             

C++ / c# / ~> python


