import pytest


# テストの処理をまとめて別ファイルから読み出せるfixture
# yeildを使うとcsvを開いて先で使える、終了時に閉じてくれる
@pytest.fixture
def csv_file():
    yield 'csv file!!!'

# ターミナルで実行した際にオプションから値を取得できる
def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')