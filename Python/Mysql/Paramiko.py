#!/usr/bin/python
# -*-coding:utf-8-*-
# import paramiko
# ssh_client=paramiko.SSHClient()#创建一个远程连接的客户端
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)#跳过验证，不到Know_host文件中查找。远程连接的ip会让我们选择yes/no，这个问题是解决自动选择yes
# ssh_client.connect(hostname='192.168.10.89',port=22,username='root',password='shi123')#连接服务器
# stuin,stuout,stuerr=ssh_client.exec_command('ls')#执行操作,stuin是执行的命令，stuout是执行的结果，stuerr是执行的错误
# result=stuout.read().decode('utf-8')#获取命令执行的结果
# print(result)
# ssh_client.close()#断开连接



#用paramiko模块传输文件
# import paramiko
# tran=paramiko.Transport(('192.168.10.89',22))#获取传输通道
# tran.connect(username='root',password='shi123')#输入用户名和密码连接服务器
# sftp=paramiko.SFTPClient.from_transport(tran)#创建一个sftp客户端
# localPath=r'E:\shi\Python\Mysql\oo.txt'#本地路径
# remotePath='/root/b.txt'#远程路径
# # sftp.put(localPath,remotePath)#执行上传，从本地上传到远程
# sftp.get(remotePath,localPath)#执行下载,从远程下载到本地
# tran.close()