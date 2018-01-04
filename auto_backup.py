#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 0003 下午 15:40
# @Author  : BLKStone
# @Site    : http://blkstone.github.io
# @File    : auto_backup.py
# @Software: PyCharm

"""Github Repos Auto Backup v0.1

Demo:
  python auto_backup.py backup backup_list.xlsx --xlsx=D:\github_backup
  python auto_backup.py update --xlsx=D:\github_backup

Usage:
  auto_backup.py backup <source> [--xlsx=<destination>]
  auto_backup.py update [--xlsx=<destination>]
  auto_backup.py (-h | --help)
  auto_backup.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --dst=<destination>     github repos backup path.
  --xlsx=<source>     backup list (excel)

"""

from docopt import docopt
import openpyxl
import subprocess
import os


class BackupExcelReader(object):
    def __init__(self, path='backup_list.xlsx'):
        self.path = path

    def show_sheets(self, sheets):
        print u'[*] 查看sheet列表: [',
        for sheet in sheets:
            print sheet+',',
        print ']'

    def get_sheet_names(self):
        wb = openpyxl.load_workbook(filename=self.path)
        sheets = wb.get_sheet_names()
        return sheets

    def get_urls_list(self):
        path = self.path
        print u'[*] BackupExcelReader 的备份清单：', path
        wb = openpyxl.load_workbook(filename=path)
        sheets = wb.get_sheet_names()

        urls_list = []
        self.show_sheets(sheets)
        for sheet_name in sheets:
            print u'[*] 获取', sheet_name, u'(sheet) 中的URL'
            ws = wb.get_sheet_by_name(sheet_name)  # 获取特定的 worksheet
            url_list = []
            # 获取表格所有行和列，两者都是可迭代的
            rows = ws.rows
            columns = ws.columns
            for idx, row in enumerate(rows):
                if idx == 0:
                    continue
                # print type(row)
                # print '[+] git clone', row[1].value
                if row[1].value is None:
                    continue
                if 'http' not in row[1].value:
                    continue
                url_list.append(row[1].value)

            urls_list.append(url_list)

        return urls_list


class NTPathDirector(object):
    def __init__(self):
        pass

    def absolute_dir(self):
        path = os.getcwd()  # 文件夹目录
        files = os.listdir(path)  # 得到文件夹下的所有文件名称
        directories = []
        for file in files:  # 遍历文件夹
            # print os.path.join(os.getcwd(), file)
            abs_path = os.path.join(os.getcwd(), file)
            directories.append(abs_path)
        return directories


# 备份仓库
def repo_backup():
    urls_list = backup_reader.get_urls_list()
    sheets = backup_reader.get_sheet_names()
    for idx, urls in enumerate(urls_list):
        print u'[*] 正在处理 sheet', sheets[idx]
        for url in urls:
            print '[+] git clone', url
            subprocess.call(["git", "clone", url])


# 更新仓库
def repo_update():
    director = NTPathDirector()
    dirs = director.absolute_dir()
    for dir in dirs:
        os.chdir(dir)
        print '[*] Change Working Path:', dir
        subprocess.call(['git', 'pull'])


# update (git pull)
# backup (git clone)
if __name__ == '__main__':
    arguments = docopt(__doc__, version='[v] Github Repos Auto Backup v0.12')
    # print arguments

    if arguments['<source>'] is not None:
        backup_list_path = arguments['<source>']
    else:
        backup_list_path = os.path.join(os.getcwd(), 'backup_list.xlsx')

    if arguments['--xlsx'] is not None:
        dest_path = arguments['--xlsx']
    else:
        dest_path = 'D:\github_backup'

    backup_reader = BackupExcelReader(path=backup_list_path)

    print u'[*] 备份清单路径:', backup_list_path
    print u'[*] 备份目标路径:', dest_path

    os.chdir(dest_path)

    if arguments['update']:
        print '[*] Starting Update ...'
        repo_update()

    if arguments['backup']:
        print '[*] Starting Backup ...'
        repo_backup()
