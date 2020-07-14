#상속 p202

class FourCal:
    def __init__(self,first=1,second=4):
        self.first = first
        self.second = second
        print("생성자")

    def setdata(self, first, second): #첫번째는 무조건 self
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
###########################################
class MoreFourCal(FourCal): #상속받을 클래스
    def pow(self):
        result = self.first ** self.second
        return result
    
    def div(self): #오버라이딩
        if self.second ==0:
            return 0
        else:
            return self.first/self.second

cal1 = MoreFourCal() #기본값이 들어감 1,4
cal2=MoreFourCal(5,6)

print(cal1.add())
print(cal2.add())
print(cal1.pow())
print(cal2.pow()) #5의 6제곱

print(cal1.div())