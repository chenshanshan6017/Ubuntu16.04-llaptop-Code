#!/usr/bin/python2
#-*-coding:utf-8-*-
import numpy as np
import scipy.io as sio
import calendar
from mysupport import *
import MyPackge
import sys

print("xiao")
print np.zeros([10, 10])
MD_contends = sio.loadmat('./Data/MD/all_md.mat')
matlab_contends = sio.loadmat('./matlab.mat')
print(sio.whosmat('./matlab.mat'))
print (MD_contends['A'])
print(matlab_contends)
B = [[1, 2, 3], [4.5, 5, 6], [7, 8, 9]]
print(B[0:2][0])

sio.savemat("pythonGen.mat", {'Bmat': B})
#use calendar
strCal = '\n\n' + calendar.month(2018, 5)
print(strCal)
print(calendar.weekday(2018, 5, 21))

#use support.py function
printStr("xiaogongwei")
#class1
my_class = myClass("calss1")
my_class.printClassName()
print(myClass.__dict__)
print(getattr(myClass, 'm_class_name'))
print(my_class.m_class_name)
del my_class

#class2
my_class2 = myClass2()
my_class2.printClassName()
my_class2.printClassName2()
print(myClass2.__dict__)
print(getattr(myClass2, 'm_class_name'))
del my_class2


#use package: MyPackage
MyPackge.Pots2()
#sys.path.append(".")
print(sys.path)
#print(raw_input("david,please input sth :"))

with open('david.log', 'w') as fid:
    for i in range(1, 10):
        fid.write('xiaogongwei10->{0}{1}{0}\n'.format(' xiao->', i))


