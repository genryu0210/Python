import pandas
import pandas as pd
from sklearn.cluster import KMeans
from tqdm import tqdm
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, "JST")
now = datetime.datetime.now(JST)
date = now.strftime(("%Y%m%d"))
database = pd.read_excel("created.xlsx", dtype=object, index_col=None)
mail_adress_list = pd.read_excel("3_メールアドレスリスト_2022.06(6月在籍者).xlsx", dtype=object, index_col=None)
df = pd.read_csv("test.csv", index_col=None, dtype=object)
columns = df.columns
columns = columns.drop(columns[7])
columns = columns.drop(columns[5])
columns = columns.drop(columns[4])
columns = columns.drop(columns[0])
columns = columns.drop(columns[0])
df = df[columns]
df["生年月日"] = 0
df["性別"] = 0
df = df.sort_values("社員番号")
mail_adress_list = mail_adress_list.sort_values("社員番号")
for i in tqdm(range(len(df))):
    for j in range(len(mail_adress_list)):
        if df.iloc[i, 1] == mail_adress_list.iloc[j, 1]:
            df.iloc[i, 3] = mail_adress_list.iloc[j, 7]
            df.iloc[i, 4] = mail_adress_list.iloc[j, 8]
            break
count_branch = pd.DataFrame(columns=[["総数", "リセットした人", "割合"]])
count_branch["リセットした人"] = df["本支店名"].value_counts()
count_branch["総数"] = database["本支店名"].value_counts()
count_ratio = []
for i in range(len(count_branch)):
    count_ratio.append(count_branch.iloc[i, 0] / count_branch.iloc[i, 1])
count_branch["割合"] = count_ratio
df["割合"] = 0
for i in range(len(df)):
    for j in range(len(count_branch.index)):
        if df.iloc[i, 2] == count_branch.index[j]:
            df.iloc[i, 5] = count_branch.iloc[j, 2]
taiou = pd.DataFrame(data=df[["本支店名", "割合"]]).drop_duplicates()
df = df.drop(["氏名（漢字）"], axis=1)
df = df.drop(["社員番号"], axis=1)
df = df.drop(["本支店名"], axis=1)
df["年齢"] = 0
for age in df["生年月日"]:
    num = df[df["生年月日"] == age]["生年月日"].index
    df["年齢"][num] = int(int(int(date) - int(pd.to_datetime(age).strftime("%Y%m%d"))) / 10000)
drop0 = df[df["年齢"]>0]
mean = drop0.mean()
mean = mean.iloc[[2, 0]]
df_sc = pd.get_dummies(df, drop_first=True)

model = KMeans(n_clusters=4, random_state=1)
model.fit(df_sc)

cluster = model.labels_
df[cluster] = cluster

from sklearn.decomposition import PCA
pca = PCA(n_components=2, random_state=1)
pca.fit(df_sc)
feature = pca.transform(df_sc)
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 6))
plt.scatter(feature[:, 0], feature[:, 1], alpha=0.8, c=cluster)
plt.xlabel('principal component 1')
plt.ylabel('principal component 2')
plt.show()
