# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:37:37 2022

@author: ' + syaban + '
"""
import glob
import matplotlib.pyplot as plt
import pandas as pd

inputdata = pd.read_csv (r'１①入力.csv',encoding = 'shift-jis')
Year = str(int(inputdata.iat[1,1]))
Month = str(int(inputdata.iat[2,1]))
if len(Month) < 2 :
    Month = '0' + str(Month)
else :Month = str(Month)



fin = pd.DataFrame()

#31日まで回す
for i in range(32):
    if i <10 : 
        Date = Year + Month + '0' + str(i)
    else :
        Date = Year + Month + str(i)
        #ない日を飛ばす
    try:
        #ログのデータを読み込んで、合わせる
        log_data2 = pd.read_csv (r'VPN管理コンソールにて取得したアクティビティログ\\'+ Year + '_' + Month + '\\' + 'nmact_' + Date + '(1).log')
        log_data1 = pd.read_csv (r'VPN管理コンソールにて取得したアクティビティログ\\' + Year + '_' + Month + '\\' + 'nmact_' + Date + '.log')
        log_data_ = pd.concat([log_data1, log_data2])
        log_data = log_data_[['Date','Event','User Name']]
        log_data['User Name'] = log_data['User Name'].str.extract('([0-9]{6})')
        
        #COnnect Romaming Reachableを抽出する
        dfReachable = log_data[log_data.Event == "Reachable"]
        dfConnect = log_data[log_data.Event == "Connect"]
        dfRoaming = log_data[log_data.Event == "Roaming"]
        
        #ここでログデータの使った人の数を出す
        df_drop = log_data.drop_duplicates(subset = "User Name")
        
        #ここでconnect roaming reachableの人数を出す
        df_dropcon = dfConnect.drop_duplicates(subset = "User Name")
        df_droproa = dfRoaming.drop_duplicates(subset = "User Name")
        df_droprea = dfReachable.drop_duplicates(subset = "User Name")
        
        #ここで各人数を抽出
        len_connect =len(df_dropcon) 
        len_roaming = len(df_droproa)
        len_reach = len(df_droprea)
        len_df = len(df_drop)
        #これが求めたいもの
        df = pd.DataFrame([[log_data.iat[0,0],len_df,len_reach, len_connect, len_roaming]],
            columns =("データ日時", "利用者合計（重複なし）","Reachable", "Connect", "Roaming" 
            ))
        
        fin = pd.concat([fin,df])
    except Exception as e:
        print()
    #ここでCSVにセーブする
fin.to_csv (Year + '_' + Month + 'Excel' + '.csv',encoding = 'shift-jis' , index=None)


x = fin["データ日時"]
height = fin["利用者合計（重複なし）"]
labels = fin["データ日時"].str[-2:]
plt.bar(x, height, tick_label = labels, width=0.5)
plt.savefig(Year + '_' + Month + 'Graph' +'.jpg')
#read_text_file.to_csv (r"C:\\Users\\' + syaban + '\\Desktop\\abc.csv", index=None)
