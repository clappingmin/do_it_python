import string, re

booklist=[]
page=-1


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 도서 정보 등록
    T - 전체 도서 목록
    U - 도서 정보 수정
    D - 도서 정보 삭제
    Q - 프로그램 종료
    ''')  

    if choice=="I":        
        print("도서 정보 등록")

        book={'num':'','title':'','house':'','author':'','explain':'','stok':''}

        while True :
            check = 0
            book['num'] = input("책번호를 입력하세요. >>")
            
            for i in booklist:
                if i['num'] == book['num'] : 
                    check = 1
            
            if check == 0:
                break

            print("중복되는 책번호가 있습니다.")

        book['title'] = input("책제목을 입력하세요. >>")
       
        book['house'] = input("출판사를 입력하세요. >>")
       
        book['author'] = input("저자를 입력하세요. >>")
        
        book['expain'] = input("메모를 입력하세요. >>")
        
        stok = input("재고를 입력하세요. >>")
        while stok.isdecimal() == False or int(stok) < 0 :
            print("입력 형식이 틀렸습니다.")
            stok = input("재고를 입력하세요. >>")
        book['stok'] = int(stok)


        booklist.append(book)
        page+=1

    elif choice == 'T':
        print("전체 도서 목록")
        for i in range(len(booklist)):
            print(booklist[i])

    elif choice=='D':
        print("도서 정보 삭제")

        for i in booklist :
            print(i['num'],':',i['title'],end=" ")
        print()

        choice1 = input("삭제하고자 하는 도서의 번호를 입력하세요.")
        delok = 0

        for i in range(0,len(booklist)): #range는 0부터 마지막 그전까지
            if booklist[i]['num'] == choice1:
                print('{} 도서의 정보가 삭제되었습니다.'.format(booklist[i]['title']))
                del booklist[i]
                delok =1
            
            if delok == 1:
                break
        
        if delok == 0:
            print("등록되지 않은 도서의 번호입니다.")

        for i in booklist :
            print(i['num'],':',i['title'],end=" ")
        print()

    elif choice=="U": 
        print("도서 정보 수정")

        for i in booklist :
            print(i['num'],':',i['title'],end=" ")
        print()

        choice2 = input("수정하고자 하는 도서의 번호를 입력하세요.")
        idx = -1

        for i in range(0,len(booklist)): #range는 0부터 마지막 그전까지
            if booklist[i]['num'] == choice2:
                idx = i
            if idx != -1 :
                break
        
        if idx == -1:
            print("도서를 찾을 수 없습니다. 도서 번호를 확인해 주세요. ")
        
        else :
            umenu = input("1.제목 수정 2.출판사 수정 3.저자 수정 4.설명 수정 5. 재고 수정 ")

            if umenu == '1' :
                print("도서 제목 수정")
                booklist[idx]['title'] = input("수정하고자 하는 제목을 입력하세요. ")

                print("수정 결과")
                print(booklist[idx]['num'],':',booklist[idx]['title'])

            elif umenu == '2' :
                print("도서 출판사 수정")
                booklist[idx]['house'] = input("수정하고자 하는 출판사를 입력하세요. ")

                print("수정 결과")
                print(booklist[idx]['num'],':',booklist[idx]['house'])

            elif umenu == '3' :
                print("도서 저자 수정")
                booklist[idx]['author'] =input("수정하고자 하는 저자를 입력하세요. ")

                print("수정 결과")
                print(booklist[idx]['num'],':',booklist[idx]['author'])

            elif umenu == '4' :
                print("도서 설명 수정")
                booklist[idx]['explain'] =input("수정하고자 하는 설명을 입력하세요. ")

                print("수정 결과")
                print(booklist[idx]['num'],':',booklist[idx]['explain'])

            elif umenu == '5' :
                print("도서 재고 수정")
                ustok =input("수정하고자 하는 재고를 입력하세요. ")

                while ustok.isdecimal() == False and stok < 0 :
                    print("입력 형식이 틀렸습니다.")
                    stok = input("재고를 입력하세요. >>")
                    
                book['stok'] = int(stok)

                print("수정 결과")
                print(booklist[idx]['num'],':',booklist[idx]['stok'])

    elif choice=="Q":
        print("프로그램 종료")
        break

