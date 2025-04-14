import copy
import random
import numpy as np


class GeneticAlgTSP:
    n=0
    filename=''
    cities=np.array
    population_size=1000
    population=np.array
    fits=np.array
    def __init__(self,filename):
        #读文件
        self.filename=filename
        with open(filename,'r') as file:
            line= file.readline()
            while line:
                if line[0]=='D':
                    t_l=line.split()
                    self.n=int(t_l[-1])
                    self.cities=np.zeros((self.n,2),dtype = float)
                if line[0]=='1' :
                    i=0
                    while (line !='')&( line!='EOF\n'):
                        t_l=line.split()
                        self.cities[i][0]=float(t_l[1])
                        self.cities[i][1]=float(t_l[2])
                        line=file.readline()
                        i+=1
                line=file.readline()
        # print(self.n,self.cities)
        #初始化种群
        i=0
        self.population=np.zeros((self.population_size,self.n),dtype=int)
        while i<self.population_size:
            self.population[i]=np.random.choice(range(1,self.n+1),self.n,replace=False)
            i+=1
        # print(self.population
    def iterate(self,num_interations):
        i=0

        while i<num_interations:
            self.fits=np.zeros((self.population_size))
            self.fitness()
            self.choose()
            self.cross()
            self.mutate()
            i+=1
    def fitness(self):
        i=0
        while i < self.population_size:
            j=0
            rj1=self.population[i][self.n-1]-1
            rj2=self.population[i][0]-1
            self.fits[i]+=pow(pow(self.cities[rj1][0]-self.cities[rj2][0],2)+pow(self.cities[rj1][1]-self.cities[rj2][1],2),0.5)
            while j<self.n-1:
                rj1=self.population[i][j]-1
                rj2=self.population[i][j+1]-1
                t_distance=pow(pow(self.cities[rj1][0]-self.cities[rj2][0],2)+pow(self.cities[rj1][1]-self.cities[rj2][1],2),0.5) 
                self.fits[i]+=t_distance
                j+=1
            i+=1
    def choose(self):
        fits_sum=np.sum(self.fits)
        fits_rate=np.zeros(self.population_size)
        i=0
        while i<self.population_size:
            fits_rate[i]=fits_sum-self.fits[i]
            i+=1
        t_population=copy.deepcopy(self.population)
        self.population=random.choices(t_population,weights=fits_rate,k=self.population_size)
        # minimum=self.fits
        # mi=np.argwhere(self.fits==minimum)
        # print(mi)
        # self.population[0]=t_population[mi]
        
    def cross(self):
        i=int(self.population_size/2)
        while i>0:
            indexs=random.sample(range(0,self.n),2)
            indexs.sort()
            k1=indexs[0]
            k2=indexs[1]
            changed_part1=self.population[2*i-1][k1:k2]
            changed_part2=[]
            j=0
            k=0
            while j<self.n:
                t_value=self.population[2*i-2][j]
                if t_value in changed_part1:
                    changed_part2.append(t_value)
                    self.population[2*i-2][j]=changed_part1[k]
                    k+=1
                j+=1
            self.population[2*i-1][k1:k2]=changed_part2
            i-=1
    def mutate(self):
        i=0
        while i<self.population_size:
            indexs=random.sample(range(0,self.n),2)
            indexs.sort()
            k1=indexs[0]
            k2=indexs[1]
            self.population[k1:k2]=reversed(self.population[k1:k2])
            i+=1
filename="dj38.tsp"
tsp1= GeneticAlgTSP(filename)
i=0
while i<1000:
    # print(tsp1.n)
    tsp1.iterate(1)
    # print(tsp1.population)
    print(tsp1.fits.min())
    i+=1