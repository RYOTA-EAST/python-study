f = open('test.txt', 'w')
f.write('test\n')
print('My','name', 'is', 'mike', sep='#', end='!', file=f)
f.close()

# r+は読み込み先がないとエラーw+は最初にリセット
with open('test.txt', 'r+') as f:
    f.write('test\n')
    print('MY','name', 'is', 'mike', sep='#', end='!', file=f)
    f.seek(0)
    print(f.read())

    # １ラインごとに読み出す
    while True:
        chunk = 2
        line = f.read(chunk) #行ごとにchunk(2文字)づつ読む
        print(line)
        if not line:
            break

    # 文字を指定して実行する
    print(f.tell()) #現在位置を示す
    print(f.read(1)) #読む文字数
    f.seek(4) #最初から何文字目(enterも一文字)
    print(f.read(5))
    f.seek(13)
    print(f.read(3))