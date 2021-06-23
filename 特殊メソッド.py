class Word(object):
    # 初期化
    def __init__(self, text):
        self.text = text
    # 文字列として読み込まれた時
    def __str__(self):
        return 'word!!!'
    # 文字数を返す
    def __len__(self):
        return len(self.text)
    # 足し算
    def __add__(self, word):
        return self.text.lower() + word.text.lower()
    # 等しいか
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()
    # インスタンスが不要になった時
    def __del__(self):
        print('delete')


w = Word('test')
print(w)
print(len(w))
w2 = Word('#########')
print(w + w2)
del w
print('#######')
