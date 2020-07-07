import re
p= re.compile('ab*')

m = p.match('bac') #match는 처음부터 체크해서 a가 안오면 None
print(m)

m1 = p.search('bac')
print(m1)

email = input("이메일 입력")
p = re.compile('[a-z][az0-9]{4,}@[a-z]')
result =p.match(email)
print(result)