#计算0-100之和
# a = 0
# sum = 0
# while a <= 100:
#     sum += a
#     a += 1
# print(sum)

# a = 0
# for i in range(0,101) :
#     a += i
# print(a)


#计算100以内偶数之和
# a = 0
# sum = 0
# while a <= 100 :
#     if a % 2 == 0 :
#         sum += a
#     a += 1
# print(sum)

# sum = 0
# for i in range(0,101):
#     if i % 2 == 0 :
#         sum += i
# print(sum)


#找出100-999所有的水仙花数
# a = 100
# while a <= 999 :
#     b = a // 100
#     c = (a - b * 100) // 10
#     d = a - b * 100 - c * 10
#     if b ** 3 + c ** 3 + d ** 3 == a :
#         print(a,end="\t")
#     a += 1

# for a in range(100,1000) :
#     b = a // 100
#     c = (a - b * 100) // 10
#     d = a - b * 100 - c * 10
#     if b ** 3 + c ** 3 + d ** 3 == a :
#         print(a,end="\t")


#求出100以内质数之和
# a = 2
# sum = 0
# while a <= 100 :
#     b = 2
#     while b < a :
#         if a % b == 0 :
#             break
#         b += 1
#     else :
#         sum += a
#     a += 1
# print(sum)

# i = 0
# for a in range(2,101) :
#     for b in range(2,a) :
#         if a % b == 0 :
#             break
#     else :
#         i += a
# print(i)


#打印出100以内的所有偶数
# a = 0
# while a <= 100 :
#     if a % 2 > 0 :
#         continue
#     else :
#         print(a)
#     a += 2

# for a in range(0,101) :
#     if a % 2 > 0 :
#         continue
#     else :
#         print(a)

#计算出100以内偶数和奇数之差
# a = 0
# sum = 0
# i = 0
# while a <= 100:
#     if a % 2 == 0 :
#         sum += a
#     else:
#         i += a
#     a += 1
# print(sum - i)

# sum = 0
# a = 0
# for i in range(1,101):
#     if i % 2 == 0 :
#         sum += i
#     else:
#         a += i
# print(sum - a)
#定义一门学科的成绩，90-100为优秀，70-90为良好，60-70为及格，0-60为不及格
# while True:
#     a = int(input("请输入成绩："))
#     if a >= 90 and a <= 100 :
#         print("优秀")
#     elif a >= 70 and a < 90:
#         print("良好")
#     elif a >= 60 and a < 70 :
#         print("及格")
#     elif a >= 0 and a < 60:
#         print("不及格")


#九九乘法表
# a = 1
# while a <= 9 :
#     b = 1
#     while b <= a :
#         print("%d*%d=%d" % (b,a,a*b),end="\t")
#         b += 1
#     print("")
#     a += 1

# for a in range(1,10):
#     for i in range(1,a+1):
#         print("%d*%d=%d" % (a,i,a*i),end="\t")
#     print("")

#输入一个整数，如果它既能被2整除，又能被3整除，那么打印(helloworld)；如果只能被2整除，打印（hello），如果只能被3整除，打印（world）；既不能被2整除又不能被3整除，打印（123）
# while True :
#     a = int(input("请输入一个整数："))
#     if a % 2 == 0 :
#         if a % 3 == 0 :
#             print("hello world")
#         else :
#             print("hello")
#     elif a % 3 == 0:
#         print("world")
#     else :
#         print("123")
#写出1，2,3,4所能组成的所有三位数，且不能重复，一个三位数之间也不能有重复的数字
# for a in range(1,5):
#     for b in range(1,5) :
#         for c in range(1,5) :
#             if (a != b) and (b != c) and (a != c) :
#                  print("%d%d%d" % (a,b,c))

# a = 1
# while a <= 4 :
#     b = 1
#     while b <= 4 :
#         c = 1
#         while c <= 4 :
#             if (a != b) and (b != c) and (a != c) :
#                 print("%d%d%d" % (a,b,c))
#             c += 1
#         b += 1
#     a += 1

