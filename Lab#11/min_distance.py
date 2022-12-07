import csv
import numpy as np

def test_min(test_input,setosa_m,versicolor_m,virginica_m):
    dist=[]
    dist.append(np.linalg.norm(test_input-setosa_m))
    dist.append(np.linalg.norm(test_input-versicolor_m))
    dist.append(np.linalg.norm(test_input-virginica_m))
    prediction = dist.index(min(dist))
    if(prediction == 0):
        return "Iris Setosa"
    if(prediction == 1):
        return "Iris Versicolor"
    if(prediction == 2):
        return "Iris Virginica"


my_list=[]
with open('dataset.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        my_list.append(row)
#print(my_list)
setosa=my_list[0:50]
versicolor=my_list[50:100]
virginica=my_list[100:150]
#print(setosa)
#print("****************************************************************")
#print(versicolor)
#print("****************************************************************")
#print(virginica)
setosa_train = setosa[0:25]
for row in setosa_train:
    del row[4]
setosa_test = setosa[25:50]
for row in setosa_test:
    del row[4]
#print(setosa_train)
setosa_mean=np.mean(np.array(setosa_train,dtype=np.float64),axis=0)
print(setosa_mean)
versicolor_train = versicolor[0:25]
for row in versicolor_train:
    del row[4]
versicolor_test = versicolor[25:50]
for row in versicolor_test:
    del row[4]
#print(versicolor_train)
versicolor_mean=np.mean(np.array(versicolor_train,dtype=np.float64),axis=0)
print(versicolor_mean)
virginica_train = virginica[0:25]
for row in virginica_train:
    del row[4]
virginica_test = virginica[25:50]
for row in virginica_test:
    del row[4]
#print(virginica_train)
virginica_mean=np.mean(np.array(virginica_train,dtype=np.float64),axis=0)
print(virginica_mean)
count=0
for i in range(0,25):
    pred = test_min(np.array(virginica_test[i],dtype=np.float64),setosa_mean,versicolor_mean,virginica_mean)
    if(pred == "Iris Virginica"):
        count += 1
for i in range(0,25):
    pred = test_min(np.array(setosa_test[i],dtype=np.float64),setosa_mean,versicolor_mean,virginica_mean)
    if(pred == "Iris Setosa"):
        count += 1
for i in range(0,25):
    pred = test_min(np.array(versicolor_test[i],dtype=np.float64),setosa_mean,versicolor_mean,virginica_mean)
    if(pred == "Iris Versicolor"):
        count += 1
Accuracy = (count/75)*100
print(count)
print("Accuracy: ",Accuracy,"%" )
