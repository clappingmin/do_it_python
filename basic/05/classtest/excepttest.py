#FileNotFoundError:
#f=open("test.txt","r") #생성되어있는 파일이 없을 경우 오류뜸

#ZeroDivisionError:
#4/0

#IndexError
# li=[1,5,6]
# li[3]

try:
    f=open("test.txt","r") #생성되어있는 파일이 없을 경우 오류뜸
    4/0
    li=[1,5,6]
    li[3]

except IndexError as err:
    print(err) #list index out of range

except FileNotFoundError as err:
    print(err) #No such file or directory

except ZeroDivisionError as err:
    #print(err) #division by zero
    pass #오류가 발생해도 그냥 통과시키고 싶을 때

finally:
    print("finally") #성공하든 안하든 실행