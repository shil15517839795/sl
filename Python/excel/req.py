#!/usr/bin/python
# -*-coding:utf-8-*-
# import requests
# import re
# for j in range(264,703):
#     url=(f"http://www.quanshuwang.com/book/9/9055/9674{j}.html")#请求网页
#     html=requests.get(url)#接收响应内容，网页是用什么样的语言写的就用什么样的编码方式去解码
#     # print(html)
#     #1、接收方式：text，以Unicode编码方式接收
#     # neiRong=html.text
#     # print(neiRong)
#     #2、接收响应方式：content，以字节方式接收
#     neiRong=html.content.decode("GBK")
#     # print(neiRong)
#     biaoTi=re.findall(re.compile('<title>盗墓笔记_(.*?)_全书网</title>',re.S),neiRong)
#     zhengZe=re.compile('type="text/javascript"></script></div>(.*?)<script type="text/javascript">style6',re.S)
#     result=re.findall(zhengZe,neiRong)
#     # print(result[0]+'<br />')
#     a =result[0]+'<br />'
#     b=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
#     b_neirong=re.findall(b,a)
#     # b_neirong=re.findall(b,aaa)
#     # print(b)
#     with open('hhh.txt','a',encoding='utf-8') as f:
#         f.write('\t\t\t\t\t\t\t\t\t\t'+biaoTi[0]+'\n')
#         for i in b_neirong:
#             f.write(i+'\n')


# http://www.quanshuwang.com/book/9/9055/9674264.html
# http://www.quanshuwang.com/book/9/9055/9674265.html
# http://www.quanshuwang.com/book/9/9055/9674266.html
# http://www.quanshuwang.com/book/9/9055/9674702.html

#1."."匹配任意一个字符
#2."*"匹配前一个字符0次或者多次
#3."()"将括号内的内容看作是一个整体
#4."[]"匹配括号内的任意一个字符
#5."[^]"匹配除了括号里的任意一个字符
#6."{}"匹配前面字符重复几次
#7."^ $"匹配开头或者结尾的
#8."\b"匹配单词边界
#9."?"匹配前一个字符0次或者1次
#10."|" 或的意思
#非贪婪模式
# *?:匹配0次
# +?:匹配1次
# ??:匹配0次
# {m,n}:只匹配m次
# import re
# a='wqe\nQfwq123qfQwqw'
# zhengze=re.compile('q(.*?)q',re.I)
# result=re.findall(zhengze,a)
# print(result)


#爬盗墓笔记
# import requests
# import re
# for j in range(264,703):
#     url=(f"http://www.quanshuwang.com/book/9/9055/9674{j}.html")#请求网页
#     html=requests.get(url)#接收响应内容，网页是用什么样的语言写的就用什么样的编码方式去解码
#     neiRong=html.content.decode("GBK")
#     biaoTi=re.findall(re.compile('<title>盗墓笔记_(.*?)_全书网</title>',re.S),neiRong)
#     zhengZe=re.compile('type="text/javascript"></script></div>(.*?)<script type="text/javascript">style6',re.S)
#     result=re.findall(zhengZe,neiRong)
#     a =result[0]+'<br />'
#     b=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
#     b_neirong=re.findall(b,a)
#     with open('hhh.txt','a',encoding='utf-8') as f:
#         f.write('\t\t\t\t\t\t\t\t\t\t'+biaoTi[0]+'\n')
#         for i in b_neirong:
#             f.write(i+'\n')k


#爬图片
# import requests
# import re
# request=requests.get("http://www.mmonly.cc/sgtp/")
# response=request.content.decode("gbk")#用来接收响应以及设置接收的编码方式
# # print(response)
# guoLv1=re.compile('<div class="img">(.*?)original=',re.S)#正则表达式预编译
# bianLi1=re.findall(guoLv1,response)#遍历匹配响应内容
# # print(bianLi1)
# word = re.findall(re.compile('alt="(.*?)"',re.S),str(bianLi1))
# # print(word)
# lianJie=re.findall(re.compile('src="(.*?)"',re.S),str(bianLi1))
# request_picture=requests.get(lianJie[0])
# # print(picture)
# # print(lianJie)
# # a=zip(word,lianJie)
# for i,j in zip(word,lianJie):
#     request_picture=requests.get(j)
#     picture = request_picture.content
#     with open(r'E:\shi\Python\excel\tupian\{}.jpg'.format(i),'wb') as f:
#         f.write(picture)





# import requests
# import re
# for x in range(1,11):
#     request=requests.get(f"http://www.mmonly.cc/wmtp/list_20_{x}.html")
#     response=request.content.decode("gbk")#用来接收响应以及设置接收的编码方式
#     # print(response)
#     guoLv1=re.compile('<div class="imgwkc">(.*?)original=',re.S)#正则表达式预编译
#     bianLi1=re.findall(guoLv1,response)#遍历匹配响应内容
#     # print(bianLi1)
#     word = re.findall(re.compile('alt=(.*?)" ',re.S),str(bianLi1))
#     # print(word)
#     lianJie=re.findall(re.compile('src="(.*?)"',re.S),str(bianLi1))
#     request_picture=requests.get(lianJie[0])
#     # print(picture)
#     # print(lianJie)
#     a=zip(word,lianJie)
#     for i,j in zip(word,lianJie):
#         request_picture=requests.get(j)
#         picture = request_picture.content
#         with open(r'E:\shi\Python\excel\tupian1\{}.jpg'.format(i),'wb') as f:
#             f.write(picture)




#动态爬虫
# import requests
# import json
# url='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.215104%7C34.754749%7C114.577653%7C34.844963&keywords=%E6%B4%97%E6%B5%B4%E4%B8%AD%E5%BF%83'
# head={'Host':'www.amap.com',
# 'User-Agent':'Mozilla/5.0 (WindowsNT10.0;Win64; x64;rv:70.0)Gecko/20100101Firefox/70.0',
# 'Accept':'*/*',
# 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 'Accept-Encoding':'gzip,deflate,br',
# 'amapuuid':'4c212586-a36f-4243-b3b5-8b4d14d7daa8',
# 'x-csrf-token':'null',
# 'X-Requested-With':'XMLHttpRequest',
# 'Connection':'keep-alive',
# 'Referer':'https://www.amap.com/search?query=%E6%B4%97%E6%B5%B4%E4%B8%AD%E5%BF%83&city=410200&geoobj=114.215104%7C34.754749%7C114.577653%7C34.844963&zoom=12',
# 'Cookie': 'key=bfe31f4e0fb231d29e1d3ce951e2c780; guid=3c10-aabf-9328-ba77; cna=1XRCFuo3SHoCAbZ4MhbEw/Rh; UM_distinctid=16e2486b871a-0b12df9d073cc3-4c302b7a-144000-16e2486b873c9; CNZZDATA1255626299=1328001706-1572567107-https%253A%252F%252Fwww.baidu.com%252F%7C1572577907; isg=BDc32bF2JrVyLaI5_8OOBlvxxStBVAFllx6_EYnkToZtOFd6kMx6rvcRGljDy-PW; l=dBN4fhdcqlCO5jZdBOCNmuIRhcQO_IOYYuPRwRqpi_5aH68s20QOkNDdDFJ6csWftZ8p4XAbiLp9-etk9FCZOCRGeXE3uxDc.; _uab_collina=157257084108278461672597; x5sec=7b22617365727665723b32223a22376265626334666139613930646436666135616363373935636530623433326343497a4f37753046454b6a676f764f2b744f373066513d3d227d',
# 'If-None-Match':'W/"757c-eQQQDgK5jkL2Bj4xmORXxGO0J8Q"',
# 'Cache-Control':'max-age=0'}
# html=requests.get(url,headers=head)
# result=html.text
# result=json.loads(result)
# print(result)
# read=json.load(open(r'jsonsource.dat','r'))
# json.dump(read,open('newjsonfile.dat','w'))
# aaaa=json.loads(read)
# print(aaaa)



# 爬智联招聘
# import requests
# import json
# def request_zhilian():
#     url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.07902557&x-zp-page-request-id=0dfbc13f69644f09a13d23e14d4d0aa4-1572657082000-950010&x-zp-client-id=b8517405-4cec-4a0d-a01b-2eed35a54ee3'
#     head = {'Host':'fe-api.zhaopin.com',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
# 'Accept':'application/json, text/plain, */*',
# 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Origin':'https://sou.zhaopin.com',
# 'Connection':'keep-alive',
# 'Referer':'https://sou.zhaopin.com/?jl=538&sf=0&st=0&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3',
# 'Cookie':'urlfrom2=121126445; adfbid2=0; x-zp-client-id=b8517405-4cec-4a0d-a01b-2eed35a54ee3; sts_deviceid=16e25d89821448-0cc66ae0afc5258-4c302b7a-1327104-16e25d898223aa; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e25d89837108-0e86574e1b487e8-4c302b7a-1327104-16e25d8983864b%22%2C%22%24device_id%22%3A%2216e25d89837108-0e86574e1b487e8-4c302b7a-1327104-16e25d8983864b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%7D; acw_tc=3ccdc15d15725929823118540e59e4392e02f660f45386c632928c4b566a25; adfcid2=none; dywea=95841923.3197260489302350300.1572592989.1572606504.1572655387.4; dywez=95841923.1572593039.1.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1572592990,1572593039,1572606504,1572655387; __utma=269921210.1604528657.1572592990.1572606505.1572655388.5; __utmz=269921210.1572593039.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; sou_experiment=capi; LastCity=%E4%B8%8A%E6%B5%B7; LastCity%5Fid=538; ZP_OLD_FLAG=false; POSSPORTLOGIN=8; CANCELALL=0; urlfrom=121126445; adfbid=0; sts_sg=1; sts_evtseq=11; sts_sid=16e29909f0462-0cdcbb15e3bb418-4c302b7a-1327104-16e29909f05117; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAs0FYUkI00000P_OfNC00000T1BdaZ.THLyktAJdIjA80K85ydEUhkGUhNxndqbusK15H6LPWf1mWu9nj0sujN-nAn0IHY4PDu7rjwDrjn3rRNjPRPAwbcLwHKArH6swjmLn17AnsK95gTqFhdWpyfqn1c3rjb4rjc4PiusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1YdPHRkn0%26tpl%3Dtpl_11534_19968_16032%26l%3D1514225627%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3288998295_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D64%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_3_dg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26rqlang%3Dcn; adfcid=none; dyweb=95841923.1.10.1572655387; dywec=95841923; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1572657033; jobRiskWarning=true; __utmb=269921210.1.10.1572655388; __utmc=269921210; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%224db31fdd-046e-4012-a15b-f21325cb6934-sou%22%2C%22funczone%22:%22smart_matching%22}}',
# 'TE':'Trailers'}
#     request = requests.get(url, headers=head)
#     html = request.json()
#     return html
# def create_excel():
#     import xlwt
#     geShi=xlwt.Workbook(encoding='utf-8')
#     sheet=geShi.add_sheet('软件测试工程师')
#     geShi.save('智联招聘.xls')
# def read_json(shuJu,i):
#     jobName=shuJu['data']['results'][i]['jobName']
#     company=shuJu['data']['results'][i]['company']['name']
#     salary=shuJu['data']['results'][i]['salary']
#     city=shuJu['data']['results'][i]['city']['display']
#     return city,company,jobName,salary
# def addTo_excel(html,nums):
#     from xlutils.copy import copy
#     import xlrd
#     read_excel=xlrd.open_workbook('智联招聘.xls')
#     new_excel=copy(read_excel)
#     sheet_1=new_excel.get_sheet('软件测试工程师')
#     sheet_1.write(0,0,'城市')
#     sheet_1.write(0,1, '公司')
#     sheet_1.write(0,2, '职位')
#     sheet_1.write(0,3, '薪资')
#     for i in range(nums):
#         sheet_1.write(i+1,0,read_json(html,i)[0])
#         sheet_1.write(i+1,1, read_json(html,i)[1])
#         sheet_1.write(i+1,2, read_json(html,i)[2])
#         sheet_1.write(i+1,3, read_json(html,i)[3])
#     new_excel.save('智联招聘.xls')
# import time
# wangZhi=request_zhilian()
# time.sleep(3)
# create_excel()
# time.sleep(1)
# addTo_excel(wangZhi,50)

#爬智联招聘到数据库
# import requests
# import json
# import pymysql
# def aa():
#     url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=719&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.87574066&x-zp-page-request-id=b65f4c17aaa7440daa3e3202602d4d40-1572959920398-968936&x-zp-client-id=b8517405-4cec-4a0d-a01b-2eed35a54ee3'
#     head={'Host':'fe-api.zhaopin.com',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
#     'Accept':'application/json, text/plain, */*',
#     'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Accept-Encoding':'gzip, deflate, br',
#     'Origin':'https://sou.zhaopin.com',
#     'Connection':'keep-alive',
#     'Referer':'https://sou.zhaopin.com/?jl=719&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3',
#     'Cookie':'urlfrom2=121126445; adfbid2=0; x-zp-client-id=b8517405-4cec-4a0d-a01b-2eed35a54ee3; sts_deviceid=16e25d89821448-0cc66ae0afc5258-4c302b7a-1327104-16e25d898223aa; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e25d89837108-0e86574e1b487e8-4c302b7a-1327104-16e25d8983864b%22%2C%22%24device_id%22%3A%2216e25d89837108-0e86574e1b487e8-4c302b7a-1327104-16e25d8983864b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%7D; acw_tc=3ccdc15d15725929823118540e59e4392e02f660f45386c632928c4b566a25; adfcid2=none; dywea=95841923.3197260489302350300.1572592989.1572923612.1572959903.8; dywez=95841923.1572593039.1.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1572851319,1572914572,1572923612,1572959904; __utma=269921210.1604528657.1572592990.1572923613.1572959904.9; __utmz=269921210.1572593039.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; sou_experiment=capi; LastCity=%E9%83%91%E5%B7%9E; LastCity%5Fid=719; ZP_OLD_FLAG=false; POSSPORTLOGIN=6; CANCELALL=0; urlfrom=121126445; adfbid=0; sts_sg=1; sts_evtseq=5; sts_sid=16e3bb7446b16c-0660279233cac5-4c302b7a-1327104-16e3bb7446c503; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAsaHI_7I00000P_OfNC00000T1BdDM.THLyktAJdIjA80K85ydEUhkGUhNxndqbusK15HbYnjDvnHDLnj0snWc3rym0IHY4PDu7rjwDrjn3rRNjPRPAwbcLwHKArH6swjmLn17AnsK95gTqFhdWpyfqn1c3rjb4rjc4PiusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1Y1nWRsrf%26tpl%3Dtpl_11534_19968_16032%26l%3D1514225627%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3288998295_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D64%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_3_dg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26rqlang%3Dcn; adfcid=none; dyweb=95841923.1.10.1572959903; dywec=95841923; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1572959912; jobRiskWarning=true; __utmb=269921210.1.10.1572959904; __utmc=269921210; __utmt=1; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22c7a3f235-c92d-4b7f-82d1-8517bcb3a25c-sou%22%2C%22funczone%22:%22smart_matching%22}}',
#     'TE':'Trailers'}
#     request=requests.get(url,headers=head)
#     html=request.json()
#     print(html)
#     return html
# def create():
#     connect=pymysql.connect(host='192.168.10.45',user='root',password='shi123',port=3306)
#     cs=connect.cursor()
#     cs.execute('create database abc;')
#     cs.execute('use abc;')
#     cs.execute('create table aaa(JobName char(50),company char(50),city char(50),salary char(30));')
# create()
# for i in range(20):
#     JobName=(aa()['data']['results'][i]['jobName'])
#     company=(aa()['data']['results'][i]['company']['name'])
#     city=(aa()['data']['results'][i]['city']['display'])
#     salary=(aa()['data']['results'][i]['salary'])
#     connect = pymysql.connect(host='192.168.10.45', user='root', password='shi123', port=3306)
#     cs = connect.cursor()
#     cs.execute('use abc;')
#     cs.execute('insert into aaa values("{}","{}","{}","{}");'.format(JobName,company,city,salary))
# connect.commit()
# connect.close()


#爬一部小说
# import requests
# import re
# for j in range(264,703):
#     url=(f'http://www.quanshuwang.com/book/9/9055/9674{j}.html')
#     req=requests.get(url)
#     html=req.content.decode('gbk')
#     guoLv=re.compile('type="text/javascript">style5(.*?)<script type="text/javascript">style6',re.S)
#     title=re.findall(re.compile('<strong class="l jieqi_title">正文(.*?)</strong><a href=',re.S),html)
#     bianLi=re.findall(guoLv,html)
#     a=bianLi[0]+'<br />'
#     # print(a)
#     guoLv1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
#     result=re.findall(guoLv1,a)
#     with open('aaa.txt','a',encoding='utf-8') as f:
#         f.write('\t'*8+title[0]+'\n')
#         for i in result:
#             f.write(i+'\n')
#         f.write('\n')
#     f.close()
















# class shi():
#     def __init__(self,name,xue,zhan):
#         self.name = name
#         self.xue = xue
#         self.zhan = zhan
#     def fighting(self):
#         self.xue -= 100
#         self.zhan += 200
#     def relax(self):
#         self.xue += 300
#     def pri(self):
#         print(f'{self.name}剩下{self.xue},战斗力为{self.zhan}')
# class lei(shi):
#     pass
# q = lei('马克',1000,3000)
# w = lei('项羽',3000,1500)
# q.fighting()
# q.fighting()
# w.relax()
# q.pri()
# w.pri()