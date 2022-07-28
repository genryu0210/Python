import csv

with open("ranking.csv", "w", newline="") as f:
    fieldnames = ["Name", "Count"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    name = input("こんにちは！私はRobokoです。あなたの名前は何ですか？")
    name = name.capitalize()
    favorite_restaurant = input("{}さん。どこのレストランが好きですか？".format(name))
    favorite_restaurant = favorite_restaurant.capitalize()
    writer.writerow({"Name": favorite_restaurant, "Count": 1})
    print("{}さん。ありがとうございました。\n良い一日を！さようなら。".format(name))
