# This will just make a dataset out of chorales.lisp
from pybrain.datasets import SupervisedDataSet
ds = SupervisedDataSet(10, 10)

f = open('chorales.lisp')
file = f.read()
splitfile = file.split('\n')
for i in splitfile:
    list = []
    for x in i.split("))"):
        for y in x.split(")"):
            list.append(y.split(" ")[-1])
    if list != ['']:
        count = 0
        new_list = []
        while count < len(list):
            new_list.append(list[count:count + 6])
            count += 6
        for i in new_list[:]:
            if len(i) < 6:
                new_list.remove(i)
        for i in new_list:
            i[1] = str(int(i[1]) - 60)
            if i[4] == '12':
                i[4] = '0'
            else:
                i[4] = '1'
        print new_list
        for i in range(len(new_list) - 4):
            ds.addSample((new_list[i][1], new_list[i][2], new_list[i][3], new_list[i][4], new_list[i][5], new_list[i+1][1], new_list[i+1][2], new_list[i+1][3], new_list[i+1][4], new_list[i+1][5]), (new_list[i+2][1], new_list[i+2][2], new_list[i+2][3], new_list[i+2][4], new_list[i+2][5], new_list[i+3][1], new_list[i+3][2], new_list[i+3][3], new_list[i+3][4], new_list[i+3][5]))

# THE DATA IS MODIFIED TO BETTER SUIT THE NETWORK!
# notes in the dataset are just notes from chorales.lisp minus 60
# a timekey of 12 is 0
# a timekey of 16 is 1