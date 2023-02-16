import numpy as np
import time 
def Insertion(s,n):
    j = n
    while j>=1:
        k=n-j
        val = s[n-j]
        for i in range(n-j,n):
            if s[i]<val:
                val = s[i]
                k=i
        s[k]=s[n-j]
        s[n-j]=val
        j-=1
    return s
s = list(np.array(range(1, 100000, 1)))
s.reverse()
n = len(s)
time_now = time.time()
so = Insertion(s,n)
time_end = time.time()
print(time_end-time_now)