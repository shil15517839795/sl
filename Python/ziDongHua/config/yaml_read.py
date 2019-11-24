#!/usr/bin/python
# -*-coding:utf-8-*-
import yaml
with open(r'E:\shi\Python\ziDongHua\config\a.yaml','r') as file:
    data=yaml.load(file,Loader=yaml.FullLoader)
print(data)
print(data['name'])
print(data['age'])
print(data['wife'])
print(data['wife']['name'])
print(data['wife']['age'])
print(data['child'])
print(data['child'][0]['name'])
print(data['child'][1]['age'])
print(data['child'][2]['name'])
print(data['child'][3]['age'])

# import yaml
# dic={'name':'Tom','age':20}
# print(yaml.dump(dic))#将字典转换为yaml
# list=['name','age']
# print(yaml.dump(list))#将列表转换为yaml