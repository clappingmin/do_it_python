import bookmanagement_function

def exe(choice):
        if choice=='I':
            bookmanagement_function.insertData()
        
        elif choice=='T':
            bookmanagement_function.totalSearch()
        
        elif choice=='U':
            bookmanagement_function.updateData()
        
        elif choice=='D':
            bookmanagement_function.deleteData()
        
        elif choice=='Q':
            quit()


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 도서 정보 등록
    T - 전체 도서 목록
    U - 도서 정보 수정
    D - 도서 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    exe(choice)