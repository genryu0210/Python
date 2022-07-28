import win32com.client


xl = win32com.client.Dispatch("Excel.Application")
wb = xl.Workbooks.open(r"C:\Users\406429\KYUDENKO CORPORATION\デジタル新技術開発課 - 11.FXM_Windows導入\Windwsフレックスモビリティ申請集約.xlsx")
ws = wb.Worksheets("Form1")
for i in range(2, 200):
    try:
        print(int(ws.Range(f"A{i}").Value))
        ws.Range(f"E{i}").Value = "松本"
        ws.Range(f"J{i}").Value = "承認"
        ws.Range(f"A{i}").Copy(ws.Range("A2"))
    except :
        continue