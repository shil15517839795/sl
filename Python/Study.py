#!/usr/bin/python
# -*-coding:utf-8-*-
#计算从昨天下午六点一直到现在经过了多少时间戳
# import time
# a = time.strptime('2019/11/01 18:00:00','%Y/%m/%d %X')
# b=time.mktime(a)
# c=time.time()
# print(c-b)

#设置休眠时间
# from time import *
# start=time()
# for i in range(3):
#     print(i)
#     sleep(5)
# end=time()
# print("这个程序执行结束一共用了%f秒:"%(end-start))


#爬一部小说，并将它写到txt文件中
# import requests
# import re
# for i in range(876,906):
#     url=(f'http://www.quanshuwang.com/book/38/38304/13947{i}.html')
#     html=requests.get(url)
#     response=html.content.decode('gbk')
#     guoLv=re.compile('<script type="text/javascript">style5(.*?)<script type="text/javascript">style6',re.S)
#     biaoTi=re.findall(re.compile('知否？知否？应是绿肥红瘦</a>(.*?)</div>',re.S),response)
#     bianLi=re.findall(guoLv,response)
#     # print(bianLi[0])
#     a = bianLi[0]+'<br />'
#     # print(a)
#     guoLv1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
#     guoLv1_neirong=re.findall(guoLv1,a)
#     # print(guoLv1_neirong)
#     with open(r'E:\shi\Python\bb.txt','a',encoding='utf-8') as f :
#         f.write("\t\t\t\t\t\t\t\t\t\t\t\t"+biaoTi[0]+'\n')
#         for i in guoLv1_neirong:
#             f.write(i)
#             f.write('\n')

#将txt文件中的内容读写到excel表格中
# a = open(r'E:\shi\Python\九九.txt','r',encoding='utf-8')
# b = a.readlines()
# import xlwt
# file= xlwt.Workbook(encoding='utf-8')
# sheet=file.add_sheet('sl')
# for i in range(len(b)):
#     c = b[i].split('\t')
#     for j in range(len(c)):
#         sheet.write(i,j,c[j])
# file.save('a.xls')
#将excel表格中的内容读写到txt文件中
# import xlwt
# file=xlwt.Workbook(encoding='utf-8')
# sheet=file.add_sheet('九九')
# for i in range(10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,f'{i}*{j}={i*j}\t')
# file.save('九九.xls')
# import xlrd
# txt=open('九九.txt','w',encoding='utf-8')
# file1=xlrd.open_workbook('九九.xls')
# look_sheet=file1.sheet_by_name('九九')
# hangShu=look_sheet.nrows
# for m in range(hangShu):
#     for n in range(len(look_sheet.row_values(m))):
#         a = look_sheet.cell(m,n).value
#         txt.write(a+' ')
#     txt.write('\n')

#爬一页小说到数据库表里
# import requests
# import re
# url='http://www.quanshuwang.com/book/44/44683/15379610.html'
# html=requests.get(url)
# response=html.content.decode('gbk')
# guolv=re.compile('text/javascript">style5(.*?)<script type="text/javascript">style6',re.S)
# bianli=re.findall(guolv,response)
# # print(bianli[0])
# a = bianli[0] + '<br />'
# # print(a)
# guolv1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
# guolv1_neirong=re.findall(guolv1,a)
# # print(guolv1_neirong)
# import pymysql
# connect=pymysql.connect(host='192.168.10.89',user='root',password='shi123',port=3306)
# # print(connect)
# cs=connect.cursor()
# cs.execute('create database shi')
# cs.execute("use shi;")
# cs.execute('create table b(name varchar(255));')
# for i in guolv1_neirong:
#     cs.execute('insert into b values ("{}");'.format(i))
# connect.commit()
# connect.close()



#爬小说
# import requests
# import re
# url= "http://www.quanshuwang.com/book/1/1018/326804.html"
# html=requests.get(url)
# response=html.content.decode('gbk')
# guoLv=re.compile('type="text/javascript">style5(.*?)<script type="text/javascript">style6',re.S)
# title=re.findall(re.compile('jieqi_title">(.*?)</strong><a href=',re.S),response)
# bianLi=re.findall(guoLv,response)
# # print(bianLi[0])
# a = bianLi[0]+'<br />'
# # print(a)
# guoLv1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
# guoLv1_neirong=re.findall(guoLv1,a)
# # print(guoLv1_neirong)
# with open('haha.txt','w',encoding='utf-8') as f:
#     f.write('\t'*9+title[0]+'\n')
#     for i in guoLv1_neirong:
#         f.write(i+'\n')


#设置休眠时间
# from time import *
# start=time()
# for i in range(5):
#     print(i)
#     sleep(3)
# end=time()
# print("此程序执行结束共用了%f秒："%(end-start))

# import time
# from time import sleep
# a=time.time()
# for i in range(3):
#     print(i)
#     sleep(3)
# b=time.time()
# print("%f" %(b-a))







