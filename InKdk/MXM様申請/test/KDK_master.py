import datetime
import openpyxl
import os
import tqdm
import openpyxl.cell._writer


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
workbooks = []
print(path_lists)
for i in range(5):
    workbooks.append(get_workbook(path_lists[i]))

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
for i in tqdm.tqdm(range(1, 8136)):
    ws.cell(row=i, column=1, value=mailaddress_list_sheet.cell(row=i, column=3).value)
    ws.cell(row=i, column=2, value=mailaddress_list_sheet.cell(row=i, column=2).value)
    ws.cell(row=i, column=6, value=mailaddress_list_sheet.cell(row=i, column=22).value)
    ws.cell(row=i, column=7, value=mailaddress_list_sheet.cell(row=i, column=34).value)
    ws.cell(row=i, column=8, value=mailaddress_list_sheet.cell(row=i, column=23).value)
    ws.cell(row=1, column=3, value="回線番号")
    ws.cell(row=1, column=4, value="機種名")
    for j in range(4, 432):
        if ws.cell(row=i, column=6).value == m_suishin_sheet.cell(row=j, column=2).value:
            ws.cell(row=i, column=10, value=m_suishin_sheet.cell(row=j, column=8).value)
            ws.cell(row=i, column=9, value=m_suishin_sheet.cell(row=j, column=9).value)
            ws.cell(row=i, column=11, value=m_suishin_sheet.cell(row=j, column=11).value)
            ws.cell(row=i, column=12, value=m_suishin_sheet.cell(row=j, column=10).value)
    for j in range(2, 7407):
        if ws.cell(row=i, column=2).value == phonenum_list_sheet.cell(row=j, column=18).value:
            ws.cell(row=i, column=3, value=phonenum_list_sheet.cell(row=j, column=2).value)
            ws.cell(row=i, column=4, value=phonenum_list_sheet.cell(row=j, column=14).value)
            continue

target.save("created.xlsx")
target.close()
print("おわり")
