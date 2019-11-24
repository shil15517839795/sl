#!/usr/bin/python
# -*-coding:utf-8-*-
# xlwt:对excel的写入的操作
# xlrd：对excel的读取的操作
# import xlwt
# # 设置excel文件的格式
# file = xlwt.Workbook(encoding='utf-8')
#
# # 创建标签页，并命名标签页 cell_overwrite_ok=True表示单元格可以重设值
# sheet = file.add_sheet('py_1906',cell_overwrite_ok=True)
# sheet1=file.add_sheet('第二页')
# # sheet.write(0,1,'内容')#第一个数字代表行，第二个代表列数
# for i in range(10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,"%d*%d=%d" %(i,j,i*j))
# # 保存并关闭文件,可以加上不同的路径来保存文件
# file.save('a.xls')


# import xlrd
# file = xlrd.open_workbook('a.xls')#打开要读的excel文件
#第一种方法
# sheet_count=file.nsheets
# print(sheet_count) #统计文件中标签页的数量
# look_sheet=file.sheets()[0]
# print(look_sheet)#通过索引进入到要进入的标签页，看到的是对应标签页的位置
# a=look_sheet.cell(0,0).value
# b=look_sheet.cell(1,0).value
# print(a,b)#查看excel表格对应标签页的单元格的内容

#第二种方法
# sheet_name=file.sheet_names()
# print(sheet_name)#查看excel表格的所有标签页的名称
# look_sheet=file.sheet_by_name("py_1906")
# print(look_sheet)#通过标签页的名字进入标签页
# hang_count=look_sheet.nrows
# print(hang_count)#统计标签页内容的行数
# # for i in range(10):
# #     hang_neirong=look_sheet.row_values(i)
# #     print(hang_neirong)#查看行里面的内容
#
# lie_count=look_sheet.ncols
# print(lie_count)#统计标签页的列数
# lie_neirong=look_sheet.col_values(4)
# print(lie_neirong)#查看标签页某一列的内容

# a=look_sheet.cell(0,0).value
# b=look_sheet.cell(1,0).value
# print(a,b)



#xlutils模块
# from xlutils.copy import copy
# import xlrd
# file=xlrd.open_workbook('a.xls')
# New_file=copy(file)#不是直接操作我们打开的excel文件，而是复制一份操作复制的文件，只有写的操作
# sheet=New_file.get_sheet(0)#get_sheet(下标位置)，根据下标位置进入标签页
# sheet.write(1,1,'你好时雷')
# New_file.save('sl.xls')


# a = open('a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         a.write(f'{i}*{j}={i*j}\t')
#     a.write("\n")
# a.close()

# b = open('a.txt','r',encoding='utf-8')
# c = b.readlines()
# print(c)


#将excel中内容写入到txt文件中
# import xlwt
# file = xlwt.Workbook(encoding='utf-8')
# sheet =file.add_sheet("shi")
# for i in range(10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,"%d*%d=%d" %(i,j,i*j))
# file.save("x.xls")
#
# import xlrd
# txt=open('y.txt','w',encoding='utf-8')
# file =xlrd.open_workbook("x.xls")
# sheet_name=file.sheet_names()
# look_sheet=file.sheet_by_name("shi")
# hang_shu=look_sheet.nrows
# for i in range(hang_shu):
#     for j in range(len(look_sheet.row_values(i))):
#         a = look_sheet.cell(i,j).value
#         txt.write(a+" ")
#     txt.write("\n")
# txt.close()


#将txt中内容写入到excel表格中
# a = open('b.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         a.write("%d*%d=%d\t" %(i,j,i*j))
#     a.write("\n")
# a.close()
#
# d=open('b.txt','r',encoding='utf-8')
# b=d.readlines()
# # print(b)
#
# import xlwt
# file=xlwt.Workbook(encoding='utf-8')
# sheet=file.add_sheet('s')
# for c in range(len(b)):
#     e=b[c].split("\t")
#     for k in range(len(e)):
#         sheet.write(c,k,e[k])
# file.save("l.xls")









#时间模块
# import time
# second=time.time()
# local=time.localtime(second)#显示的是本地时间
# print(local)
# utc=time.gmtime(0)#显示UTC时间
# print(utc)

#格式化时间
# import time
# geshihua=time.strftime("%Y/%m/%d %H:%M:%S ",time.localtime())
# print(geshihua)#将结构化时间转换为格式化时间

# import time
# jieGouhua=time.strptime("2019/10/28 18:00:00","%Y/%m/%d %X")#将格式化时间转化为结构化时间，因为只有结构化时间才能转化为时间戳
# shiJian=time.mktime(jieGouhua)#将结构化时间转换为时间戳
# # print(shiJian)
# a=time.time()
# # print(a)#从1790年到现在所经过的时间戳
# print(a-shiJian)#两个时间戳相减


# from time import *
# start=time()
# for i in range(3):
#     print(i)
#     sleep(3)#休眠时间3秒再运行
# end=time()
# print('这个代码执行的时间为%f' %(end-start))


#输入一个年份，判断它是闰年还是平年
# a = int(input("请输入年份："))
# if a%4==0:
#     if a%400==0:
#         print("世纪闰年")
#     else:
#         print("是闰年")
# else:
#     print("是平年")



#去除b.txt中所有的空行和以#开头的行
# a = open(r"E:\shi\Python\shi\b.txt",'r',encoding='utf-8')
# b=a.readlines()
# c=[]
# for i in b:
#     if b.count(i)==1:
#         c.append(i)
#     if i.startswith('#'):
#         c.remove(i)
#     for m in c:
#         if m==('\n'):
#             c.remove(m)
# d = open(r'E:\shi\Python\shi\b.txt','w',encoding='utf-8')
# for j in c:
#     d.write(j)
# d.close()