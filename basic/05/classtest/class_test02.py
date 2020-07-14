class Person:
    cnt = 0 #클래스 변수
    def __init__(self,name,age=1):
        self.name=name
        self.__age=age #프라이빗
        Person.cnt +=1
        print(self.name+'('+str(self.__age)+") is initialize")

    def work(self,company):
        print(self.name+'is strong in'+company)
        self.__getage()
    
    def sleep(self):
        print(self.name+'is sleeping')
    
    def __getage(self):
        print(self.__age)

    @classmethod
    def getcount(cls):
        return cls.cnt


obj1 = Person("hong")

print(obj1.name)