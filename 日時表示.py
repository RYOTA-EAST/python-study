import datetime
# 今の日時
now = datetime.datetime.now()
print(now)
# １週間前の日付
d = datetime.timedelta(weeks=1)
print((now - d).strftime('%Y/%m/%d'))

import time
print("######")
# 5秒後に実行
time.sleep(5)
print("###5病後に実行###")

import os
import shutil
file_name = 'test.txt'
# ファイルがある場合日時を添えてバックアップを作成
if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M')))

with open(file_name, 'w')as f:
    f.write('test')
