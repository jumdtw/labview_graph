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
i        : カウンター
baf_time :一時的に(string)時間をおくため
baf_vol  :一時的に(string)電圧をおくため
"""
flag = 0
time = [0]
vol = []
i = 0
count = 0
key = 18.0
baf_time = None
baf_vol = None
#18秒になるまでdataを取得.pythonにdo-whileがないのでkeyを使って代用
while time[count] == key:
    if(flag == 0):
        del time[0]
    while datas[i] != ",":
        baf_time = baf_time + datas[i]
        i += 1
    time.append(float(baf_time))
    i += 1
    while datas[i] != "/n":
        baf_vol = baf_vol * datas[i]
        i += 1
    vol.append(float(baf_vol))
    i += 1
    #time[]とvol[]の現在扱っているインデックスとcountの数値を一緒にしたいため以下コードを記述
    if(flag==0):
        flag += 1
    else:
        count += 1

