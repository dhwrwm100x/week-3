import numpy as np
import random
m=np.random.randint(1,10,size=(3,3))
avg=m.mean(axis=0)
print ('avg')
print(avg)
sum=m.sum(axis=0)
print(f"sum \n",sum)
