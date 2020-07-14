#from modtest.mod1 import add,sub #주소를 잘 적어주자 , 뒤에 가져올때 나열 가능
from modtest.sound.etc import mod1 as m # as 뒤에 별칭

a=m.add(2,4)
print(a)
b=m.sub(4,2)
print(b)

import sys
print(sys.path)
sys.path.append("c:\\python\\mtest")

import mod2 #못찾음
print(mod2.div(3,5))