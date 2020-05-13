# @Time : 2020/5/5 11:34 

# @Author : Aliun.Liu

# @File : login_test.py 

# @Software: PyCharm
import unittest

from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class LoginTest(SeleniumBaseCase):
    def setUp(self) -> None:
        super().setUp()
        print('LoginTest.setUp.print')
        self.test_class_data = TestDataUtils('login_suite', 'LoginTest').convert_exceldata_to_testdata()

    @unittest.skipIF(True,'')
    def test_login_success(self):
        test_function_data = self.test_class_data('test_login_access')
        self._testMethodDoc = test_function_data['test_name']  # 这里是干嘛的？？？？？？？？
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'),
                                               test_function_data['test_parameter'].get('password'))
        actual_result = main_page.get_user_name()
        self.assertEqual(actual_result, test_function_data['excepted_result'], 'test_login_success用例执行失败')


if __name__ == '__main__':
    pass
