import time, random

animal_en = ['horse','monkey','lion','tiger','leopard','giraffe','hippopotamus','snake']
aq = 0
wrong = 0

input("엔터시 게임시작")
start = time.time()

for x in range(0,3):
    tmp = False
    num = random.randint(0,8)
    print()
    print(animal_en[num])
    answer = input()
    
    if(answer == animal_en[num]):
        aq+=1
        tmp = True
    
    else:
        while(tmp == False):
            print("틀렸습니다. 다시 적어 주세요.")
            wrong+=1
            print(animal_en[num])
            answer = input()

            if(answer == animal_en[num]):
                aq+=1
                tmp = True


end = time.time()

print("틀린 횟수 :", wrong)
print("타자 시간 : {:.0f}초".format(end-start))

