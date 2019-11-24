#!/usr/bin/python
# -*-coding:utf-8-*-
# 计算100以内的质数之和
# a=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         a+=i
# print(a)

#输入一个整数，如果能整除2和3打印helloWord，如果只能整除2打印hello，只能整除3打印Word，既不能整除2又不能整除3打印123
# while 1:
#     a=int(input("请注入一个整数："))
#     if a % 2 == 0:
#         if a % 3 == 0:
#             print('helloWord')
#         else:
#             print('hello')
#     elif a % 3 == 0:
#         print('Word')
#     else:
#         print(123)

# OS模块
# import os
# a = os.getcwd()
# print(a)
# print(os.name)
# b = os.listdir(a)
# print(b)
# a = os.listdir(r'E:\shi\Python\exercise')
# print(a)
# a = os.path.isdir(r'E:\shi\Python\ziDongHua')
# print(a)
# a = os.path.isfile(r'E:\shi\Python\anjian.py')
# print(a)
# a = os.path.split(r'E:\shi\Python\en.txt')
# print(a)
# b = os.path.join(r'E:\shi\Python','en.txt')
# print(b)
# a = os.path.exists('h.txt')
# print(a)

# paramiko模块
# import paramiko
# ssh_client=paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh_client.connect(hostname='192.168.10.49',port=22,username='root',password='shi123')
# stuin,stuout,stuerr=ssh_client.exec_command('ls')
# result=stuout.read().decode('utf-8')
# print(result)
# ssh_client.close()

# 用paramiko模块传输文件
# import paramiko
# tran=paramiko.Transport(('192.168.10.49',22))
# tran.connect(username='root',password='shi123')
# sftp=paramiko.SFTPClient.from_transport(tran)
# localpath='aa.txt'
# remotepath='/root/c.txt'
# sftp.put(localpath,remotepath)
# # sftp.get(remotepath,localpath)
# tran.close()


# pymysql模块
# import pymysql
# connect = pymysql.connect(host='192.168.10.49',user='root',password='shi123',port=3306)
# # print(connect)
# cs=connect.cursor()
# cs.execute('create database shi;')
# cs.execute('use shi;')
# cs.execute('create table lei(name char(20),age int(8));')
# cs.execute('insert into lei values("时雷",23);')
# cs.execute('insert into lei values("张三",22);')
# cs.execute('insert into lei values("李四",20);')
# cs.execute('select * from lei;')
# b=cs.fetchall()
# print(b)

#有100块钱，公鸡5元一只，母鸡3元一只，小鸡一元钱2只，一共需要买鸡100只，而且正好把100元钱花完，而且三种鸡都要有
# for i in range(1,100//5):
#     for j in range(1,100//3):
#         for a in range(1,100*3):
#             if i+j+a==100 and 5*i+3*j+a/2==100:
#                 print(i,j,a)
#输入三个数判断能否组成三角形，且判断组成的是直角、钝角或锐角三角形
# while True:
#     a=int(input("输入边长："))
#     b=int(input("输入边长："))
#     c=int(input("输入边长："))
#     d=[a,b,c]
#     if a+b>c and a+c>b and b+c>a:
#         print("能组成三角形")
#         d.sort()
#         if d[0]**2+d[1]**2>d[2]**2:
#             print("锐角三角形")
#         elif d[0]**2+d[1]**2<d[2]**2:
#             print("钝角三角形")
#         elif d[0]**2+d[1]**2==d[2]**2:
#             print("直角三角形")
#     else:
#         print("不能组成三角形")
#求出1-999中所有的水仙花数
# for i in range(100,1000):
#     a=i//100
#     b=(i-a*100)//10
#     c=i-a*100-b*10
#     if a**3+b**3+c**3==i:
#         print(i,end='\t')
#有1、2、3、4四个数字，判断他们能组成多少不同且两两数字不重复的三位数
# for i in range(1,5):
#     for j in range(1,5):
#         for a in range(1,5):
#             if i!=j and i!=a and j!=a:
#                 print("%d%d%d" %(i,j,a))
#打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d" %(i,j,i*j),end='\t')
#     print('\n')
#计算100以内的偶数与奇数之差
# i=0
# j=0
# for a in range(1,101):
#     if a%2==0:
#         i+=a
#     else:
#         j+=a
# print(i-j)
#求出500以内因数之和等于它本身的数,因数除了它本身以外
# for i in range(1,501):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if a == i:
#         print(i)
#求出100以内质数之和
# a=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         a+=i
# print(a)
#打印出一个列表里所有第一大和第二大的数
# a=[32,90,43,90,85,21,54,85,90]
# a.sort(reverse=True)
# for i in a:
#     if i < a[0]:
#         b=i
#         break
# for j in a:
#     if j == a[0] or j==b:
#         print(j,end='\t')
#选择法和冒泡法排序
#将二进制数转换成十进制数
#读取excel表格里的内容到txt文件里
#读取txt文件中的内容到excel表格里
#爬一部小说




