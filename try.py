l = [1, 2, 3]
i = 5
# リストを削除しエラーを発生させる
# del l

# 以下のコードを実行する
try:
    # 成功（リストの最初を表示）
    l[0]
    # エラー（存在しないリストを表示）
    # l[i]
except IndexError as ex:
    print("don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other:{}".format(ex))
# 例外が発生しない時
else:
    print('done')
# エラーが発生しても必ず実行する
finally:
    print('clean up')