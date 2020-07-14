def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(__name__) #자기가 메인이면 __main__이 출력 다른 곳에서 불리면 위치를 출력함

if __name__=="__main__": #자기가 메인이면 실행되고 다른 곳에서 호출되면 실행되지 않는다.
    print(add(1,4))