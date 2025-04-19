import re
import os

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file

    def analyze_logs(self, keyword):

        if not os.path.exists(self.log_file):
            print(f"로그 파일이 존재하지 않습니다: {self.log_file}")
            return []

        with open(self.log_file, "r", encoding="utf-8") as file:
            logs = file.readlines()

        matches = [line for line in logs if re.search(keyword, line, re.IGNORECASE)]
        return matches

# 로그 분석 실행
log_analyzer = LogAnalyzer("server.log")
error_logs = log_analyzer.analyze_logs("ERROR")

print(f"🔍 발견된 오류 로그 ({len(error_logs)}건):")
for log in error_logs:
    print(log.strip())
