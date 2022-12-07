import csv
import numpy

list_data = []
with open('dataset.csv',newline='') as t:
    reader = csv.reader(t)
    for row in reader:
        list_data.append(row)

p1 = list_data[0:50]
p2 = list_data[50:100]
p3 = list_data[100:150]

train_p1 = p1[0:25]
for row in train_p1:
    row[0] = float(row[0])
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = 1

test_p1 = p1[25:50]
for row in test_p1:
    row[0] = float(row[0])
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = 1

train_p2 = p2[0:25]
for row in train_p2:
    row[0] = float(row[0])
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = -1

test_p2 = p2[25:50]
for row in test_p2:
    row[0] = float(row[0])
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = -1

train_data = train_p1 + train_p2
test_data = test_p1 + test_p2
w = [1,0,0,0,0]

while(1):
    count = 0
    for i in range(0,50):
        x = [[1],[train_data[i][0]],[train_data[i][1]],[train_data[i][2]],
             [train_data[i][3]]]
        margin = sum(train_data[i][4]*numpy.dot(w,x))
        if(margin>0):
            count += 1
        if(margin<0):
            d= [0.1*x[0][0]*train_data[i][4],0.1*x[1][0]*train_data[i][4],
                     0.1*x[2][0]*train_data[i][4],0.1*x[3][0]*train_data[i][4],
                     0.1*x[4][0]*train_data[i][4]]
            w = numpy.add(w, d)
    if(count == 50):
        break
print(w)
for i in range(0,50):
    val = [test_data[i][0]*w[1],test_data[i][1]*w[2],
           test_data[i][2]*w[3],test_data[i][2]*w[4],w[0]]
    print(val)
    val = sum(val)

    if(val>=0):
        print("Iris Setosa")
    if(val<0):
        print("Iris Versicolor")
