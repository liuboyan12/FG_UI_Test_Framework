# @Time : 2020/5/5 11:34 

# @Author : Aliun.Liu

# @File : login_test.py 

# @Software: PyCharm

from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase


class LoginTest(SeleniumBaseCase):
    def setUp(self) -> None:
        super().setUp()
        print('LoginTest.setUp.print')

    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        mainpage = login_action.login_success('test01', 'newdream123')
        self.assertEqual(mainpage.get_user_name(), '测试人员1', 'test_login_success用例执行失败')


if __name__ == '__main__':
    pass
