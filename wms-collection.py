# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:41:07 2019

@author: mactone
"""

import serial
import time

#start command解構開始
import re
import numpy as np

ser=0
commum=0

ser=serial.Serial()

def init_Serial():
    ser.baudrate=115200
    ser.port='COM3'
    ser.timeout=10
    ser.open()
    if ser.isOpen():
        print('Open:' +ser.portstr)
        



def decompose(sig,start_position):
    #建立找出+-號的整數
    pattern=re.compile(r'[+-]?\d{1,5}')
    
    sig=list(map(str,sig))
    b=sig[1]
    c=sig[2]
    
    #將b,c字串，依據上述pattern拆解成s, t list
    s=re.findall(pattern,b)
    t=re.findall(pattern,c)
    #
    ##list中的第一個數字並非[]內的，而是amp1f與amp2f，因此把它丟掉
    s.pop(0)
    t.pop(0)
    
    s=list(map(float,s))
    t=list(map(float,t))
    s=np.array(s)
    t=np.array(t)
    
    #找到2f波型peaks點位置
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(t, height=500)   #height=500，代表500以上才找peak
    #plt.plot(t)
    #plt.plot(peaks, t[peaks], "x")
    
    #求出2f peak值所在位置 2f/1f
    wms_peak=s[peaks]/t[peaks]
    print(wms_peak)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(15,8))
    plt.subplot(2,1,1)
    plt.title("1f signal")
    plt.ylim(500,np.max(s)*1.05)
    plt.plot(s,color='blue',linewidth=4)
    plt.vlines(x=peaks, ymin=min(s),ymax=max(s))
    plt.hlines(y=s[peaks],xmin=0,xmax=200)
    plt.text(peaks,s[peaks]*0.95,'2f/1f='+str(wms_peak),fontsize=20)
    
    
    plt.subplot(2,1,2)
    plt.title("2f signal")
    plt.plot(t,color='orange',linewidth=4)
    plt.plot(peaks,t[peaks],"x",linewidth=8)
    plt.vlines(x=peaks, ymin=min(t),ymax=t[peaks])
    plt.text(peaks+5,t[peaks]*0.9,'peak value='+str(t[peaks]),fontsize=20)
    
    print('2f peak value=',t[peaks])
    print('2f/1f @ peak=',wms_peak)

sig=[]
start_position=1    #Signal的第一個開始解析

#for j in range(5): #連續發送5個start
#    print('scan time-'+str(j))
#    for i in range(50):  #一個start指令，會輸出3個byte (start OK, amp1f; i2f)
#        ser.write(b'meas on\r')
#        sig.append(ser.readline())
##        print(sig)
##        print('-----------')
#        time.sleep(5)
#    decompose(sig,start_position)
#    start_position=start_position+3

def meason():
    init_Serial()
    ser.write(b'meas on\r')

def measoff():
    ser.write(b'meas off\r')    
#    print(ser.readlines())
    ser.close()

pattern=re.compile(r'[+-]?\d{1,5}')

sig=[]
meason()
j=0
for i in range(30):
    b=ser.readline()
    if i>0:
        b=str(b,encoding="utf-8")
        run,num=re.findall(pattern,b)
#        print(num)
        if i>3:
            sig.append(num)
            if j>10:
                sig.pop(0)
            j=j+1
            print(i,j,num, max(sig),sig)
    
#for i in range(10):  #一個start指令，會輸出3個byte (start OK, amp1f; i2f)
#    sig.append(ser.readline())
##    print(sig)
#    print('**'+str(i))
#    time.sleep(0.001)
#
#sig2=[]
#for i in range(10):
#    pattern=re.compile(r'[+-]?\d{1,5}')
#    sig=list(map(str,sig))
#    s=re.findall(pattern,sig[i])
#    sig2.append(s)
    
measoff()




