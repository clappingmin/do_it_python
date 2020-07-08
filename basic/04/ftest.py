def add_and_mul(a,b):
    return a+b,a*b  #return이 여러 개면 알아서 tuple로 묶어서 반환해준다.

result = add_and_mul(3,4)
print(type(result)) #tuple

print(result) #tuple로 묶어서 반환

add,mul = add_and_mul(3,4)

print(add) #7

print(3,5,6,7,8,9, sep="," ) #sep로 설정안하면 숫자 사이에 공백이 들어감


def say_myself(name,old, man=True,*addr): #초기값을 미리 설정해놓으면
    print("나의 이름은",name,"입니다.")    #안넣어도 초기값으로 설정된다.
    print("나이는",old,"살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
    for i in addr:
        print (i)

say_myself("박수민",24,False,"대구","서울","부산") #man값 안넣어도 초기값 True를 받음

#---------------------------------------------------#
a=1

def vartest(a):
    a=a+1
    print(a) #2
    return(a)

a=vartest(a)
print(a) #return 없으면 1 있으니 2

#global은 바깥쪽 변수를 같이 쓰는거니 매개변수,return 필요없음
#함수는 독립적인게 좋으니 가급적 사용피하기
def vartest2():
    global a
    a=a+1
    print(a)

vartest2()
print(a)


