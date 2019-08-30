# -*- coding: utf-8 -*-
"""Python0826.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vOqU2GlizCDnzXHl9brYJAvBTrFw4tUS

## **301**
"""

import pandas as pd

datas= [[75, 62, 85, 73, 60], [91, 53, 56, 63, 65],
         [71, 88, 51, 69, 87], [69, 53, 87, 74, 70]]
indexs= ["小林", "小黃", "小陳", "小美"]
columns= ["國語", "數學", "英文", "自然", "社會"]

df= pd.DataFrame(datas, index= indexs, columns= columns)

print("行標題為科目，列題標為個人的所有學生成績")
print(df)

print("\n後二位的成績")
print(df[2:4])

print("\n以自然遞減排序")
print(df.sort_values(by="自然", ascending=False)["自然"])

df.loc["小黃"]["英文"]= 80
print("\n小黃的成績")
print(df.iloc[1])

"""## **302**"""

import numpy as np

num= np.random.randint(5, 15, 15)
x= num.reshape(3,5)

print("隨機正整數：",num)
print("X矩陣內容：")
print(x)

print("最大：",np.max(x))
print("最小：",np.min(x))
print("總和：",np.sum(x))
print("四個角落元素：")
print(x[np.ix_([0, -1],[0, -1])])

"""## **303**"""

import pandas as pd

price = [[9, 203674, 13.2, 18894],
         [11.7, 180785, 12.3, 54894],
         [10.1, 127802, 14.7, 18563],
         [11.8, 28604, 14.9, 21963],
         [13.2, 600, 13.1, 900],
         [6.9, 38071, 9.6, 3555],
         [12.1, 35660, 10.6, 9005],
         [12, 15000, 13, 12000],
         [11.7, 48770, 9.1, 14370],
         [9.84, 6100, 11.89, 8980]]
sec = ["三重市", "台中市", "台北一", "台北二", "台東市", "板橋區", "高雄市", "嘉義市", "鳳山區", "豐原區"]
item = ["西瓜價", "西瓜量", "香瓜價", "香瓜量"]

df= pd.DataFrame(price, index= sec, columns= item)
print("西瓜與香瓜之拍賣行情價量表")
print(df)

print("\n以西瓜價遞減排序")
print(df.sort_values(by= "西瓜價", ascending= False)["西瓜價"])

print("\n台北一市場的行情")
print(df.loc["台北一"])

print("\n全體市場行情")
print(df.rename(index={"三重市":"三重區"}, columns= {"香瓜價": "洋香瓜價", "香瓜量": "洋香瓜量"}))

"""## **305**"""

import pandas as pd

df= pd.read_csv("read.csv")
print(df.groupby(by="居住縣市")["確定病例數"].sum().sort_values(ascending=False))
print(df.groupby(by="感染國家")["確定病例數"].sum().sort_values(ascending=False).head())
print(df[df.居住縣市=="台北市"].groupby(by="居住鄉鎮")["確定病例數"].sum())
print("發病日:",max(df[df.居住縣市=="台北市"]["發病日"]))