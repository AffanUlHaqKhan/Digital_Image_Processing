import csv
import numpy as np
def test_func(test_input,w_coff):
    val = [test_input[0]*w_coff[1],test_input[1]*w_coff[2],test_input[2]*w_coff[3],test_input[3]*w_coff[4],w_coff[0]]
    print(val)
    val = sum(val)

    if(val>=0):
        print("Iris Setosa")
    if(val<0):
        print("Iris Versicolor")


my_list=[]
with open('dataset.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        my_list.append(row)
#print(my_list)
setosa=my_list[0:50]
versicolor=my_list[50:100]
#print(setosa)
#print("****************************************************************")
#print(versicolor)
setosa_train = setosa[0:25]
for row in setosa_train:
    row[0] = float(row[0])
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = 1
setosa_test = setosa[25:50]
for row in setosa_test:
    row[0] = float(row[0])
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = 1
#print(setosa_train)
versicolor_train = versicolor[0:25]
for row in versicolor_train:
    row[0] = float(row[0])
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = -1
versicolor_test = versicolor[25:50]
for row in versicolor_test:
    row[0] = float(row[0])
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = -1

#print(versicolor_train)
train_data = setosa_train + versicolor_train
test_data = setosa_test + versicolor_test
#print(test_data)
w = [1,0,0,0,0]

while(1):
    count = 0
    for i in range(0,50):
        x = [[1],[train_data[i][0]],[train_data[i][1]],[train_data[i][2]],[train_data[i][3]]]
        margin = sum(train_data[i][4]*np.dot(w,x))
        if(margin>0):
            count += 1
        if(margin<0):
            delta = [0.1*x[0][0]*train_data[i][4],0.1*x[1][0]*train_data[i][4],0.1*x[2][0]*train_data[i][4],0.1*x[3][0]*train_data[i][4],0.1*x[4][0]*train_data[i][4]]
            w = np.add(w, delta)
    if(count == 50):
        break
print(w)
for i in range(0,50):
    test_func(test_data[i],w)

