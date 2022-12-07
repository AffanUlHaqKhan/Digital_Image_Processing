import csv
import numpy as np
import random
def test_func(input_data,train_data_f,k):
    distances=[]
    counts = []
    for i in range(0,75):
        dist = (((float(input_data[0])-float(train_data[i][0]))**2) + ((float(input_data[1])-float(train_data[i][1]))**2) + ((float(input_data[2])-float(train_data[i][2]))**2) + ((float(input_data[3])-float(train_data[i][3]))**2))**(1/2)
        distances.append([dist,train_data[i][4]])
    distances.sort()
    temp = distances[0:k]
    counts.append(sum(x.count('Iris-setosa') for x in temp))
    counts.append(sum(x.count('Iris-virginica') for x in temp))
    counts.append(sum(x.count('Iris-versicolor') for x in temp))
    ind = counts.index(max(counts))
    if(ind == 0):
        return 'Iris-setosa'
    if(ind == 1):
        return 'Iris-virginica'
    if(ind == 2):
        return 'Iris-versicolor'

my_list=[]
with open('dataset.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        my_list.append(row)
#print(my_list)
setosa=my_list[0:50]
versicolor=my_list[50:100]
virginica=my_list[100:150]

train_data = setosa[0:25]+virginica[0:25]+versicolor[0:25]
test_data = setosa[25:50]+virginica[25:50]+versicolor[25:50]

random.shuffle(train_data)
#print(train_data)
for j in range(1,75):
    count = 0
    for i in range(0,75):
        prediction = test_func(test_data[i],train_data,j)
        if(prediction == test_data[i][4]):
            count += 1
    Accuracy = (count/75)*100
    print(j," Accuracy: ",Accuracy,"%" )



