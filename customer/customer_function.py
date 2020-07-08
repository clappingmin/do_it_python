import re
custlist=[]
page = -1

def insertData(page):
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

        for i in custlist:
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
 
    custlist.append(customer)
    page += 1
    return page
  
def curSearch(page):
    print("현재 고객 정보 조회")
    if page == -1:
        print("아직 입력된 고객 정보가 없습니다.")
    else :
        print("%d장"%(page+1),custlist[page])

def preSearch(page):
    print("이전 고객 정보 조회")
    if page == -1 :
        print("아직 입력된 고객 정보가 없습니다.")
    elif page == 0 :
        print("이전 페이지가 없으므로 이동이 불가능합니다.")
        print("%d장"%(page+1),custlist[page])
    else :
        page -= 1
        print("%d장"%(page+1),custlist[page])
    
    return page
        
def nextSearch(page):
    print("다음 고객 정보 조회")
    if page == -1 :
        print("아직 입력된 고객 정보가 없습니다.")
    elif page == len(custlist)-1 :
        print("현재 페이지가 마지막 장이므로 이동이 불가능합니다.")
        print("%d장"%(page+1),custlist[page])
    else :
        page+=1
        print("%d장"%(page+1),custlist[page])

    return page

def deleteData(page):
    print("고객 정보 삭제")

    for i in custlist :
        print(i['name'],':',i['email'],end=" ")
    print()

    choice1 = input("삭제하고자 하는 이메일을 입력하세요.")
    delok = 0

    for i in range(0,len(custlist)): #range는 0부터 마지막 그전까지
        if custlist[i]['email'] == choice1:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            delok =1
            
        if delok == 1:
            page -=1
            break
        
        if delok == 0:
            print("등록되지 않은 이메일입니다.")

        for i in custlist :
            print(i['name'],':',i['email'],end=" ")
        print()
    
    return page

def updateData(): 
    print("고객 정보 수정")

    for i in custlist :
        print(i['name'],':',i['email'],end=" ")
    print()

    choice2 = input("수정하고자 하는 이메일을 입력하세요.")
    idx = -1

    for i in range(0,len(custlist)): #range는 0부터 마지막 그전까지
        if custlist[i]['email'] == choice2:
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
            custlist[idx]['name'] = uname

            print("수정 결과")
            print(custlist[idx]['name'],':',custlist[idx]['email'])

        elif umenu == '2' :
            print("고객 성별 수정")
            ugender = input("수정하고자 하는 성별을 입력하세요. (f,F/m,M) >>")
            ugender=ugender.upper()
            while ugender  not in ('M','F'):
                print("입력 형식이 틀렸습니다.")
                ugender = input("수정하고자 하는 성별을 입력하세요. (f,F/m,M) >>")
                ugender=ugender.upper()

            custlist[idx]['gender'] = ugender

            print("수정 결과")
            print(custlist[idx]['gender'],':',custlist[idx]['email'])

        elif umenu == '3' :
            print("고객 출생년도 수정")
            ubirthyear = input("수정하고자 하는 출생년도를 입력하세요. ")

            while len(ubirthyear) != 4 and ubirthyear.isdecimal() == False :
                print("입력 형식이 틀렸습니다.")
                ubirthyear = input("수정하고자 하는 출생년도를 입력하세요. ")
    
            ubirthyear = int(ubirthyear)
            custlist[idx]['birthyear'] = ubirthyear

            print("수정 결과")
            print(custlist[idx]['birthyear'],':',custlist[idx]['email'])

