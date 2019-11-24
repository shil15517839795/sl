#!/usr/bin/python
# -*-coding:utf-8-*-
#1、导入相关库和方法
import smtplib#封装了smtp协议
from email.mime.multipart import MIMEMultipart#处理邮件中的组成部分
from email.mime.text import MIMEText#负责构建文本

#2、设置邮箱域名，smtp服务器，这里使用的是163邮箱
mail_host='smtp.163.com'
mail_sender='shi15517839795@163.com'#设置发件人邮箱
mail_licence='shi123'#邮箱授权码，注意不是邮箱密码,licence:许可证
mail_receiver='1583792786@qq.com'#设置收件人邮箱,可以是多个收件人

#3、创建一个空邮件，可以在里面添加文本、图片、附件
message=MIMEMultipart()

#4、设置邮件头部内容
#设置邮件主题
message['subject']='测试的第一封邮件'
#设置发送者
message['from']=mail_sender
#设置邮件接收者
message['to']=mail_receiver

#5、添加正文文本
#邮件正文内容
text='You know what? When I first saw you,I said to myself.Oh,my god! This one is going to heart.'
info_text=MIMEText(text)
#向MIMEMultipart对象中添加文本对象
message.attach(info_text)

#5、添加图片
att2 =MIMEText(open(r'E:\shi\Python\excel\tupian1\漂亮的小清新花卉意境图片.jpg', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="hei.jpg"'
message.attach(att2)## 头部字段

#6、发送邮件
stp=smtplib.SMTP()#创建smtp对象:stp=smtplib.SMTP_SSL(mail_host，465)
stp.connect(mail_host,25)
stp.login(mail_sender,mail_licence)#登录邮箱
stp.sendmail(mail_sender,mail_receiver,message.as_string())#发送邮件
print("邮件发送成功")
stp.close()#关闭smtp


