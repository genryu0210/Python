import pandas as pd
import os

path_lists = os.listdir(os.path.dirname(__file__))
print(path_lists)
database = pd.read_excel("created.xlsx", sheet_name=0, index_col=None, na_values=0, dtype=object)
database = database.fillna(0)
columns = ["PhoneNumber", "Count", "氏名（漢字）", "社員番号", "機種名", "所属組織コード", "本支店名", "所属組織名称"]
phone_numbers_df = pd.DataFrame(columns=columns, data=[[0, 0, 0, 0, 0, 0, 0, 0]])
for path in path_lists:
    if path == "created.xlsx" or path == "main.py" or path == "test.csv" or path == "clastaring.py":
        pass
    else:
        df = pd.read_excel(path, sheet_name=1, index_col=0)
        df = df[df["オーダー種別"] == "パスワードリセット・変更"]
        phone_numbers = pd.Series(df["利用対象の携帯電話"], copy=True)
        for i in range(phone_numbers.count()):
            phone_number = phone_numbers.iloc[i]
            phone_number = str(phone_number[0:3] + phone_number[4:8] + phone_number[-4:])
            phone_number_df = pd.DataFrame(data=[[phone_number, 0, 0, 0, 0, 0, 0, 0]], columns=columns)
            phone_numbers_df = pd.concat([phone_numbers_df, phone_number_df], ignore_index=True)

counted_num_list = phone_numbers_df.drop(columns=["Count"])
for i in range(len(counted_num_list)):
    for j in range(len(database)):
        if counted_num_list["PhoneNumber"][i] == database["回線番号"][j]:
            for column in columns:
                if column == "PhoneNumber" or column == "Count":
                    continue
                counted_num_list[column][i] = database[column][j]

try:
    count1 = 0
    count2 = 0

    for row in range(len(counted_num_list)):
        if counted_num_list.iloc[row-count1, 1] == 0:
            counted_num_list = counted_num_list.drop(row)
            count1 +=1

    for row in range(len(counted_num_list)):
        if counted_num_list.iloc[row-count2, 0] == 0 or counted_num_list.iloc[row-count2, 0] == "--":
            counted_num_list = counted_num_list.drop(row)
            count2 += 1

except IndexError:
    pass

print("fin")
counted_num_list.to_csv("test.csv", encoding='utf_8_sig')
