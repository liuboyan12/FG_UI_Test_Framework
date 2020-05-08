import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config

'''
    setUpClass的使用demo
'''


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # 针对类级别的
        print('SeleniumBaseCase.setUpClass')
        cls.url = local_config.url

    @classmethod
    def tearDownClass(cls) -> None:
        print('SeleniumBaseCase.tearDownClass')

    def setUp(self) -> None:  # 针对方法级别的
        print('SeleniumBaseCase.setUp')
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        print('SeleniumBaseCase.tearDown')
        self.base_page.close_tab()
        # 差失败截图


if __name__ == '__main__':
    unittest.main()
