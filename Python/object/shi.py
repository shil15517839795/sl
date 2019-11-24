#!/usr/bin/python
# -*-coding:utf-8-*-
#创建一个类
# class Dog():
    # 属性
    #方法
    # def run(self):
    #     print("---跑---")
    # def pee(self):
    #     print("---撒尿---")
    # def info(self):
    #     self.pee()
    #     print(self.color)
    #     print(self.sex)
    #     print(self.name)
    #     print(self.tuiCount)

#创建一个叫做大狗的对象
# bigDog=Dog()
# bigDog.name="大狗"
# print(bigDog.name)
# bigDog.color="黄色"
# bigDog.sex="公"
# bigDog.tuiCount="3"
# bigDog.info()
# print(bigDog.color)
# print(bigDog.sex)
# bigDog.run()
# bigDog.pee()
#创建一个黑狗的对象
# blackDog=Dog()
# blackDog.pee()
# blackDog.run()
# blackDog.name="狗"
# print(blackDog.name)
# blackDog.color="黑色"
# blackDog.sex="公"
# blackDog.tuiCount="4"
# blackDog.info()
# print(blackDog.color)
# print(blackDog.sex)








#继承
# class Lei():
#     a='fdafas'
#     def hanshu111(self):
#         pass
#     def hanshu(self):
#         self.hanshu111()
#         print(self.a)
# class Dog:
#     def call(self):
#         print("---汪汪---")
# class newLei(Lei,Dog):
#     pass
# class newnewLei(newLei):
#     def shi(self):
#         print("嘻嘻")
#         def lei():
#             print("--xiaoxiao--")
#         return lei
# xiaoming=newLei()
# xiaozhang=newnewLei()
# xiaoming.hanshu()
# xiaoming.hanshu111()
# xiaoming.call()
# xiaozhang.call()
# xiaozhang.shi()()


#函数方法重写
# class Lei():
#     a='fdafas'
#     def hanshu111(self):
#         pass
#     def hanshu(self):
#         self.hanshu111()
#         print(self.a)
# class Shi(Lei):
#     def aaa(self):
#         self.hanshu()
#     def hanshu(self):
#       print("dlfkas")
# a = Shi()
# a.hanshu()


#多态
import abc
# class Animal(metaclass=abc.ABCMeta):
    # @abc.abstractmethod
#     def talk(self):
#         pass
# class People(Animal):
#     def talk(self):
#         print("你好世界！")
# class Pig(Animal):
#     def talk(self):
#         print("哼哼")
# class Dog(Animal):
#     def talk(self):
#         print("汪汪")
# def func(obj):
#     obj.talk()
# func(Pig())


#专有方法
# class Dog():
#     def __init__(self,color,weiba):
#         self.color=color
#         self.weiba=weiba
#         print(self.color)
#         print(self.weiba)
#     def pee(self):
#         print("--撒尿--")
# daDog=Dog('黄色','有尾巴')
# daDog.pee()


# 打印出第一大和第二大的数
# a =[32,65,78,34,78,65,12,78,65]
# a.sort(reverse=True)
# for i in a:
#     if i<a[0]:
#         b = i
#         break
# for j in a :
#     if j==a[0] or j == b:
#         print(j,end='\t')