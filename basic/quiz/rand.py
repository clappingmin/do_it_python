import random, time

print(random.randint(1,50))

oper=['+','-','*','/']

input("엔터시 게임시작")
start = time.time()
for x in range(0,3):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)
    quiz=str(a)+op+str(b)
    print(quiz,'=')

    c=int(input('정답 ='))

    if int(eval(quiz)) == c:
        print("정답!!")
        count+=1
    else:
        print("오답!")

end = time.time()

print("차이 : ",int(abs(end-start)),"초" )
print("%d개 맞음"%count)
