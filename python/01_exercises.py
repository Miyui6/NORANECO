"""
Tips!
この "(ダブルクォーテーション)を3つを上下で囲ったものは
Pythonでは複数行のコメントアウトを記述するときに利用します。
参考 https://uxmilk.jp/8847
"""


"""
お題1: 今日の曜日は？
お題: 今日の曜日を日本語で表示させてください

import datetime
today = datetime.date.today()

today.day
をすると今日の日付が返ってきます。

today.weekday()
をすると曜日の数字が返って来ます。0が月曜日で、6が日曜日帰って来ます。
"""

import datetime 
today = datetime.date.today()
today.day  # これは今日の日付
today.weekday()  # これは曜日の数字を取得

print(today)

print(today.weekday())

w=["月曜日","火曜日","水曜日","木曜日","金曜日","土曜日","日曜日"]
print("今日は"+today.weekday()+"です")

# # print("今日の日付は？"+today.strftime("2021-06-03"))
# # print("今日の曜日は"+today.strftime("木曜日"))

# # ここから下に解答を書く


# # 出力例 今日は水曜日です


# #######################################################
# print("_________________________________")


"""
お題2: 一番大きい数、小さい数字、平均値は？
お題: 配列の中の一番大きい数字、小さい数字、平均値をそれぞれ表示してください。
"""
import statistics
import math

numbers = [73, 24, 64, 10, 56, 89]
print(max(numbers))
print(min(numbers))
mean=statistics.mean(numbers)
print(mean)




"""
出力例
89
10
52.666666666666664
"""

#######################################################



"""
お題3: 連絡先をを表示して
お題: dictに入ったデータを使って連絡先を整形して出力してみましょう。
"""

person = {
    "first_name": "太郎",
    "last_name": "すなば",
    "address": {
        "post_code": '904-0004',
        "prefecture": "沖縄県",
        "city": "沖縄市",
        "street": "中央1丁目14-3"},
    "phone": "080-1234-5678",
}

# print("名前："+last_name+first_name
# "郵便番号："+post_code)

# ここから下に解答を書く


"""
出力例
名前: すなば 太郎
郵便番号: 904-0004
住所: 沖縄県沖縄市中央1丁目14−3
電話番号番号: 080-1234-5678
"""


