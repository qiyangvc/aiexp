from GeneticAlgTSP import GeneticAlgTSP
import matplotlib.pyplot as plt
j=0
while j<10:
    # filename=input("请输入文件名：")
    # filename="ch71009.tsp"
    filename="dj38.tsp"
    tsp1= GeneticAlgTSP(filename)
    i=0

    m=30000
    while i<100:#手动控制每次输出的最小值，迭代1000次
        # print(tsp1.n)
        tsp1.iterate(1)#这里被改为迭代一次
        # print(tsp1.population)
        if m>tsp1.fits.min():
            m=tsp1.fits.min()
        #这里可以根据最小值查找相应populaition（即路径解法）的下标，比如使用wherearg确定下标
        i+=1
    print(m)
    j+=1
    