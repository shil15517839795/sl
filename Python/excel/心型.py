#!/usr/bin/python
# -*-coding:utf-8-*-
txt=open('b.txt','w',encoding='utf8')
q = '高含月  '  #必须加起来有8格
txt.write(' '*8)    #中文一个字两格
txt.write(f'{q}'*1)
txt.write(' '*16)
txt.write(f'{q}'*1)
txt.write('\n')
txt.write(' '*4)
txt.write(f'{q}'*2)
txt.write(' '*8)
txt.write(f'{q}'*2)
txt.write('\n')
txt.write(f'{q}'*6)
txt.write('\n')
txt.write(f'{q}'*6)
txt.write('\n')
for a in range(6):
    txt.write(' ' * (a*4))
    txt.write(f'{q}' * (6-a))
    txt.write('\n')
# txt.close()
#





# txt=open('b.txt','w',encoding='utf8')
q = 'LSF   '  #必须加起来有6格
txt.write(' '*9)
txt.write(f'{q}'*2)
txt.write(' '*18)
txt.write(f'{q}'*2)
txt.write('\n')
txt.write(' '*6)
txt.write(f'{q}'*3)
txt.write(' '*12)
txt.write(f'{q}'*3)
txt.write('\n')
txt.write(' '*3)
txt.write(f'{q}'*4)
txt.write(' '*6)
txt.write(f'{q}'*4)
txt.write('\n')
for a in range(10):
    txt.write(' ' * (a*3))
    txt.write(f'{q}' * (10-a))
    txt.write('\n')
txt.close()