# coding=utf-8
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值
'''
#from random import randint

#a=randint(0,9)
#a=3
#t=int(raw_input ("请输入一个数字:"))
# s=[]
# b=0
# for i in range(1,t+1):
#     for j in range(i):
#         print a * 10 ** (i - j)
Tn = 0
Sn = []
n = int(raw_input('n = '))
a = int(raw_input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn







