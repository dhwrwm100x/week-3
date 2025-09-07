import numpy as np
import random
count=0
marks=np.zeros((20,5),dtype=float)
marks=np.random.randint(40,101,size=(20,5))
avgt=marks.mean(axis=0)
print ('avg marks of each subject \n')
print(avgt)
print('avg marks of each student \n')
avgs=marks.mean(axis=1)
print(avgs)
for i in range (len(marks)):
    if (avgs[i]<=50):
        count+=1
print('number of stidents with avgs less than 50 ',count)
for i in range(len(marks)):
    print(f"student{i+1}->{marks[i]}")
