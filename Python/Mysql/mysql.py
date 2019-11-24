#!/usr/bin/python
# -*-coding:utf-8-*-
import pymysql
#192.168.10.89
#host:mysql所在的虚拟机的IP地址
#user:mysql的用户
#password:用户的密码
#port:mysql的端口号（默认是3306）
connect=pymysql.connect(host='192.168.10.89',user='root',password='shi123',port=3306)
# print(connect)
cs=connect.cursor()#创建游标，一种临时的数据库对象，相当于购物车
# cs.execute('create database lei;')#执行操作
cs.execute('use lei;')
# cs.execute('create table k(name char(30),age int(5));')
# cs.execute('insert into k values("时雷",20);')
cs.execute('select * from k;')
# data=cs.fetchone()#fetchone:取出数据库表中的一行数据，可迭代
# data_1=cs.fetchone()
# data_2=cs.fetchone()
# print(data,data_1,data_2)
# data=cs.fetchall()#fetchall:取出数据库表中所有的数据
# print(data)
data=cs.fetchmany()#括号里面可以填选择取出数据的个数
print(data)
connect.commit()#提交数据
connect.close()#断开连接