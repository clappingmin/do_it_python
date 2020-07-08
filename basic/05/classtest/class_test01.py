class Cookie:
    pass

a=Cookie()

print(type(a))

class FourCal:
    mode=1
    def __init__(self,first,second):
        self.first = first
        self.second = second
        print("생성자")

    def setdata(self, first, second): #첫번째는 무조건 self
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result

# a = FourCal()
b=FourCal(4,7)
# c=FourCal()

print(FourCal.mode)
print(id(FourCal.mode))


