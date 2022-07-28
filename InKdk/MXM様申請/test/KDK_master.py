import win32com.client
import datetime
import openpyxl
import os


def get_workbook(workbook_name):
    try:
        if workbook_name == r"C:\Users\406429\Documents\GitHub\Python\InKdk\MXM様申請\test\KDK_master.py":
            pass
        workbook = xl.Workbooks.Open(r"C:\Users\406429\Documents\GitHub\Python\InKdk\MXM様申請\test\\" + workbook_name)
        return workbook
    except:
        print(f"{workbook_name}名を確認してください")
def get_worksheet(workbook_name):
    try:
        pass
    except:
        pass


# リストを作る日にちを手に入れる
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
date = now.strftime("%Y")
m_d = str(now.strftime("%m/%d"))

xl = win32com.client.Dispatch("Excel.Application")
path_lists = os.listdir(os.path.dirname(__file__))



print(path_lists)
for i in range(len(path_lists)):
    workbook.append(get_workbook(path_lists[i]))
    print(workbook[i])
