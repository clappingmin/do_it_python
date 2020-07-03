import pickle #python 내에서 파일 주고 받기에는 좋으나 다른 곳에 주고 받기에는 힘듬 그래서 보통 json 사용

data = {1:'python',2:'you need'}
#type dict
print(type(data))

f = open("test.pickle",'wb')
pickle.dump(data,f)
f.close()


#파일로 저장
with open("test.pickle",'wb') as f: #with을 쓰면 블록 끝날 때 알아서 close해준다.
    pickle.dump(data,f) #저장할 때 dump

# #파이썬 내에서 사용 바이트 형태
# datab=pickle.dumps(data)
# print(type(datab))

#파일을 읽어옴
with open("test.pickle",'rb') as f:
    data =pickle.load(f) #읽어올 때 dump
    print(data)
    print(type(data))