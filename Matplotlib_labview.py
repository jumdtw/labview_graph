import sys

data = sys.argv
file = 'labview.lvm/' + data[1]
with open(file,'r') as f:
    datas = f.read()


print(datas)