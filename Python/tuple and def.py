#!/usr/bin/python
# -*-coding:utf-8-*-
# a = ("qwe","qw3","w234",2342,4234)
# print(a[1][2:])
# print(a[1::3])


# a = {
#     "name" : "张三",
#     "age" : 19,
#     "sex" : "男"
# }
# print(a["sex"])

# a.pop("sex")
# print(a)
# a ["qwe"]="1234"
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())


# a = [11,22,33,44,55,66,77,88,99]
# b = []
# c = []
# for i in a :
#     if i >= 55:
#         if i == 55:
#             continue
#         b.append(i)
#     else:
#         c.append(i)
# d = {"key1" : b,"key2" : c}
# print(d)

# dic = {"k1":"alex","k2":" aric","k3":"Alex","k4":"Tony"}
# a = list(dic.values())
# for i in a:
#     i = i.replace(" ","")
#     if (i.startswith("a") or i.startswith("A")) and i.endswith("c"):
#         print(i)

# set
# a = {123,45,76,8,9,43,8}
# b = {}
# print(a)
# a.add(5)
# a.remove(123)
# print(a)

# a = ["qwe","ert","rty","tyu"]
# for i in enumerate(a):
#     print(i)

# b = {"qwe":212,"wer":345,"ret":567}
# for i,j in b.items():
#     print(i,j)



# a = ["手机","电脑","鼠标垫","游艇"]
# for i,j in enumerate(a):
#     print(i,j)
# b = int(input("输入商品编号："))
# print(a[b])


# a = [1,2,3,"a",4,"c"]
# dic = {}
# dic["key1"]=a[1::2]
# print(dic)

# a = [1,2,3,"a",4,"c"]
# dic = {}
# dic["key1"]=a[1],a[3],a[5]
# print(dic)


# i = "wardewdfwdfsafdae"
# for a in range(len(i)-1):
#     for b in range(a+1,len(i)):
#         if i.count(i[a]) < i.count(i[b]):
#             i[a],i[b]=i[b],i[a]
# print(i)
# for a in set(i):
#     if i.count(a) >= 1:
#         b = print("%s %d" % (a,i.count(a)))
# print("b")


#字符串的反转
# a = "1211141234"
# b = a[::-1]
# c = 0
# for i,j in enumerate(b):
#     for k in range(10):
#         if str(k)==j:
#             c+=k*10**i
# print(c)




#列表推导式:将条件控制语句（循环语句、判断语句等）直接写在列表中，产生的结果会自动存储在列表中
# 计算10以内每个偶数的平方，放在一个列表中
# a = []
# for i in range(2,11,2):
#     a.append(i**2)
# print(a)
#
# b = [i**2 for i in range(2,11,2)]
# print(b)


#将大于55的放在一个列表，小于55的放在另一个列表
# a = [11,22,33,44,55,66,77,88,99]
# b = [i for i in a if i > 55]
# c = [i for i in a if i < 55]
# print(b);print(c)


                                         #函数
# def shi():
#     a = 0
#     for i in range(2,101):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             a += i
#     print(a)

#2、变量的作用域

# 局部变量：只在函数内有用的变量（只在一小块区域内可以使用）
# 全局变量：在整个py文件中都可以使用的（在任何区域都能使用）

# a = 5
# def i():
#     global a
#     a = 2
#     print(a)
# i()
# print(a)

#3、参数传递
#3.1 必须参数：必须填写的参数
#格式：def 变量名(参数名：参数名的命名规则和变量名的命名规则一样)
           # 执行语句块

# def shi(x,y):
#     a = 0
#     for i in range(x,y+1):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             a += i
#     print(a)
# shi(2,100)

#3.2 默认参数：当调用函数时传入数据了就使用传入数据的值，否则就使用默认参数
#格式：def 变量名(参数名=值)
           # 执行语句块
# def a (x=100):
#     b = sum(range(x+1))
#     print(b)
# a() #或者a(填写一个新的值)


# def haha(x=1,y=10):
#     for a in range(x,y):
#         for b in range(1,a+1):
#             print("%d*%d=%d" % (a,b,a*b),end="\t")
#         print("")
# haha()

# 3.3.1 可变长参数：一次性可以接收多个参数
# 格式：def 函数名 (*参数名):
#             执行模块
# def a(*args):
#     print(args)
# a([1,342,532],32,[224,52],"fgsf")

# 3.3.2 可变长参数：一次性可以接收多个参数
# 格式：def 函数名 (**参数名):参数名最好是  **kwargs
#             执行模块
# def a(**kwargs):
#     print(kwargs)
# a(name="张三",age=17,sex="男")

#4、return 返回值
# 作用：将return后面的数据赋值给函数的调用者
        # 结束函数
# 格式：def 函数名():
#     执行语句块
#     return 数据

# # 4.1：将return后面的数据赋值给函数的调用者
# def sum1(x):
#     b = sum(range(x+1))
#     return b
# def sum2(x):
#     for i in range(2,x+1):
#         b = [j for j in range(1,i) if i % j == 0]
#         if sum(b) == i:
#             print(i)
# c = sum1(100)
# sum2(c)

#一个函数，传两个参数a,b，a是列表，b是一个数字，找出a列表中两数之和等于b的打印出来这两个数
# def shi(a,b):
#     c = []
#     for i in a:
#         for j in a:
#             if i + j == b:
#                 c.append(i)
#                 c.append(j)
#                 if c.count(i)>1:
#                     c.remove(i)
#                 if c.count(j)>1:
#                     c.remove(j)
#     print(c)
# shi([10,2,14,1,5],15)

# def shi(a=[],b=0):
#     for i in range(len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[i] + a[j] == b:
#                 print(a[i],a[j],end="\t")
# shi([10,1,14,5,9],15)


# 将a列表里最大的放在最后一位，最小的放在第一位
# a = [19,34,12,56,98,43]
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i] < a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


#统计一个字符串中每个字幕出现的次数，然后根据次数进行排序
# while True:
#     a = input("输入一个字符串：")
#     b = list(set(a))
#     c = []
#     for d in b:
#         e = str(a.count(d))
#         c.append(e+d)
#     c.sort()
#     print(c)
#     for h in c:
#         print(h[-1],end="\t")


# li = [1,2,3,4,5,6,7,8,8]能组成多少个互不相同且不重复的数字的两位数
# li = [1,2,3,4,5,6,7,8,8]
# a = list(set(li))
# a = list(li)
# b = []
# c = []
# for i in a:
    # for j in a :
        # if i != j :
            # h = "%d%d" %(i,j)
            # b.append(h)
# print(b)
# for k in b :
#     if k not in c:
#         c.append(k)
# print(c)


# 嵌套函数
# def haha():
#     a = 1
#     print(1231)
#     return a
# a = haha
# a()


# def ha():
#     a = 1
#     # print(a)
#     def wrapper():
#         b = 2
#         return b
#     return wrapper
#     # wrapper()
# print(ha()())


# def hanshu():
#     a = 1
#     print(a)
#     def wrapper():
#         aa = 111
#         print(aa)
#     # wrapper()
#     # return wrapper()
# print(hanshu())


