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
mail.to = 'kdk-support@mxmobiling.com'
mail.cc = 'Matsuoka Memi-MXM <matsuoka-m@mxmobiling.com>; Takatsugu Takashi-MXM <takatsugu-t@mxmobiling.com>;\
          スマートデバイス運用ML <smart-device-operation@kyudenko365.onmicrosoft.com>; 牟田 光繁 <t-muta@kyudenko.co.jp>'
mail.subject = '各種申請_' + str(date) + '分'
mail.bodyFormat = 1
mail.Attachments.Add(r"C:\Users\406429\Dropbox (株式会社九電工)\【スマホPJ】展開運用\60_運用\50_申請_通常\01_MX送付分\【九電工様】各種申請書_Ver2.8_" + now.strftime("%Y%m%d") + ".xlsm")
mail.body = '''MXモバイリング
各種申請受付　ご担当者さま

いつもお世話になっております。九電工の松本です。

本日分の申請です。
お忙しいところ恐縮ですが、ご確認お願いいたします。


'''


mail.display(True)
