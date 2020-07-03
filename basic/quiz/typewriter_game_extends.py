import random,time,json

animal_en = ['horse','monkey','lion','tiger','leopard','giraffe','hippopotamus','snake']


while True:
    print("1.타자게임 2.문제불러오기 3.문제저장하기 4.새문제 등록 5.등수 6.종료")
    menu = input("메뉴를 선택하세요.\n")

    if menu == '1' :
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

    elif menu == '2':
        f = open('./basic/quiz/word.json','rt')
        w = json.load(f)
        f.close()
        print(w)

    elif menu == '3':
        f = open('./basic/quiz/word.json','wt')
        json.dump(animal_en,f,indent=4)
        f.close()

    elif menu =='4':
        pass

    elif menu =='5':
        pass

    elif menu == '6':
        pass
    
    else:
        print("메뉴를 잘못 선택하셨습니다.")