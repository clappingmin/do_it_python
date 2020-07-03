str1="abcdefgh"
list1=[1,2,3,4,5,6]
tuple1=(1,2,3,4,5,6)
dic1={1:"첫번째",2:"두번째"}
set1={1,2,3,4}

for i in list1:
    print(i,end=",") #end ="" : 줄바꿈

for k,v in dic1.items(): #딕셔너리에서 같이 가져올 때 :items()사용 튜플로 받아옴
    print(k,v)

for i in range(10): #0~9
    print(i)

for i in range(1,10): #1~9
    print(i)


for i in range (2,10) :
    print("\n--[%d단]--"%i)
    for j in range (1, 10) :
        print("%d * %d = %2d"%(i,j,i*j))
print("---------")

for x in range(1,10):
    for y in range (2,10):
        print("{} * {} = {:2}".format(y,x,x*y),end=" ") #{:2} : 두자리를 주겠다. 예쁘게 출력할 때

    print()

a = [1,2,3,4,5]
result = [num*3 for num in a if num % 2 == 0]
print(result)

result = [] #배열
for num in a:
    if num%2 ==0:
        result.append(num*3)

print(result)