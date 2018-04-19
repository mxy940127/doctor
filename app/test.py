#Author : mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao

# import numpy
# import random
# count = 0
# serial_a =[]
# serial_b =[]
# for i in range(0,59):
#     count = count + 1
#     number = numpy.random.randint(10000)
#     if number<5000:
#         serial_a.append(number)
#     else:
#         serial_b.append(number)
# print(serial_a)
# print(serial_b)

# from ctypes import *
# from threading import Thread
#
# lib = cdll.LoadLibrary("libdead_loop.so")
# t = Thread(target=lib.DeadLoop)
# t.start()
#
# lib.DeadLoop()