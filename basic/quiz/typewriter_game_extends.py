import random,time,json

animal_en = ['horse','monkey','lion','tiger','leopard','giraffe','hippopotamus','snake']
#rank={} #등수값을 저장할 딕셔너리

# def sortV(x) :
#     retrun x[1]

with open('./basic/quiz/rank.json','rt') as f:
    rank = json.load(f)
        


while True:
    print("1.타자게임 2.문제불러오기 3.문제저장하기 4.새문제 등록 5.등수 6.종료")
    menu = input("메뉴를 선택하세요.\n")

    if menu == '1' : #타자게임
        aq = 0
        wrong = 0
        
        input("엔터시 게임시작")
        start = time.time()

        for x in range(0,3):
            tmp = False
            q = random.choice(animal_en)
            print()
            print(q)
            answer = input()
            
            if(answer == q):
                aq+=1
                tmp = True
                
            else:
                while(tmp == False):
                    print("틀렸습니다. 다시 적어 주세요.")
                    wrong+=1
                    print(q)
                    answer = input()
                    
                    if(answer == q):
                        aq+=1
                        tmp = True
                        
        end = time.time()
        print("틀린 횟수 :", wrong)
        print("타자 시간 : {:.0f}초".format(end-start))
        name = input("사용자 이름을 입력하세요. ")
        rank[name] = float(end-start)

    elif menu == '2': #문제 불러오기
        f = open('./basic/quiz/word.json','rt')
        w = json.load(f)
        f.close()
        print(w)

    elif menu == '3': #문제 저장하기
        f = open('./basic/quiz/word.json','wt')
        json.dump(animal_en,f,indent=4)
        f.close()

    elif menu =='4': #새문제 등록
        menu = input("1.등록 2.수정 3.삭제")
        if menu == '1' :
            print(animal_en)
            quiz = input('문제 입력 ')
            animal_en.append(quiz)
            print(animal_en)
        elif menu == '2' :
            print(animal_en)
            quiz = input("어떤 문제를 수정하나요? ")
            index = animal_en.index(quiz)
            quiz = input("수정 내용 ")
            animal_en[index]=quiz

        elif menu == '3':
            print(animal_en)
            quiz=input('문제 입력 ')
            animal_en.remove(quiz)
            print(animal_en)

    elif menu =='5': #등수보기

        ranklist = sorted(rank.items(),key=lambda x: x[1])
        num = 1
        for k,v in ranklist :
            print("%d등 %s %.0f초" %(num,k,v))
            num = num+1


    elif menu == '6': #종료
        break
    
    else:
        print("메뉴를 잘못 선택하셨습니다.")

with open('./basic/quiz/rank.json','wt') as f:
    json.dump(rank,f,indent=4) #indent : 들여쓰기 줄바꿈 해줌