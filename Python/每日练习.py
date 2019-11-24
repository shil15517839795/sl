#!/usr/bin/python
# -*-coding:utf-8-*-
# li = [1,2,3,4,5,6,7,8,8]能组成多少个互不相同且不重复的数字的两位数
# a = [1,2,3,4,5,6,7,8,8]
# b = []
# c = []
# for i in a:
#     for j in a:
#         if i != j:
#             h = ("%d%d" % (i,j))
#             b.append(h)
# for e in b:
#     if e not in c:
#         c.append(e)
# print(c)
#公鸡5文钱一只，母鸡3文钱一只，小鸡两只一文钱，用100文钱买100只鸡,其中 公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱？
# for a in range (1,100 // 5):
#     for b in range(1,100 // 3):
#         for c in range(1,100 *2):
#             if a + b + c == 100 and a*5 + b*3 + c/2 == 100:
#                 print(a,b,c)


# 将二进制数转换成十进制数
# a=input('输入二进制：')
# b=a[::-1]
# i=0
# for k in range(len(a)):
#     c=int(b[k])*(2**k)
#     i+=c
# print(i)

#19.	用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只，要求三只鸡都要买。
# for a in range(1,100 // 2):
#     for b in range(1,100 // 1):
#         for c in range(1,100 * 2):
#             if a+b+c==100 and a*2 + b*1 + c / 2==100:
#                 print(a,b,c)

# m = int(input("输入总钱数："))
# k = int(input("输入花多少钱可以加一元："))
# i = 0
# j = 0
# while 0 < m:
#     m-=1
#     i+=1
#     j+=1
#     if i % k == 0:
#         m+=1
# print(j)


#100以内质数之和
# a = 0
# for i in range(2,101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         a += i
# print(a)


#九九乘法表
# for i in range(1,10):
#     j = 1
#     for j in range(1,i+1):
#         print("%d*%d=%d" %(j,i,i*j),end="\t")
#     print("")


#计算10以内的数的阶乘
# a = 1
# for i in range(1,11):
#     a *= i
# print(a)


# def aaa():
#     a = 1
#     # print(a)
#     def eee(x):
#         aa = 2
#         print(x)
#         def ccc():
#             bb = 3
#             print(5)
#         return ccc
#     eee(3)()
#     return eee
# print(aaa()(4)())

#判断三角形(判断是否为钝角、直角或锐角三角形)
# while True:
#     a = int(input("输入边长："))
#     b = int(input("输入边长："))
#     c = int(input("输入边长："))
#     d = []
#     if a+b>c and a+c>b and b+c>a:
#         print("图形是三角形")
#         d.append(a)
#         d.append(b)
#         d.append(c)
#         d.sort()
#         if d[0]**2+d[1]**2<d[2]**2:
#             print("钝角三角形")
#         elif d[0]**2+d[1]**2>d[2]**2:
#             print("锐角三角形")
#         elif d[0]**2+d[1]**2==d[2]**2:
#             print("直角三角形")
#     else:
#         print("不能构成三角形")

#判断以什么开头，以什么结束
# a = input("输入一个字符串：")
# print(a[0],a[-1])


#去重并排序
# a = [23,21,54,43,98,12,54,23]
# b = list(set(a))
# for i in range(len(b)):
#     for j in range(i+1,len(b)):
#         if b[i] < b[j]:
#             b[i],b[j]=b[j],b[i]
# print(b)
#判断字符串是否回文
# a = input("请输入一个六位字符串：")
# if a[0]==a[-1] and a[1]==a[-2] and a[2]==a[-3]:
#     print("是回文")
# else:
#     print("不是回文")
#排序（选择法和冒泡法）
# a = [12,43,13,11,98,76]
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

#水仙花数，计算100-1000以内的水仙花数
# for i in range(100,1000):
#     a = i // 100
#     b = (i - a*100)//10
#     c = i - a*100-b*10
#     if a**3 + b**3 + c**3 == i:
#         print(i)

#打印列表中所有第一大和第二大的数
# a=[12,2,4,65,89,54,65,89]
# a.sort(reverse=True)
# for i in a :
#     if i<a[0]:
#         b = i
#         break
# for j in a:
#     if j == a[0] or j==b:
#         print(j,end="\t")
#三次猜数字
#不用int将字符串变成整数
#将列表中的元素向左挪一位
#将列表中最大的放在最后一位，最小的放在第一位
#一个有顺序的列表，随机加入一个数，加入的数在正确的位置
#从键盘上输入若干个学生的成绩，统计出平均成绩并输出低于平均分的学生成绩，用输入负数结束输入

#十进制转换成十六进制
# a=int(input("输入一个十六进制数："))
# b = hex(a)
# print(b)

#一个数的因数之和等于它本身（因数不包括它本身）计算500以内的
# for i in range(1,501):
#     a=0
#     for j in range(1,i):
#         if i % j ==0:
#             a+=j
#     if a==i:
#         print(i)


#任意4个数字(1,2,3,4)，组成不相同的三位数
# a = [1,2,3,4]
# for i in a:
#     for j in a:
#         for x in a:
#             if i != j and j != x and x != i:
#                 print("%d%d%d" % (i,j,x),end="\t")



#一个函数，传两个参数a，b  a是数组，b是一个数字，找出a数组中两数之和等于b，打印出来这两个数
# def shi(a=[],b=0):
#     for i in range(len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j]==b:
#                 print(a[i],a[j],end="\t")
# shi([12,3,4,11,10],14)

#青蛙爬井问题
# high = int(input("输入一个整数："))
# up = int(input("白天向上爬的距离："))
# down = int(input("晚上向下滑的距离："))
# day = 0
# while 0 < high:
#     if up >= high:
#         day += 1
#         break
#     else:
#         high -= up
#         high += down
#         day += 1
# print(day)



# people = int(input("输入人数："))
# cost = int(input("输入他们的总花费："))
# for a in range(0,cost//3):
#     for b in range(0,cost//2):
#         for c in range(0,cost):
#             if a+b+c==people and 3*a+2*b+c==cost:
#                 print(a,b,c)
# else:
#     print("No answer")


