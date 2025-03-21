class StuData():
    data=[]
    def __init__(self):
        filename='student_data.txt'
        file_object=open(filename,'r') 
        
        while True:
            line=file_object.readline()
            if not line :
                break
            lt=line.split()
            lt[3]=int(lt[3])
            print (lt)
            self.data.append(lt)
        file_object.close
        # self.name=name
        # self.stu_num=stu_num
        # self.gender=gender
        # self.age=age
    def AddData(self,**student_info):
        t=[]
        for dat in student_info:
            t.append(student_info[dat])
        self.data.append(t)
    def SortData(self,str):
        def mycmp(x) :
            if str=='name':             #python疑似有点太自由了
                return x[0]
            elif str=='stu_num':
                return x[1]
            elif str=='gender':
                return x[2]
            elif str=="age":
                return x[3]
        # def tkname(elem) :
        #     return elem[0]
        # def tksn(elem) :
        #     return elem[1]
        # def tkgdr(elem) :
        #     return elem[2]
        # def tkage(elem) :
        #     return elem[3]
        # if str=='name':
        #     self.data.sort(key=tkname)
        # elif str=='stu_num':
        #     self.data.sort(key=tksn)
        # elif str=='gender':
        #     self.data.sort(key=tkgdr)
        # elif str=="age":
        #     self.data.sort(key=tkage)
        self.data.sort(key=mycmp)
    def ExportFile(self,filename):
        i=0
        with open(filename,'w') as file_object:
            while i<len(self.data):
                j=0
                while j<len(self.data[i]):
                    file_object.write(str(self.data[i][j]))
                    file_object.write(" ")
                    j+=1
                # file_object.write(self.data[i][0])
                # file_object.write(" ")
                # file_object.write(self.data[i][1])
                # file_object.write(" ")
                # file_object.write(self.data[i][2])
                # file_object.write(" ")
                # file_object.write(str(self.data[i][3]))
                file_object.write("\n")
                i+=1
d = StuData()
d.AddData(name="Bob",stu_num="003",gender="M",age=20)
print(d.data)
d.SortData('name')
print(d.data)
d.ExportFile('new_stu_data.txt')