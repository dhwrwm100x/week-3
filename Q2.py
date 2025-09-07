import numpy as np
import random
a=np.random.randint(1,51,size=100)
for i in range(len(a)):
    for j in range(len(a)):
        if (a[i]+a[j]==50):
            print(f"{a[i]}+{a[j]}=50")
