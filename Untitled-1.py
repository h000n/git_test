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
s = [1,33,13,3,2,3,5,24,1]
n = len(s)
so = Insertion(s,n)
print(so)