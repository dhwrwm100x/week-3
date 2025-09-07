import numpy as np
def interchange(a):
    a[1],a[-2]=a[-2],a[1]
    print('the req result is ',a)
b=np.array([1,2,3,4,5,6,7])
print ('the array',b)
interchange(b)
