import glob
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    # 圧縮するファイルを一つずつ指定する必要がある
    # z.write('test_dir')
    # z.write('test_dir/test.txt')

    # まとめて指定する
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)
# 展開する
with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz2')
    # 展開せずファイルを確認する
    with z.open('test_dir/test.txt') as f:
        print(f.read())