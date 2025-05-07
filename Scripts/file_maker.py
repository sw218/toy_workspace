from datetime import datetime

# 현재 시간을 파일 이름 형식에 맞게 가져오기 ('YYYYMMDD_HHMMSS')
current_time_prefix = datetime.now().strftime('%Y%m%d_%H%M%S')

dest_folder_path = "/tmp"

# 파일 이름 생성 (현재 시간 + '_log.txt')
file_name = f'{dest_folder_path}\\{current_time_prefix}_log.txt'

# 파일 생성 및 실행 시간 기록
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(f'프로그램 실행 시간: {current_time_prefix}\n')

print(f"{file_name} 파일이 생성되었습니다.")
