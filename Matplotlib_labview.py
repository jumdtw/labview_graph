#!python3
"""
時間が","、電圧が"\n"で区切られているため、これを利用し時間用のリストtime、電圧用のリストvolにそれぞれの値を代入.
その後matplotlibを利用し折れ線グラフを作成する。どこが最大値かわかりやすくするため同時に点も表示する.
"""
def main():
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
    max_vol  :最大電圧 
    key_vol  :電圧のflag
    top_list :
    """
    flag = 0
    time = [0]
    vol = []
    i = k = v =0
    count = 0
    key = 18.0
    baf_time = None
    baf_vol = None
    key_vol = 0
    print("波形番号    "+"時刻(秒)    "+"電圧(V)")
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
        #山の頂点に点を打つ。
        if(key_vol<=vol[len(vol)-1]):
            key_vol = vol[len(vol)-1]
        elif(vol[len(vol)-2]>=3.5):
            key_vol = 0
            v += 1
            print(str(v) +"    "+str(time[len(time)-2])+"    "+str(vol[len(vol)-2]))
            p = plt.plot(time[len(time)-2],vol[len(vol)-2],'o',color = "blue")
        #time[]とvol[]の現在扱っているインデックスとcountの数値を一緒にしたいため以下コードを記述
        if(flag==0):
            flag += 1
        else:
            count += 1

    max_vol = max(vol)

    while 1:
        if vol[k] == max_vol:
            line_x = k
            break
        k += 1


    print("\n\n")
    print("最大電圧: " + str(vol[k]) + " V\n" + "計測開始からの時間: " + str(time[k]) + "秒\n")
    left = np.array(time)
    height = np.array(vol)
    p = plt.xlabel("(S)")
    p = plt.ylabel("(V)")
    p = plt.title("Labview")
    p = plt.plot(time[k],vol[k],'o',color = "red")
    p = plt.plot(left,height,linewidth = 1,color="black")
    plt.show(p)

if __name__ == '__main__':
    main()