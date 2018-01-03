#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 0003 下午 15:40
# @Author  : BLKStone
# @Site    : http://blkstone.github.io
# @File    : auto_backup.py
# @Software: PyCharm

import openpyxl
import os
import subprocess


class BackupExcelReader(object):
    def __init__(self, path='backup_list.xlsx'):
        self.path = path

    def show_sheets(self, sheets):
        print '[*] 查看sheet列表: [',
        for sheet in sheets:
            print sheet+',',
        print ']'

    def get_url_list(self):
        path = self.path
        print '[*] 备份清单路径：', path
        wb = openpyxl.load_workbook(filename=path)
        sheets = wb.get_sheet_names()
        sheet_name = sheets[0]
        ws = wb.get_sheet_by_name(sheet_name)  # 获取特定的 worksheet

        self.show_sheets(sheets)

        url_list = []
        # 获取表格所有行和列，两者都是可迭代的
        rows = ws.rows
        columns = ws.columns
        for idx, row in enumerate(rows):
            if idx == 0:
                continue
            # print type(row)
            # print '[+] git clone', row[1].value
            url_list.append(row[1].value)

        return url_list


if __name__ == '__main__':

    backup_list_path = 'D:\\pydev\\github_auto_backup\\backup_list.xlsx'
    dest_path = 'D:\github_backup'
    backup_reader = BackupExcelReader(path=backup_list_path)

    os.chdir(dest_path)
    url_list = backup_reader.get_url_list()
    for url in url_list:
        print '[+] git clone', url
        subprocess.call(["git", "clone", url])

