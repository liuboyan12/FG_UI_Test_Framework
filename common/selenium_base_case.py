import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config
from common.log_utils import logger

'''
    setUpClass的使用demo
'''


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # 针对类级别的
        logger.info('=' * 10 + '测试用例开始' + '=' * 10)
        print('SeleniumBaseCase.setUpClass')
        cls.url = local_config.url

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('=' * 10 + '测试用例结束' + '=' * 10)
        print('SeleniumBaseCase.tearDownClass')

    def setUp(self) -> None:  # 针对方法级别的
        logger.info('-' * 10 + '方法执行开始' + '-' * 10)
        print('SeleniumBaseCase.setUp')
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:

        print('SeleniumBaseCase.tearDown')

        # 差失败截图
        errors = self._outcom.errors
        for test, exc_info in errors:
            if exc_info:
                self.base_page.screenshot_as_file_in_report_page()# report中进行截图
        self.base_page.close_tab()
        logger.info('-' * 10 + '方法执行结束' + '-' * 10)


if __name__ == '__main__':
    unittest.main()
