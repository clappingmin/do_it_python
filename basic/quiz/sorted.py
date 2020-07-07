
myList = [4,1,3,5,6]
myList.sort()
print(myList)


myDic ={1:1,3:3,2:2}
#myDic.sort() dictionary는 sort없음 -> sorted를 사용하자
print(myDic)

print(sorted("hello", reverse=True))

#list
sorted([5,6,1,2,9,7,4])
#sorted([2,1,3],[3,2,1],[1,2,3])

#set
sorted({3,2,1})

#tuple
sorted((3,2,1))

#value값을 기준으로 정렬? sorted함수의 파라메터인 key를 이용
#dict
myDic = {3:1,2:3,1:4}

#[(3,1), (2,3),(1,4)]
sorted(myDic.items(),key=lambda x: x[1]) #두번째 있는 값으로 정렬하겠다.
                                         #딕셔너리를 한쌍으로 들어갈 수 있게 items()
                                         #비교 함수는 익명 함수(lambda)
                                         #복수개를 가지고 있을 때 사용

print(sorted(['bac','abc','python'],key=lambda x: x[1],reverse=True)) #두번째 있는 값으로 정렬하겠다.
                                                               #내림차순 : reverse = True