import os
import time

#
# 휴지통으로 이동 처리되는게 아닌 즉시 삭제를 하는 프로그램.
#

folder = "C:/Users/kojeomstudio/Downloads"
days_old = 30
now = time.time()

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    if os.path.isfile(path) and (now - os.path.getmtime(path)) > (days_old * 86400):
        os.remove(path)
        print(f"삭제된 파일: {file}")
