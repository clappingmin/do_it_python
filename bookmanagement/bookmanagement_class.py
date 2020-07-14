import string, re

class Bookmanagement:
    booklist=[]

    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            I - 도서 정보 등록
            T - 전체 도서 목록
            U - 도서 정보 수정
            D - 도서 정보 삭제
            Q - 프로그램 종료
            ''').upper()
        return choice
    
    def exe(self,choice):
        if choice=='I':
            self.insertData()
        
        elif choice=='T':
            self.totalSearch()
        
        elif choice=='U':
            self.updateData()
        
        elif choice=='D':
            self.deleteData()
        
        elif choice=='Q':
            quit()

    def insertData(self): 
        print("도서 정보 등록")
    
        book={'num':'','title':'','house':'','author':'','explain':'','stok':''}

        while True :
            check = 0
            book['num'] = input("책번호를 입력하세요. >>")
                
            for i in self.booklist:
                if i['num'] == book['num'] : 
                    check = 1
                
            if check == 0:
                break

            print("중복되는 책번호가 있습니다.")

        book['title'] = input("책제목을 입력하세요. >>")
        
        book['house'] = input("출판사를 입력하세요. >>")
        
        book['author'] = input("저자를 입력하세요. >>")
            
        book['explain'] = input("메모를 입력하세요. >>")
            
        stok = input("재고를 입력하세요. >>")
        while stok.isdecimal() == False or int(stok) < 0 :
            print("입력 형식이 틀렸습니다.")
            stok = input("재고를 입력하세요. >>")
        book['stok'] = int(stok)


        self.booklist.append(book) 

    def totalSearch(self):
        print("전체 도서 목록")
        for i in range(len(self.booklist)):
            print(self.booklist[i])

    def deleteData(self):
        print("도서 정보 삭제")

        for i in self.booklist :
            print(i['num'],':',i['title'],end=" ")
        print()

        choice1 = input("삭제하고자 하는 도서의 번호를 입력하세요.")
        delok = 0

        for i in range(0,len(self.booklist)): #range는 0부터 마지막 그전까지
            if self.booklist[i]['num'] == choice1:
                print('{} 도서의 정보가 삭제되었습니다.'.format(self.booklist[i]['title']))
                del self.booklist[i]
                delok =1
                
            if delok == 1:
                break
            
        if delok == 0:
            print("등록되지 않은 도서의 번호입니다.")

        for i in self.booklist :
            print(i['num'],':',i['title'],end=" ")
        print()
    
    def updateData(self):
        print("도서 정보 수정")

        for i in self.booklist :
            print(i['num'],':',i['title'],end=" ")
        print()

        choice2 = input("수정하고자 하는 도서의 번호를 입력하세요.")
        idx = -1

        for i in range(0,len(self.booklist)): #range는 0부터 마지막 그전까지
            if self.booklist[i]['num'] == choice2:
                idx = i
            if idx != -1 :
                break
            
        if idx == -1:
            print("도서를 찾을 수 없습니다. 도서 번호를 확인해 주세요. ")
            
        else :
            umenu = input("1.제목 수정 2.출판사 수정 3.저자 수정 4.설명 수정 5. 재고 수정 ")

            if umenu == '1' :
                print("도서 제목 수정")
                self.booklist[idx]['title'] = input("수정하고자 하는 제목을 입력하세요. ")

                print("수정 결과")
                print(self.booklist[idx]['num'],':',self.booklist[idx]['title'])

            elif umenu == '2' :
                print("도서 출판사 수정")
                self.booklist[idx]['house'] = input("수정하고자 하는 출판사를 입력하세요. ")

                print("수정 결과")
                print(self.booklist[idx]['num'],':',self.booklist[idx]['house'])

            elif umenu == '3' :
                print("도서 저자 수정")
                self.booklist[idx]['author'] =input("수정하고자 하는 저자를 입력하세요. ")

                print("수정 결과")
                print(self.booklist[idx]['num'],':',self.booklist[idx]['author'])

            elif umenu == '4' :
                print("도서 설명 수정")
                self.booklist[idx]['explain'] =input("수정하고자 하는 설명을 입력하세요. ")

                print("수정 결과")
                print(self.booklist[idx]['num'],':',self.booklist[idx]['explain'])

            elif umenu == '5' :
                print("도서 재고 수정")
                ustok =input("수정하고자 하는 재고를 입력하세요. ")

                while ustok.isdecimal() == False and ustok < 0 :
                    print("입력 형식이 틀렸습니다.")
                    ustok = input("재고를 입력하세요. >>")
                        
                self.booklist[idx]['stok'] = int(ustok)

                print("수정 결과")
                print(self.booklist[idx]['num'],':',self.booklist[idx]['stok'])

    def __init__(self):
        self.booklist=[]
        while True: #무한루프
            self.exe(self.firstinput())

Bookmanagement()