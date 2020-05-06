import xlrd
import os
from common.config_utils import local_config

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../elements_data/element_info.xlsx')


class ElementsdataUtils:
    def __init__(self, module_name, page_name, element_path=excel_path):  # 有默认值的参数要写在最后
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(module_name)
        self.page_name = page_name
        self.row_count = self.sheet.nrows

    def get_element_data(self):
        element_datas = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i, 2) == self.page_name:
                this_ele_data = {}
                this_ele_data['element_name'] = self.sheet.cell_value(i, 1)
                this_ele_data['locator_type'] = self.sheet.cell_value(i, 3)
                this_ele_data['locator_value'] = self.sheet.cell_value(i, 4)
                time_out_value = self.sheet.cell_value(i, 5)
                this_ele_data['timeout'] = time_out_value if isinstance(time_out_value,
                                                                        float) else local_config.time_out
                element_datas[self.sheet.cell_value(i, 0)] = this_ele_data
        return element_datas


if __name__ == '__main__':
    elements = ElementsdataUtils('LoginPage', 'login_page').get_element_data()
    # print(elements)
    for e in elements.values():
        print(e)
