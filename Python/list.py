# name1 = "时雷"
# b = ["时","雷","哈"]
# # print(type(b))
# # print(b[0])
# # print(len(b))
# a = 0
# while a <= len(b) - 1 :
#     print("恭喜%s顺利毕业" % b[a])
#     a += 1


#for循环求100以内质数和

# c = 0
# for a in range(2,101) :
#     for b in range(2,a) :
#         if a % b == 0 :
#             break
#     else :
#         c = c + a
# print(c)

#求0到100所有数之和
# a = 0
# for i in range(0,101) :
#     a += i
# print(a)

#求100以内偶数之和
# sum = 0
# for a in range(2,101,2) :
#     sum += a
# print(sum)


#求100以内奇数之和
# sum = 0
# for a in range(1,101,2) :
#     sum += a
# print(sum)


#九九乘法表
# for i in range(1,10) :
#     for a in range(1,i+1) :
#         b = a * i
#         print("%d * %d = %d" % (i,a,b),end="\t")
#     print("")


#写出1-4所能组成的所有三位数（不能有重复）
# for a in range(1,5) :
#     for b in range(1,5) :
#         for c in range(1,5) :
#             if (a != b) and (b != c) and (a != c) :
#                 print("%d%d%d" % (a,b,c))

#水仙花数
# for a in range(100,1000,1) :
#     b = a // 100
#     c = (a - b * 100) //  10
#     d = a - b * 100 - c * 10
#     if b ** 3 + c ** 3 + d ** 3 == a :
#         print(a,end = "\t")

#打印出10以内的偶数
# for i in range(1,11) :
#     if i % 2 > 0 :
#         continue
#     print(i,end = "\t")



#排序
# s = [5,3,7,4]
# for a in range(len(s) - 1):
#     for b in range(a+1,len(s)) :
#         if s[a] > s[b] :
#             s[a],s[b] = s[b],s[a]
# print(s)

#求1-2+3-4+5-6+7-8+……+99的值
# s = 0
# c = 0
# for a in range(1,100) :
#     if a % 2 == 0 :
#         s = s + a
#     else :
#         c = c + a
# print(c - s)


# a = 0
# s = 0
# while s <= 100 :
#     if s % 2 == 0 :
#         a = a + s
#     s = s + 1
# print(a)


#奇数偶数之差
# a = 0
# b = 0
# s = 0
# while s <= 100 :
#     if s % 2 == 0 :
#         a = a + s
#     else :
#         b = b +s
#     s += 1
# print(a - b)


# a = ("abc","ABC","abb","cda")
# for i in a :
#     if (i.startswith("a") or i.startswith("A")) and i.endswith("c"):
#          print(i)


# b = [11,22,33,44,55,66,77,88,99]
# a = []
# c = []
# for i in b :
#     if i >= 55:
#         if i == 55:
#             continue
#         a.append(i)
#     else :
#         c.append(i)
# print(a)
# print(c)

#手动输入一个字符串，1、将字符串首字母变大写 2、如果字符串中含有字母a，就把a替换成123 3、如果有空格就去掉
# while True:
#     i = input("输入一个字符串：")
#     c = i.replace(" ", "")
#     a = c.title()
#     b = a.replace('a','123')
#     print(b)

#去掉列表中的重复数据
# a = [1234,1234,2768,1234,36,36,2328,1234,36,36,36,36,36,1234,1234,1234]
# for i in a :
#     if a.count(i) > 1:
#         for b in range(a.count(i)-1):
#             a.remove(i)
# print(a)

# a = [1234,1234,2768,1234,36,36,2328,1234,36,36,36,36,36,1234,1234,1234]
# b = []
# for i in a :
#     if i not in b :
#         b.append(i)
# print(b)


#打印出100以内所有7的倍数以及带有7的所有数字
# for i in range(1,101):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         print(i)

#三次猜数字
# import random
# a = random.randint(0,10)
# for c in range(3):
#     i = int(input("请输入一个10以内的整数："))
#     if i > a:
#         if c == 2:
#             continue
#         print("猜大了,还剩下%d次机会 " % (2-c))
#     elif i < a:
#         if c == 2:
#             continue
#         print("猜小了,还剩下%d次机会 " % (2-c))
#     else :
#         print("猜对了")
#         break
# else:
#     print("真棒，三次都不对")


#打印user1到user50
# a = 1
# while a <= 50:
#     print("user%d" % a)
#     a += 1

#随机输入一组数据，然后排序
# a = input("请输入一组数据：")
# i=a.split(",")
# c = []
# for d in i:
#     c.append(int(d))
# for g in range(len(c) - 1):
#     for h in range(len(c)-1):
#         if c[g] > c[h]:
#             c[g],i[g+1] = c[g+1],i[g]
# print(c)


# i = [12,23,11,34,98,45]
# for a in range(len(i)-1) :
#     for b in range(a+1,len(i)):
#         if i[a] > i[b]:
#             i[a],i[b] = i[b],i[a]
# print(i)


#复制
# a = ["shi","lei","xixi","haha"]
# b = a.copy()
# print(b)


