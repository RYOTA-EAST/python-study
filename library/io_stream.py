import io
import requests
import zipfile

import aaa

import aaa

# with open('/tmp/a.txt', 'w') as f:
#     f.write('test.test')
#
# with open('/tmp/a.txt', 'r') as f:
#     print(f.read())

# 一時ファイルに保存する
# f = io.BytesIO()
# f.write(b' string io test ')
# f.seek(0)
# print(f.read())


url = ('https://files.pythonhosted.org/packages/29/55/'
       '4c68ee6236b36fb6032437b93c635246510fb001d700467f4063a214916a/setuptools-3.8.1.zip')

f = io.BytesIO()

# ダウンロードして一時ファイルに保存する
r = requests.get(url)
f.write(r.content)

# 圧縮ファイルを解凍して中身を確認する
with zipfile.ZipFile(f) as z:
    with z.open('setuptools-3.8.1/README.txt') as r:
        print(r.read().decode())