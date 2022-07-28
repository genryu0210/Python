# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:52:06 2022

@author: 406429
"""

import win32com.client
import datetime
# 時間設定
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
date = now.strftime('%Y年%m月%d日')
# outlook開く
outlook = win32com.client.Dispatch("Outlook.Application")

# メール作成
mail = outlook.CreateItem(0)
mail.to = 'mailaddress'
mail.cc = 'CCaddress'
mail.subject = '各種申請_' + str(date) + '分'
mail.bodyFormat = 1
mail.Attachments.Add(r"C:%filepass%" + now.strftime("%Y%m%d") + ".xlsm")
mail.body = '''mail_body'''


mail.display(True)
