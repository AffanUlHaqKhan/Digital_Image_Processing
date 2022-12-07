import csv
import numpy

def dist_min(test_input,mean_setosa,mean_versicolor,mean_virginica):
    distance=[]
    distance.append(numpy.linalg.norm(test_input-mean_setosa))
    distance.append(numpy.linalg.norm(test_input-mean_versicolor))
    distance.append(numpy.linalg.norm(test_input-mean_virginica))
    temp = distance.index(min(distance))
    if(temp == 0):
        return "Iris Setosa"
    if(temp == 1):
        return "Iris Versicolor"
    if(temp == 2):
        return "Iris Virginica"
    
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
    del row[4]
test_p1 = p1[25:50]
for row in test_p1:
    del row[4]
setosa_mean=numpy.mean(numpy.array(train_p1,dtype=numpy.float64),axis=0)
print(setosa_mean)

train_p2 = p2[0:25]
for row in train_p2:
    del row[4]
test_p2 = p2[25:50]
for row in test_p2:
    del row[4]
versicolor_mean=numpy.mean(numpy.array(train_p2,dtype=numpy.float64),axis=0)
print(versicolor_mean)

train_p3 = p3[0:25]
for row in train_p3:
    del row[4]
test_p3 = p3[25:50]
for row in test_p3:
    del row[4]
virginica_mean=numpy.mean(numpy.array(train_p3,dtype=numpy.float64),axis=0)
print(virginica_mean)

count=0
for i in range(0,25):
    temp = dist_min(numpy.array(test_p3[i],dtype=numpy.float64),setosa_mean,versicolor_mean,virginica_mean)
    if(temp == "Iris Virginica"):
        count += 1

for i in range(0,25):
    pred = dist_min(numpy.array(test_p1[i],dtype=numpy.float64),setosa_mean,versicolor_mean,virginica_mean)
    if(pred == "Iris Setosa"):
        count += 1

for i in range(0,25):
    pred = dist_min(numpy.array(test_p2[i],dtype=numpy.float64),setosa_mean,versicolor_mean,virginica_mean)
    if(pred == "Iris Versicolor"):
        count += 1

accuracy = (count/75)*100
print(count)
print("Accuracy: ",accuracy,"%" )
