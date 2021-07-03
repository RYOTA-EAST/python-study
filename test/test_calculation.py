import os

import pytest
import calculation

is_release = False

class TestCal(object):
    # 実行前setup,実行後teardown,クラスにすると最初と最後のみ
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_file_name = 'test.txt'
        cls.test_dir ='/tmp/test_dir'

    def teardown_class(cls):
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    # def setup_method(self, method):
    #     print('setup_method = {}'.format(method.__name__))
        # self.cal = calculation.Cal()

    # def teardown_method(self, method):
    #     print('teardown_method = {}'.format(method.__name__))
        # del self.cal

    # def test_add_num_and_double(self, request):
    #     os_name = request.config.getoption('--os-name')
    #     if os_name == 'mac':
    #         print('ls')
    #     elif os_name == 'windows':
    #         print('dir')
    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    # テストの際に作成した一時ディレクトリtmpdir
    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    @pytest.mark.skipif(is_release==True, reason='skip!')
    def test_add_num_and_double_raise(self):
        # エラーが出ることを確認するにはwithを使う
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

    def test_add_num_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
