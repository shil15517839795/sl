#!/usr/bin/python
# -*-coding:utf-8-*-
# i = 1
# while i <= 5:
#     print("hello world")
#     i+=1


#求（0-100）的和
#方法一：
# a = 0
# for i in range(101):
#     a+=i
# print(a)

#方法二：
# a = 0
# i = 0
# while i <= 100 :
#     a+=i
#     i = i + 1
# print(a)

#求0-100所有的偶数相加
# a = 2
# sum = 0
# while a <= 100 :
#     sum = sum + a
#     a = a + 2
# print(sum)


#10的阶乘
# a = 1
# i = 1
# while i <= 10:
#     a = a * i
#     i = i + 1
# print(a)


#求0到100所有奇数之和
# a = 0
# i = 0
# while i <= 100 :
#     if i % 2 != 0 :
#         a = a + i
#     i = i + 1
# print(a)


# a = 0
# i = 1
# while i <= 10 :
#     a = a + i
#     if i == 5 :
#         i = i + 2
#         continue
#     i = i + 2
# print(a)

#while嵌套九九乘法表
# a = 1
# while a <= 9 :
#     i = 1
#     while i <= a :
#         b = a * i
#         print("%d * %d = %d" % (i,a,b),end = "\t")
#         i = i + 1
#     print("")
#     a = a + 1

#100以内质数之和
# a = 2
# c = 0
# while a <= 100 :
#     b = 2
#     while b < a :
#         if a % b == 0 :
#             break
#         b = b + 1
#     else :
#         c = c + a
#     a = a + 1
# print(c)


#打印出10以内所有的偶数
# i = 1
# while i < 10 :
#     i = i + 1
#     if i % 2 > 0 :
#         continue
#     print(i)