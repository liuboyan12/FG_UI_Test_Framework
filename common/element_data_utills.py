import xlrd
import os
from common.config_utils import local_config

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, local_config.element_info_path)


class ElementsdataUtils:
    # 当前版本page name就是excel的文件名
    def __init__(self, module_name, page_name, element_path=excel_path):  # 有默认值的参数要写在最后
        self.element_path = element_path
        self.excel_path = os.path.join(self.element_path, module_name, page_name)
        self.module_name = module_name
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(0)
        self.page_name = page_name+'.xlsx'
        self.row_count = self.sheet.nrows

    def get_element_data(self):
        element_datas = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i, 2) == self.page_name:
                this_ele_data = {}
                this_ele_data['element_name'] = self.sheet.cell_value(i, 1)
                this_ele_data['locator_type'] = self.sheet.cell_value(i, 2)
                this_ele_data['locator_value'] = self.sheet.cell_value(i, 3)
                time_out_value = self.sheet.cell_value(i, 4)
                this_ele_data['timeout'] = time_out_value if isinstance(time_out_value,
                                                                        float) else local_config.time_out
                element_datas[self.sheet.cell_value(i, 0)] = this_ele_data
        return element_datas


if __name__ == '__main__':
    elements = ElementsdataUtils('login', 'login_page').get_element_data()
    # print(elements)
    for e in elements.values():
        print(e)
