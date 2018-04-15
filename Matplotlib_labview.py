"""
時間が","、電圧が"\n"で区切られているため、これを利用し時間用のリストtime、電圧用のリストvolにそれぞれの値を代入.
その後matplotlibを利用し折れ線グラフを作成する。どこが最大値かわかりやすくするため同時に点も表示する.
"""

import numpy as np
import matplotlib.pyplot as plt 
import sys

#データ名を引数に取り、各datafileを読み込む.
dataname = sys.argv
file = '../labview.lvm/' + dataname[1]
with open(file,'r') as f:
    #現状数字扱いなのであとでfloat()を使い修正する.
    datas = f.read()

"""
time     : 測定開始時からの時間のリスト
vol      : timeに対応した電圧のリスト 
count    : 現在のtimeを確認するための変数
i,k      : カウンター
baf_time :一時的に(string)時間をおくため
baf_vol  :一時的に(string)電圧をおくため
line_x   : 直線グラフのx軸
key_time :最大電圧時の時間
key_vol  :最大電圧 
"""
flag = 0
time = [0]
vol = []
i = k = 0
count = 0
key = 18.0
baf_time = None
baf_vol = None
#18秒になるまでdataを取得.pythonにdo-whileがないのでkeyを使って代用
while time[count] != key:
    if(flag == 0):
        del time[0]
    baf_time = "0"
    baf_vol = "0"
    while datas[i] != ",":
        baf_time = baf_time + datas[i]
        i += 1
    time.append(float(baf_time))
    i += 1
    while datas[i] != "\n":
        baf_vol = baf_vol + datas[i]
        i += 1
    vol.append(float(baf_vol))
    i += 1
    #time[]とvol[]の現在扱っているインデックスとcountの数値を一緒にしたいため以下コードを記述
    if(flag==0):
        flag += 1
    else:
        count += 1

key_vol = max(vol)

while 1:
    if vol[k] == key_vol:
        line_x = k
        break
    k += 1

print("最大電圧: " + str(vol[k]) + " V\n" + "計測開始からの時間: " + str(time[k]) + "秒\n")
left = np.array(time)
height = np.array(vol)
p = plt.plot(time[k],vol[k],'o',color = "red")
p = plt.plot(left,height,linewidth = 1,color="black")
plt.show(p)