words=""" enter text_ find same ex. hello hello
"""
word = words.split()
n=0
f=0
print(len(words))
while f<len(word):
    while n<len(word):
        if(word[f]==word[n]and f<n):
            print(word[n],f,n)
            n+=1
        else:
            n+=1
    f+=1
    n=0
