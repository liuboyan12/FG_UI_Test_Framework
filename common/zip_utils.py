# encoding:utf-8
# @Time: 2020/5/10 10:03 
# @Author: Aliun.Liu
# @File: zip_utils.py
# @Software: PyCharm
# @desc:


import os
import zipfile


def zip_dir(dir_path, zip_path):
    zip = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    for root, dirnames, filenames in os.walk(dir_path):
        file_path = root.replace(dir_path, '')
        for filename in filenames:
            zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
    zip.close()
