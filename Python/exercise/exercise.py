#!/usr/bin/python
# -*-coding:utf-8-*-
#列表
# a = [32,34,2,56,7,34,32,98]
# print(a.index(56))
# a.remove(32)
# print(a)
# a.append(100)
# print(a)
# a.pop(2)
# print(a)
# del a[2]
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a.insert(0,12)
# print(a)
# # a.clear()
# # print(a)
# a[3]=56
# print(a)
# b=[]
# b.extend(a)
# print(b)

#字符串
# a = "fagkdfSFDFh"
# a.upper()
# print(a)
# a.lower()
# print(a)
# a.title()
# print(a)
# a.swapcase()
# print(a)
# print(a.index("a"))
# b=a.split("d")
# c="-".join(b)
# print(c)
# a.startswith("f")
# a.endswith("h")
# a.strip()
# print(a)
# #元祖
# a = (23,43,12,43)
# print(a.count(43))
# print(a.index(23))

#字典
# a = {"name":"zhangsan","age":21,"sex":"男"}
# print(a.keys())
# print(a.values())
# print(a.items())
# a.pop("name")
# print(a)
# a.popitem()
# print(a)
# b={}
# b.update(a)
# print(b)
# a.clear()
# print(a)
#集合
# a = {32,213,423,12,22}
# a.add(15)
# print(a)
# a.remove(22)
# print(a)
# a.pop()
# print(a)

#系统函数
# for i,j in enumerate('qwertyuiop'):
#     print(i,j)
# count
# len
#1、sum():求和，（）里面只能是列表、元祖、集合
# a = sum({2,4,3})
# print(a)

#2、max():求最大值，按照ASCII码排序,但必须是同种类型，（）里面可以是列表、元祖、集合
# a=max([1,2,3,4])
# print(a)

#3、min():求最小，按照ASCII码排序,但必须是同种类型，（）里面可以是列表、元祖、集合
# a=min([1,2,3,4])
# print(a)

#4、divmod():
# a,b=divmod(60,8)
# print(a,b) #a为商，b为余数

#5、chr():将码转换为ascii码中对应的值
# shi=chr(65)
# print(shi)

# a = [chr(i) for i in range(65,91)]
# print(a)

#6、ord():将值转换为ascii码中对应的码
# a = ord("b")
# print(a)

#7、bin():将十进制转换为二进制
# a = bin(7)
# print(a)

#8、oct():将十进制转换为八进制
# a = oct(8)
# print(a)
#9、hex():将十进制转换为十六进制
# a=hex(16)
# print(a)

#10、int():将二进制（0b）、八进制（0o）、十六进制（0x）转换为十进制
# a=int(0b10)
# print(a)
#
# a=int(0o10)
# print(a)
#
# a=int(0x10)
# print(a)



# 将excel表格中的内容读写到txt文件中
import xlwt
file=xlwt.Workbook(encoding='uft-8')
sheet=file.add_sheet('yyy')
for i in range(10):
    for j in range(1,i+1):
        sheet.write(i-1,j-1,f'{i}*{j}={i*j}\t')
file.save('yy.xls')
import xlrd
a = open('gg.txt','w',encoding='utf-8')
file1=xlrd.open_workbook('yy.xls')
look_sheet=file1.sheet_by_name('yyy')
hangshu=look_sheet.nrows
for i in range(hangshu):
    for j in range(len(look_sheet.row_values(i))):
        b = look_sheet.cell(i,j).value
        a.write(b+' ')
    a.write('\n')
a.close()

# 将txt文件中的内容读写到excel表格中
a = open('gg.txt','r',encoding='utf-8')
b = a.readlines()
# print(b)
import xlwt
file = xlwt.Workbook(encoding='utf-8')
sheet=file.add_sheet('hhhh')
for i in range(len(b)):
    c=b[i].split('\t')
    # print(c)
    for j in range(len(c)):
        sheet.write(i,j,c[j])
file.save('hhhh.xls')


# 爬一部小说
import requests
import re
for i in range(79610,80350):
    url=(f'http://www.quanshuwang.com/book/44/44683/153{i}.html')
    html=requests.get(url)
    neiRong=html.content.decode('gbk')
    # biaoTi=re.findall(re.compile('(.*?)'))
    guoLv=re.compile('type="text/javascript">style5(.*?)<script type="text/javascript">style6',re.S)
    result=re.findall(guoLv,neiRong)
    # print(result[0])
    a=result[0]+'<br />'
    b=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
    b_neirong=re.findall(b,a)
    with open('oo.txt','w',encoding='utf-8') as f:
        for i in b_neirong:
            f.write(i+'\n')




# 爬图片
# import requests
# import re
# request=requests.get('http://www.mmonly.cc/wmtp/')
# response=request.content.decode('gbk')
# guoLv=re.compile('<div class="imgwkc">(.*?)> </a> </div>')
# bianLi=re.findall(guoLv,response)
# # print(bianLi)
# word=re.findall(re.compile('alt="(.*?)"',re.S),str(bianLi))
# link=re.findall(re.compile('src="(.*?)"',re.S),str(bianLi))
# # print(word)
# # print(link)
# request_picture=requests.get(link[0])
# for i,j in zip(word,link):
#     request_picture=requests.get(j)
#     picture=request_picture.content
#     with open(r'E:\shi\Python\excel\tupian1\{}.jpg'.format(i),'wb') as f:
#         f.write(picture)



#将txt文件中的九九乘法表读写到excel表格中
# a = open('a.txt','w',encoding='utf-8')
# for i in range(10):
#     for j in range(1,i+1):
#         a.write(f'{i}*{j}={i*j}\t')
#     a.write('\n')
# a.close()
# b=open('a.txt','r',encoding='utf-8')
# c = b.readlines()
# import xlwt
# file=xlwt.Workbook(encoding='utf-8')
# sheet=file.add_sheet('九九乘法表')
# for x in range(len(c)):
#     d = c[x].split("\t")
#     for y in range(len(d)):
#         sheet.write(x,y,d[y])
# file.save('九九乘法表.xls')

#将excel中的九九乘法表读写到txt文件中
# import xlwt
# file=xlwt.Workbook('utf-8')
# sheet=file.add_sheet('嗯哼')
# for i in range(10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,f'{i}*{j}={i*j}\t')
# file.save('哦哦.xls')
# import xlrd
# a = open('哈哈.txt','w',encoding='utf-8')
# file1=xlrd.open_workbook('哦哦.xls')
# look_sheet=file1.sheet_by_name('嗯哼')
# hangshu=look_sheet.nrows
# for x in range(hangshu):
#     for y in range(len(look_sheet.row_values(x))):
#         b = look_sheet.cell(x,y).value
#         a.write(b)
#     a.write('\n')
# a.close()


# from time import *
# start=time()
# for i in range(3):
#     print(i)
#     sleep(2)
# end=time()
# print('此代码执行结束所用的时间为%f'%(end-start))

#爬一页小说
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
#     with open(r'E:\shi\Python\exercise\a.txt','a',encoding='utf-8') as f :
#         f.write("\t\t\t\t\t\t\t\t\t\t\t\t"+biaoTi[0]+'\n')
#         for i in guoLv1_neirong:
#             f.write(i)
#             f.write('\n')









