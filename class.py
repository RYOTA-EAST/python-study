class Person(object):
    # コンストラクタ(初期化：最初に実行)
    def __init__(self, name):
        self.name = name
        print('初期化')

    def say_something(self):
        print('I am {} hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

    # デストラクタ（インスタンスが破棄される）
    def __del__(self):
        print('good bye')


# インスタンスを作成する
person = Person('Mike')
person.say_something()

# 次のコンストラクタ実行されてから前のデストラクタが動作
person = Person('Ryota')
person.say_something()
