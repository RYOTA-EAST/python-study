# while　Trueで無限ループ、breakは終了、continueは次
# inputで文字入力
num = 0
while True:
    num = int(input('正の数を入力：'))
    if num > 0:
        print('正の数が入力さてました：', num)
        break
    elif num == 0:
        print('zeroが入力さてました：', num)
        break
    else:
        print('負の数でないですもう一度入力してください')
        continue

# enumerateでリスト（配列）数をカウントする
print('*****enumerate*****')
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i+1, fruit)
    if fruit == 'banana':
        print('stop eating')
        break
# 変数の値を変化ながらループ。開始、終了、ステップを指定する
print('*****range*****')
for i in range(2, 10, 2):
    print(i)


