# @Time : 2020/5/5 14:46 

# @Author : Aliun.Liu

# @File : quit_action.py 

# @Software: PyCharm
from element_infos.main.main_page import MainPage


class LoginAction:
    def __init__(self,driver):
        self.main_page = MainPage(driver)

    def quit(self):
        # self.main_page.
        pass
