import unittest
import calculation

release_name = 'lesson2'


class CalTest(unittest.TestCase):
    # テスト前に実行setUp、終了後に実行tearDown
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    # 条件分岐でスキップできる
    @unittest.skipIf(release_name == 'lesson', 'skip')
    def test_add_num_and_double(self):
        # テストする関数や引数、期待値入力してテストする
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        # エラーが出ることを確認するにはwithを使う
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')