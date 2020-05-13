# encoding:utf-8
# @Time: 2020/5/8 21:37 
# @Author: Aliun.Liu
# @File: run_all_case.py 
# @Software: PyCharm
# @desc:
import os
import unittest

from common import HTMLTestReportCN, zip_utils
from common.config_utils import local_config
from common.email_utils import EmailUtils

current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path, '..', local_config.case_path)
report_path = os.path.join(current_path, '..', local_config.report_path)


class RunAllTests(object):
    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = '自动化测试报告'
        self.description = '测试报告'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_test.py',
                                                       top_level_dir=self.test_case_path)
        main_suite = unittest.TestSuite()
        main_suite.addTest(discover)
        # 启动测试时创建文件夹并获取报告的名字
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(title=self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        print(report_path)
        fp = open(report_path, "wb")
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=self.title, description=self.description,
                                                 tester=input('请输入你的名字：'))
        runner.run(main_suite)
        fp.close()
        return dir_path


if __name__ == '__main__':
    dir_path = RunAllTests().run()
    reprot_zip_path = dir_path + '/../禅道自动化测试报告.zip'
    zip_utils.zip_dir(dir_path, reprot_zip_path)
    EmailUtils('自动化测试报告（正式版）', 'python自动化测试报告', reprot_zip_path)
