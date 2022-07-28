import pandas as pd

fieldnames = ["Name", "Count"]
try:
    df = pd.read_csv("ranking.csv")
except Exception:

name = input("こんにちは！私はRobokoです。あなたの名前は何ですか？")
name = name.capitalize()
favorite_restaurant = input("{}さん。どこのレストランが好きですか？".format(name))
favorite_restaurant = favorite_restaurant.capitalize()
print("{}さん。ありがとうございました。\n良い一日を！さようなら。".format(name))
count = 0

volume = pd.DataFrame(data={"Name": ["{}".format(favorite_restaurant)], "Count": [str(count)]})
df.loc[df["Name"]=="{}".format(favorite_restaurant).format(), "Count"] += 1

df.to_csv("ranking.csv", index=False)
