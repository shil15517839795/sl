#!/usr/bin/python
# -*-coding:utf-8-*-

# txt = open("b.txt","w",encoding="utf-8")
# for i in range(1,101):
#     for j in range(1,5):
#         txt.write("你好世界\t")
#     txt.write("\n")
# txt.close()


# txt = open("a.txt","r",encoding="utf-8")
# a=txt.read()
# b=[]
# c=""
# for i in a:
#     c+=i
#     if i == "\n":
#         b.append(c)
#         c=""
# print(b)
# txt.close()

# txt = open("a.txt","w",encoding="utf-8")
# for i in range(1,10):
#     for j in range(1,i+1):
#         txt.write(" %d*%d=%d\t"% (i,j,i*j))
#     txt.write("\n")
# txt.close()

# a = open("a.txt","r",encoding="utf-8")
# while True:
#     b = a.readline()
#     print(b)
#     if b =="":
#         break
# a.close()

# a = open("a.txt","r",encoding="utf-8")
# b = a.readlines()
# print(b)
# a.close()

# a = open("a.txt","r",encoding="utf-8")
# b = a.readlines()
# # print(b)
# i = 0
# j = 0
# for c in b:
#     if c.startswith("\n"):
#         i+=1
#     if c.startswith("#"):
#         j+=1
# print(i,j)
# a.close()

#追加权限
# a = open(r"d:\迅雷下载\bc20bab0ee6bdcee0aa8b2c737730d3cf30f4eb89d03.mp3","rb")
# b=a.read()
# a.close()
# print(b)
# c = open("x.mp3","wb")
# c.write(b)
# c.close()

# with open('a.txt','r') as f:
#     print(f.read())



