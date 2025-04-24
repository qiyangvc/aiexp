from GeneticAlgTSP import GeneticAlgTSP
import matplotlib.pyplot as plt
import numpy as np
# filename=input("请输入文件名：")
# filename="ch71009.tsp"
filename="dj38.tsp"
tsp1= GeneticAlgTSP(filename)
i=0
tm=0
m=[]
x=[]
y=[]

tt=0
while i<1000:#手动控制每次输出的最小值，迭代100次
    # print(tsp1.n)
    tsp1.iterate(1)#这里被改为迭代一次
    # print(tsp1.population)
    tm=tsp1.fits.min()
    ti=np.argwhere(tsp1.fits==tm)
    tt=ti[0][0]
    print(tsp1.population[tt])
    m.append(tm)    
    #这里可以根据最小值查找相应populaition（即路径解法）的下标，比如使用argwhere确定下标
    i+=1
print(m)
j=0

while j<tsp1.n:
    tj=tsp1.population[tt][j]-1
    x.append(tsp1.cities[tj][0])
    y.append(tsp1.cities[tj][1])
    j+=1
# xs=np.linspace(1,100,100)
# plt.plot(xs,m)
plt.plot(x,y)
plt.plot(x,y,'o',label='data point')
plt.show()



    