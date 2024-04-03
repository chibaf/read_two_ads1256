import ADS1256
from datetime import date
import time
import matplotlib.pyplot as plt
import serial

from read_m52_class import m5logger2
from ads1256b_class import read_ads1256

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="SL_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

ldata0=[0]*10
ldata=[ldata0]*10
ser0 = serial.Serial("/dev/ttyACM0",19200)
ser1 = serial.Serial("/dev/ttyACM1",19200)
ser2 = serial.Serial("/dev/ttyUSB0",19200)
ads1256a=read_ads1256()
ads1256b=read_ads1256()
sport=m5logger2()

data0=[0]*16
data=[data0]*10
data02=[0]*10
data2=[data02]*10

while True:
 try:
  ttime=time.time()-start
  if ttime<0.001:
    ttime=0.0
  st=time.strftime("%Y %b %d %H:%M:%S", time.localtime())
  ss=str(time.time()-int(time.time()))
  rttime=round(ttime,2)
  temp0=ads1256a.read(ser0)
  print(temp0)
  temp1=ads1256b.read(ser1)
  print(temp1)
  if temp0[0]==1.0:
    data1a=temp0[1:]
  else:
    data1a=temp1[1:]
  if temp1[0]==2.0:
    data2a=temp1[1:]
  else:
    data2a=temp0[1:]
#  array=data1.extend(data2)
#  print(data1.extend(data2))
  array=data1a+data2a
  print(array)
  array2=sport.read_logger(ser2)
  print(array2)
#  exit()
  f.write(st+ss[1:5]+","+str(rttime)+","+str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+","+str(array[8])+","+str(array[9])+","+str(array[10])+","+str(array[11])+","+str(array[12])+","+str(array[13])+","+str(array[14])+","+str(array[15])+","+str(array2[0])+","+str(array2[1])+","+str(array2[2])+","+str(array2[3])+","+str(array2[4])+","+str(array2[5])+","+str(array2[6])+","+str(array2[7])+","+str(array2[8])+","+str(array2[9])+"\n")
  print(st+ss[1:5]+","+str(rttime)+","+str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+","+str(array[8])+","+str(array[9])+","+str(array[10])+","+str(array[11])+","+str(array[12])+","+str(array[13])+","+str(array[14])+","+str(array[15])+","+str(array2[0])+","+str(array2[1])+","+str(array2[2])+","+str(array2[3])+","+str(array2[4])+","+str(array2[5])+","+str(array2[6])+","+str(array2[7])+","+str(array2[8])+","+str(array2[9])+"\n")
  data.pop(-1)
  data2.pop(-1)
  data.insert(0,array)
  data2.insert(0,array2)
  rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
  rez2 = [[data2[j][i] for j in range(len(data2))] for i in range(len(data2[0]))]
  x=range(0, 10, 1)
  plt.figure(100)
  plt.clf()
  plt.ylim(-1.0,5.0)
  lin0,=plt.plot(x,rez[0],label="A0")
  lin1,=plt.plot(x,rez[1],label="A1")
  lin2,=plt.plot(x,rez[2],label="A2")
  lin3,=plt.plot(x,rez[3],label="A3")
  lin4,=plt.plot(x,rez[4],label="A4")
  lin5,=plt.plot(x,rez[5],label="A5")
  lin6,=plt.plot(x,rez[6],label="A6")
  lin7,=plt.plot(x,rez[7],label="A7")
  lin8,=plt.plot(x,rez[0],label="A8")
  lin9,=plt.plot(x,rez[1],label="A9")
  lin10,=plt.plot(x,rez[2],label="A10")
  lin11,=plt.plot(x,rez[3],label="A11")
  lin12,=plt.plot(x,rez[4],label="A12")
  lin13,=plt.plot(x,rez[5],label="A13")
  lin14,=plt.plot(x,rez[6],label="A14")
  lin15,=plt.plot(x,rez[7],label="A15")
  plt.legend(handles=[lin0,lin1,lin2,lin3,lin4,lin5,lin6,lin7,lin8,lin9,lin10,lin11,lin12,lin13,lin14,lin15])
  plt.pause(0.1)
  plt.figure(200)
  plt.clf()
  plt.ylim(-25,30)
  tl0,=plt.plot(x,rez2[0],label="T0")
  tl1,=plt.plot(x,rez2[1],label="T1")
  tl2,=plt.plot(x,rez2[2],label="T2")
  tl3,=plt.plot(x,rez2[3],label="T3")
  tl4,=plt.plot(x,rez2[4],label="T4")
  tl5,=plt.plot(x,rez2[5],label="T5")
  tl6,=plt.plot(x,rez2[6],label="T6")
  tl7,=plt.plot(x,rez2[7],label="T7")
  tl8,=plt.plot(x,rez2[8],label="T8")
  tl9,=plt.plot(x,rez2[9],label="T9")
  plt.legend(handles=[tl0,tl1,tl2,tl3,tl4,tl5,tl6,tl7,tl8,tl9])
  plt.pause(0.1)
 except KeyboardInterrupt:
  f.close()
  ser.close()
  exit()
