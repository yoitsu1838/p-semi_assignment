list_num = []
with open("test.txt", "r") as fp:
    list_num = fp.read().split()

list_num = [int(i) for i in list_num]
list_num.sort()

wTmp = ""
for num in list_num:
    wTmp += str(num) + "\n"

with open("data2.txt", "w") as fp:
    print(wTmp, file=fp)
