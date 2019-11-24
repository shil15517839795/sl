#!/usr/bin/python
# -*-coding:utf-8-*-
# class People():
#     def __init__(self,name):
#         self.name=name  #玩家姓名
#         self.xueLiang0=100 #玩家血量
#         self.gongJiLi0=5  #玩家的攻击力
#         self.xueLiang1=1
#     def __str__(self):     #为了显示的更好看
#         wanjia='-'*30+'\n'
#         wanjia="玩家:"+self.name+"\n"
#         wanjia+="血量:"+str(self.xueLiang0)+"\n"
#         wanjia+="攻击力:"+str(self.gongJiLi0)+"\n"
#         if self.xueLiang1==0:
#             wanjia+='-'*30
#             wanjia+='狗死了，玩家赢了'
#         return wanjia
#     def attack(self,dog):
#         if dog.xueLiang1>0:
#             dog.xueLiang1-=self.gongJiLi0
#         self.xueLiang1=dog.xueLiang1
#         # dog.xueLiang1 -= self.gongJiLi0
#         pass
# class Dog():
#     def __init__(self,name):
#         self.name=name #狗名
#         self.xueLiang1=100  #狗的血量
#         self.gongJiLi1 = 5  #狗的攻击力
#     def __str__(self):
#         gou="狗名："+self.name+"\n"
#         gou+="狗的血量："+str(self.xueLiang1)+"\n"
#         gou+="狗的攻击力："+str(self.gongJiLi1)+"\n"
#         return gou
#     def da(self,people):
#         pass
#         # p1.xueLiang0-=self.gongJiLi1
# p1=People("Tom")
# print(p1)
# dog1=Dog('狂犬')
# print(dog1)


# while 1:
#     p1.attack(dog1)
#     if dog1.xueLiang1==0:
#         break
# print(dog1)
# print(p1)
# while dog1.xueLiang1<=100:
#     p1.attack(dog1)
#     if dog1.xueLiang1==0:
#         print("狗死了")
#         break
#     else:
#         print('继续战斗')
#         print(dog1)

# while p1.xueLiang0<=100:
#     dog1.da(p1)
#     if p1.xueLiang0==0:
#         print('玩家输了')
#         break
#     else:
#         print('继续战斗')
#         print(p1)


