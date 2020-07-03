# f = open("test.txt",'w',encoding='UTF-8')
# f.write("txt파일 생성")
# f.close()  #전체 주석 :ctrl+/

#f = open("test.txt", 'r', encoding='UTF8')

f=open("./basic/quiz/test.txt",'r',encoding='UTF8')
line ="a"
while line :
    line = f.readline() #한줄 readlines() : list로 한줄씩 다 저장 read: txt로 한꺼번에 다 읽어옴
    print(type(line))
    print(line)

f.close()