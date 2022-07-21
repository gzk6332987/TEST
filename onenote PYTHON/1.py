# -*- coding:utf-8 -*-
# author: Song Bo, Eagle, ZJU
# email: sbo@zju.edu.cn
s1 = '我是一个长句子，是的很长的句子。'
s2 = '我是短句子'

print('{:>30}'.format(s1) + '{:>60}'.format((s2)))
print('{:>30}'.format(s2) + '{:>60}'.format((s1)))

print(len(s1))