# from random import *
# date = randrange(1,46)

# print("da%dda"%date)
# print("dad{0}{1}".format(date,date+1))
# print(date,"da")
# print("da"+str(date))

# print("d\'d\'a")


# list1 = ["a"]
# list2 = [1,2,3]
# list1.extend(list2)

# dic = {3:"a","10":"da"}
# print(dic.get(3, "no"))
# print(3 in dic)
# dic[1]="ad"
# print(dic)
# del dic[1]
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# dic.clear()
# print(dic)

# tuples = ("s","a")
# a, b, c = "a", "b", "c"
# print(a,b,c)

# sets = {1,3,4,3,5,2,3,3}
# print(sets)
# a = {"a","b","c"}
# b = {"c","d","e"}
# print(a&b)
# print(a|b)
# print(a-b)
# a.add("a")
# b.remove("c")

# li = [1,2,3,4,5]
# li = [i+100 for i in li]
# print(li)

# from random import *
# cust = list(range(1,51))
# number=1
# poss = " "
# polist = list()
# for i in cust:
#     times = randrange(5,51)
#     if 5<=times & times<=15:
#         poss = "O"
#         polist.append(i)
#     else:
#         poss = " "
#     print("[{}] {}번쨰 손님 (소요시간 : {}분) ".format(poss,number,times))
#     number+=1
# print(len(polist))

# def fu(a,b=100):
#     print(a+b)
#     c = int(a/b)
#     return a+b ,c
# a=10
# a,c = fu(a,10)
# print(a,c)
# fu(a)
# print("adasdad{}dada"\
#     .format(1))

# def al(name , *alls):
#     print(name)
#     for i in alls:
#         print(i, end="")
# al("name", "a","b","c")

# glo = 10
# def a(b):
#     global glo
#     glo -=b
#     print(glo)
# a(10)

# print("a","b",sep=" vs ")
# import sys
# print("abc", file=sys.stdout)
# print("abc", file=sys.stderr)

# scores ={"sub1":1,"sub2":40}
# for sub,score in scores.items():
#     print(sub.ljust(3),str(score).zfill(3).rjust(3),sep=" :")

# print("a".rjust(10))
# print("{: >10}".format("a"))
# print("{:_<+10}".format(100))
# print("{0:^<+20,}".format(1000000))
# print("{:.2f}".format(3/5))

# files = open("file.txt","w",encoding="utf8")
# print("writing...", file=files)
# files.close()

# files = open("file.txt","a",encoding="utf8")
# files.write("some")
# files.write("thing")
# files.close()

# files = open("file.txt","r",encoding="utf8")
# print(files.read())
# while True:
#     if not files.readline():
#         break
#     print(files.readline())
# lines = files.readlines()
# for i in lines:
#     print(i)
# files.close()

# with open("file.txt","r",encoding="utf8") as files:
#     print(files.read())

# for i in range(1,51):
#     with open("{}주차.txt".format(i),"w",encoding="utf8") as bogo:
#         bogo.write("""-{}주차 주간보고-\n부서: \n이름: \n업무요약: """.format(i))


# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         print(hp,name)

#     def meth(self, ano):
#         # self.ano = ano
#         print(ano)

# class Unit2:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# class pa():
#     def __init__(self,pas):
#         self.pas = pas
#     def fly(self,ano):
#         print("fly",ano)
#     def passs():
#         pass
# class sans(Unit,pa):
#     def __init__(self,name,hp,dam,pas):
#         Unit.__init__(self,name,hp)
#         pa.__init__(self,pas)
#         self.dam = dam
#         print(hp-dam)
#     def meth(self,ano):
#         self.fly(ano)

# ma = Unit("name",100)
# # print(ma.hp)
# # ma.new = True
# # ma.news = 100
# # if ma.new == True:
# #     print("ad")
# # print("{}{}".format(ma.new,ma.news))

# ma.meth(1000)
# # print(ma.ano)

# ma2 = sans("name",10,10,10)
# ma.meth(10)
# ma2.meth(10)

# class MadeError(Exception):
#     def __init__(self,msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg
# try:
#     print(1/2)
#     if 1==2:
#         raise ValueError
#     else:
#         raise MadeError(" r  ")
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print(" ")
# except MadeError as e:
#     print(e)
# except:
#     print("")
# finally:
#     print("alll")


# chi = 10
# wai = 1
# class SoldE(Exception):
#     pass
# while True:
#     try:
#         print(chi)
#         if chi == 0:
#             raise SoldE
#             print("d")
#         o = int(input())
#         if o>10:
#             print(" ")
#             continue
#         if o>chi:
#             print(" a")
#             raise ValueError
#         else:
#             print("o")
#             wai += 1
#             chi -= o
#     except ValueError:
#         print("er")
#     except SoldE:
#         break
###raise Error = inside try: 

# from std_module import *
# func2(2)
# from std_module import func2 as d
# d(2)
# import std_module as m
# m.func2(1)

# import package.rando
# package.rando.rando().ron()
# from package.rando import rando
# rando().ron()
# import inspect
# from package import * #__init__ = []
# rando.rando().ron()
# print(inspect.getfile(rando))

# print(dir(list))
# import os ,time
# if not os.path.exists("folder"):
#     os.makedirs("folder")
# print(time.strftime("%Y-%m"))
