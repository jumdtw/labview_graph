import sys

#データ名を引数に取り、各datafileを読み込む。
data = sys.argv
file = '../labview.lvm/' + data[1]
with open(file,'r') as f:
    datas = f.read()
'''
time = []
vol = []
i = 0
while i == 20 :
'''
print(datas[1])