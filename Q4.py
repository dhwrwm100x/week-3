import numpy as np
b=np.array([1,2,3,4,5,6,7])
total=0
for i in range(len(b)):
    sq=b[i]*b[i]
    total+=sq
    print(total)
