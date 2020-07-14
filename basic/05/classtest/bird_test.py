#오류 일부러 발생시키기 P.227
class Bird:
    def fly(self):
        raise NotImplementedError

# b=Bird()
# b.fly() #오류가 난닻

class B(Bird): #Bird를 상속받는 B
    def fly(self):
        print("bird fly")

b1=B()
b1.fly() #오버라이딩은 오류가 안난다

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    def __init__(self):
        print("바보 안됨")

    if nick =='바보':
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

try:
    say_nick("바보")
except MyError as err:
    print(err)