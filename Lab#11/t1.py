import numpy
import csv
import random


list_data = []
with open('dataset.csv',newline='') as t:
    reader = csv.reader(t)
    for row in reader:
        list_data.append(row)
p1 = list_data[0:50]
p2 = list_data[50:100]
p3 = list_data[100:150]

data_train = p1[0:25]+p2[0:25]+p3[0:25]
data_test = p1[25:50]+p2[25:50]+p3[25:50]

random.shuffle(data_train)

for i in range(1,75):
    count = 0
    for j in range(0,75):
        distance = []
        counts = []
        temp1 = ''
        for k in range(0,75):
            dist = (((float(data_test[j][0])-float(data_train[k][0]))**2) +
                    ((float(data_test[j][1])-float(data_train[k][1]))**2) +
                    ((float(data_test[j][2])-float(data_train[k][2]))**2) +
                    ((float(data_test[j][3])-float(data_train[k][3]))**2))**(1/2)
            distance.append([dist,data_train[k][4]])
        distance.sort()
        temp = distance[0:i]
        counts.append(sum(x.count('Iris-setosa') for x in temp))
        counts.append(sum(x.count('Iris-virginica') for x in temp))
        counts.append(sum(x.count('Iris-versicolor') for x in temp))
        ind = counts.index(max(counts))
        if(ind == 0):
            temp1 = 'Iris-setosa'
        if(ind == 1):
            temp1 =  'Iris-virginica'
        if(ind == 2):
            temp1 = 'Iris-versicolor'
            
        prediction = temp1
        if(prediction == data_test[j][4]):
            count += 1
    Accuracy = (count/75)*100
    print(i,"    ",Accuracy,"% accurate" )
