import os
 
def changeName(path):
    i = 1
    for filename in os.listdir(path):
       # print(path+filename, '=>', path+str(cName)+str(i)+'.jpg')
        os.rename(path+filename, path+filename+'.png')
        i += 1
 
changeName('/Users/hoon/Desktop/testFolder/')
print("end")
