import re

class Customer:

    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            I - 고객 정보 입력
            C - 현재 고객 정보 조회
            P - 이전 고객 정보 조회
            N - 다음 고객 정보 조회
            U - 고객 정보 수정
            D - 고객 정보 삭제
            Q - 프로그램 종료
            ''').upper()  
        return choice
    
    def exe(self,choice):
        if choice=='I':
            self.insertData()
            
        elif choice=='C':
            self.curSearch()
        
        elif choice=='P':
            self.preSearch()

        elif choice=='N':
            self.nextSearch()

        elif choice=='U':
            self.updateData()
        
        elif choice=='D':
            self.deleteData()
        
        elif choice=='Q':
            quit()

    def insertData(self): 
        print("고객 정보 입력")
        customer={'name':'','gender':'','email':'','birthyear':''}
        customer['name'] = input("이름을 입력하세요. >>")
    
        while True :
            customer['gender'] = input("사용자 성별을 입력하세요.(f,F/m,M) >>")
            customer['gender']=customer['gender'].upper()
            if customer['gender'] in ('M','F'):
                break

        while True :
            customer['email'] = input("사용자 이메일을 입력하세요. >>")
            while re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', customer['email']) == None :
                print("이메일 형식이 잘못되었습니다. 다시 입력하세요.")
                customer['email'] = input("사용자 이메일을 입력하세요. >>")

            check = 0

            for i in self.custlist:
                if i['email'] == customer['email'] :
                    check = 1
                
            if check == 0:
                break

            print("중복되는 email이 있습니다.")

        while True :
            customer['birthyear'] = input("사용자 출생년도를 입력하세요.(4자리 ex)1997) >>")
            if len(customer['birthyear']) == 4 and customer['birthyear'].isdecimal() :
                customer['birthyear'] = int(customer['birthyear'])
                break
            
            print("입력형식이 맞지 않습니다. 다시 입력해주세요.(4자리 ex)1997) >>")
 
        self.custlist.append(customer)
        self.page += 1
        
    def curSearch(self):
        print("현재 고객 정보 조회")
        if self.page == -1:
            print("아직 입력된 고객 정보가 없습니다.")
        else :
            print("%d장"%(self.page+1),self.custlist[self.page])

    def preSearch(self):
        print("이전 고객 정보 조회")
        if self.page == -1 :
            print("아직 입력된 고객 정보가 없습니다.")
        elif self.page == 0 :
            print("이전 페이지가 없으므로 이동이 불가능합니다.")
            print("%d장"%(self.page+1),self.custlist[self.page])
        else :
            self.page -= 1
            print("%d장"%(self.page+1),self.custlist[self.page])

    def nextSearch(self):
        print("다음 고객 정보 조회")
        if self.page == -1 :
            print("아직 입력된 고객 정보가 없습니다.")
        elif self.page == len(self.custlist)-1 :
            print("현재 페이지가 마지막 장이므로 이동이 불가능합니다.")
            print("%d장"%(self.page+1),self.custlist[self.page])
        else :
            self.page+=1
            print("%d장"%(self.page+1),self.custlist[self.page])

    def deleteData(self):
        print("고객 정보 삭제")

        for i in self.custlist :
            print(i['name'],':',i['email'],end=" ")
        print()

        choice1 = input("삭제하고자 하는 이메일을 입력하세요.")
        delok = 0

        for i in range(0,len(self.custlist)): #range는 0부터 마지막 그전까지
            if self.custlist[i]['email'] == choice1:
                print('{} 고객님의 정보가 삭제되었습니다.'.format(self.custlist[i]['name']))
                del self.custlist[i]
                delok =1
            
            if delok == 1:
                self.page -=1
                break
        
            if delok == 0:
                print("등록되지 않은 이메일입니다.")

            for i in self.custlist :
                print(i['name'],':',i['email'],end=" ")
            print()

    def updateData(self): 
        print("고객 정보 수정")

        for i in self.custlist :
            print(i['name'],':',i['email'],end=" ")
        print()

        choice2 = input("수정하고자 하는 이메일을 입력하세요.")
        idx = -1

        for i in range(0,len(self.custlist)): #range는 0부터 마지막 그전까지
            if self.custlist[i]['email'] == choice2:
                idx = i

            if idx != -1 :
                break
        
        if idx == -1:
            print("사용자를 찾을 수 없습니다. 다시 이메일을 확인해 주세요. ")
        
        else :
            umenu = input("1.이름 수정 2.성별 수정 3.출생년도 수정 ")

            if umenu == '1' :
                print("고객 이름 수정")
                uname = input("수정하고자 하는 이름을 입력하세요. ")
                self.custlist[idx]['name'] = uname

                print("수정 결과")
                print(self.custlist[idx]['name'],':',self.custlist[idx]['email'])

            elif umenu == '2' :
                print("고객 성별 수정")
                ugender = input("수정하고자 하는 성별을 입력하세요. (f,F/m,M) >>")
                ugender=ugender.upper()
                while ugender  not in ('M','F'):
                    print("입력 형식이 틀렸습니다.")
                    ugender = input("수정하고자 하는 성별을 입력하세요. (f,F/m,M) >>")
                    ugender=ugender.upper()

                self.custlist[idx]['gender'] = ugender

                print("수정 결과")
                print(self.custlist[idx]['gender'],':',self.custlist[idx]['email'])

            elif umenu == '3' :
                print("고객 출생년도 수정")
                ubirthyear = input("수정하고자 하는 출생년도를 입력하세요. ")

                while len(ubirthyear) != 4 and ubirthyear.isdecimal() == False :
                    print("입력 형식이 틀렸습니다.")
                    ubirthyear = input("수정하고자 하는 출생년도를 입력하세요. ")
    
                ubirthyear = int(ubirthyear)
                self.custlist[idx]['birthyear'] = ubirthyear

                print("수정 결과")
                print(self.custlist[idx]['birthyear'],':',self.custlist[idx]['email'])

    def __init__(self):
        self.custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthyear': 2000},
            {'name': '김길동', 'gender': 'M', 'email': 'kims1@gmail.com', 'birthyear': 2010},
            {'name': '박나리', 'gender': 'F', 'email': 'park1@gmail.com', 'birthyear': 1999},
            {'name': '김철수', 'gender': 'M', 'email': 'kim00@gmail.com', 'birthyear': 1988}]
        self.page = 3

        while True: #무한루프
            self.exe(self.firstinput())

Customer()
