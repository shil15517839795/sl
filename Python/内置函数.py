#!/usr/bin/python
# -*-coding:utf-8-*-
# 字符串的内置函数
#1、upper()：将小写字母变大写字母
# a = "bcd"
# i = a[1].upper()
# print(i)
#
# a = "bcd"
# i = a.upper()
# print(i)

#2、lower():将大写变小写
# a = "BCD"
# i = a.lower()
# print(i)

# print(input("请输入一串大写字符串：").lower())

#3、title()：将首字母大写
# a = "bcd"
# i = a.title()
# print(i)

#4、swapcase():大小写相互转换
# a = input("输入一串字母:")
# i = a.swapcase()
# print(i)

#5、将字符串中的字符替换为其他数据：replace("原内容","替换内容",替换数量)
# a = "151617"
# # b = a.replace("1","q",2)
# # print(b)

#6、以括号中的数据为分隔符，将字符串分割成列表：split("分隔符")
# a = "bcdefg"
# b = a.split("e")
# print(b)

#7、以某个数据将列表连接起来形成新的字符串：分隔符.join(元素序列)
# a = ["bcde","123"]
# b = "-".join(a)
# print(b)

# a = "fhfbkfbsfkblkkfblnl"
# b = a.split("b")
# c = "-".join(b)
# print(c)

#8、startswith(字符串")：判断是否以括号中字符串的开头
# a = "bcdefg".startswith("b")
# print(a)

#9、endswith("字符串")：判断是否以括号中字符串的结尾
# a = "bcdefg".startswith("b")
# print(a)

#字符串的三种格式化
#1、"%" %填的数据（%s：通过str（）将输入进去的字符转化成字符串）,%d只能填整数，%f只能填浮点数
# a = "%s" % "123"
# print(a)

#2、a = "{}".format():格式化字符串
# a = "{}*{}={}".format(1,2,1*2)
# print(a)

# a = "{}-{}".format("asdad","dnamd")
# print(a)
#11、strip():去除字符串左右两边的字符  lstrip()去除左边字符；rstrip()去除右边字符
# i = "abcdefa"
# b = i.strip("a")
# print(b)



#12、count():统计括号中字符串的数量
# a = "asdjhaifgakbakcakc".count("a")
# print(a)


#13、index():查看括号中字符串所在的下标位置
# a = "sdjhaifgakbakcakc".index("a")

#14、len():统计有多少个元素
# a = "bcdefg"
# b = len(a)
# print(b)





#九九乘法表
# a = 1
# while a <= 9:
#     b = 1
#     while b <= a :
#         print("{}*{}={}".format(a,b,a*b),end="\t")
#         b += 1
#     print("")
#     a +=1
#输入一个字符串，判断它如果以a或者A开头，以c结尾，打印123；如果是以a开头，打印120；如果以c结尾，打印130；如果都不是则打印789
# while True :
#     i = input("输入一个字符串：")
#     if (i.startswith("a") or i.startswith("A")) and (i.endswith("c")):
#         print("123")
#     elif i.startswith("a"):
#         print("120")
#     elif i.endswith("c"):
#         print("130")
#     else :
#         print("789")

# while True:
#     i = input("输入一个六位数：")
#     if i[0] == i[-1]:
#         if i[1] == i[-2]:
#             if i[2] == i[-3]:
#                 print("回环数字")
#             else:
#                 print(i[2])
#                 print(i[-3])
#         else:
#             print(i[1])
#             print(i[-2])
#     else:
#         print("i")




#计算100以内因数之和等于它本身的数
# for i in range(1,101):
#     a = 0
#     for j in range(1,i):
#         if i % j == 0:
#             a = a + j
#     if a == i:
#         print(a)