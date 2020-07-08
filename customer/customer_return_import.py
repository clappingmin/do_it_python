import customer_function

custlist=[]
page = -1

def exe(choice,page):
        if choice=='I':
            customer_function.insertData(page)
        
        elif choice=='C':
            customer_function.curSearch(page)
        
        elif choice=='P':
            page = customer_function.preSearch(page)

        elif choice=='N':
            page = customer_function.nextSearch(page)

        elif choice=='U':
            customer_function.updateData()
        
        elif choice=='D':
            customer_function.deleteData(page)
        
        elif choice=='Q':
            quit()


while True:
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

    exe(choice,page)