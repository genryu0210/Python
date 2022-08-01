import datetime
import openpyxl
import os
import tqdm
import pandas as pd


def get_workbook(workbook_name):
    try:
        if workbook_name == "KDK_master.py":
            pass
        workbook = openpyxl.load_workbook(workbook_name, data_only=True)

        print(f"{workbook_name}を読み込みました。")
        return workbook
    except:
        print(f"{workbook_name}名を確認してください")


# リストを作る日にちを手に入れる
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
date = now.strftime("%Y")
m_d = str(now.strftime("%m/%d"))

path_lists = os.listdir(os.path.dirname(__file__))
workbooks, df = [], []
print(path_lists)
sheet_name = ["Access取込用に加工", "M_推進者", "Sheet1", "回線番号情報", "Sheet1"]
for i in range(5):
    workbooks.append(get_workbook(path_lists[i]))
    df.append(pd.read_excel(path_lists[i], sheet_name=sheet_name[i], engine="openpyxl"))


fromsb = workbooks[0]
m_suishin = workbooks[1]
mailaddress_list = workbooks[2]
phonenum_list = workbooks[3]
target = workbooks[4]
fromsb_sheet = fromsb["Access取込用に加工"]
m_suishin_sheet = m_suishin["M_推進者"]
mailaddress_list_sheet = mailaddress_list["Sheet1"]
phonenum_list_sheet = phonenum_list["回線番号情報"]
ws = target["Sheet1"]
ws.cell(row=1, column=3, value="回線番号")
ws.cell(row=1, column=4, value="機種名")
ws.cell(row=1, column=5, value="レンタル契約終了日")
for i in tqdm.tqdm(range(1, 8136)):
    ws.cell(row=i, column=1, value=mailaddress_list_sheet.cell(row=i, column=3).value)
    ws.cell(row=i, column=2, value=mailaddress_list_sheet.cell(row=i, column=2).value)
    ws.cell(row=i, column=6, value=mailaddress_list_sheet.cell(row=i, column=22).value)
    ws.cell(row=i, column=7, value=mailaddress_list_sheet.cell(row=i, column=34).value)
    ws.cell(row=i, column=8, value=mailaddress_list_sheet.cell(row=i, column=23).value)
    for j in range(4, 432):
        if ws.cell(row=i, column=6).value == m_suishin_sheet.cell(row=j, column=2).value:
            ws.cell(row=i, column=9, value=m_suishin_sheet.cell(row=j, column=9).value)
            ws.cell(row=i, column=10, value=m_suishin_sheet.cell(row=j, column=8).value)
            ws.cell(row=i, column=11, value=m_suishin_sheet.cell(row=j, column=11).value)
            ws.cell(row=i, column=12, value=m_suishin_sheet.cell(row=j, column=10).value)
            break
    flag = 0
    for j in range(2, 9135):
        # if ws.cell(row=i, column=2).value == phonenum_list_sheet.cell(row=j, column=9).value:
        #     ws.cell(row=i, column=3, value=phonenum_list_sheet.cell(row=j, column=2).value)
        #     ws.cell(row=i, column=4, value=phonenum_list_sheet.cell(row=j, column=14).value)
        #     flag += 1
        #     break
        if ws.cell(row=i, column=3).value == fromsb_sheet.cell(row=j, column=3).value:
            ws.cell(row=i, column=5, value=fromsb_sheet.cell(row=j, column=13).value)
            flag += 1
            break
        # if flag >2:
        #     break

target.save("created.xlsx")
target.close()
print("おわり")
