# github 项目自动备份脚本

## 关于背景

考虑到最近p神的github被封的事件，感觉有必要对某些github仓库进行备份，所以就随手写了这个脚本。

1. 使用 Excel 管理需要备份的github项目
2. 使用 sheet 来对不对类别的项目分类。

## 其他用途

帮助回忆 openpyxl 和 docopt 的用法。

## docopt

PyCon UK 2012: Create \*beautiful\* command-line interfaces with Python

https://www.youtube.com/watch?v=pXhcPJK5cMc&feature=youtu.be

## 使用方法


```
# Usage:
python auto_backup.py backup <source> [--xlsx=<destination>]
python auto_backup.py update [--xlsx=<destination>]
python auto_backup.py (-h | --help)
python auto_backup.py --version
  
# Demo
python auto_backup.py backup backup_list.xlsx --xlsx=D:\github_backup
python auto_backup.py update --xlsx=D:\github_backup

```