prompt = '''----------------------
     커피 자판기 메뉴
   ----------------------
   1. 커피 메뉴 입력
   2. 커피 메뉴 삭제
   3. 커피 자판기
   4. 커피 메뉴판
   5. 종료
   ----------------------'''
menudic ={'coffee':2000}

while True :
    print(prompt)
    menu = input()
    print(menu)
    if menu == '1':
        print("커피메뉴를 추가합니다")
        name = input("메뉴명 >>>")
        price = int(input("가격 >>>"))
        menudic[name]=price
        
        print("{}메뉴는 {:,}원 입니다.".format(name,price));
    
    elif menu == '2':
        print("커피메뉴를 삭제합니다")
        name = input("삭제할 메뉴명 >>>")
        del menudic[name]
        # medic.pop(name)

    elif menu == '3':
        print(menudic)
        money = input("돈을 넣어주세요.")
        choicemenu = input("커피 메뉴를 선택해주세요.")
        if choicemenu not in menudic :    #menudic.get(choicemenu) == None:
            print("메뉴없음")
        else :
             if (menudic[choicemenu]>money):
                print("금액이 부족합니다.")
             else:
                 print("{} 음료가 나옵니다.".format(choicemenu))
                 print("남은 금액 {}원을 받으세요".format(money-menudic[choicemenu]))


    elif menu == '4':
        print("---------------------\n")
        for menu, money in menudic.items():
                print("{} {:,}원".format(menu,money),end=" ")
        print("\n---------------------\n")
           
 
    elif menu == '5':
        print("프로그램 종료")
        break