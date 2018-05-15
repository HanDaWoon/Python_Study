#변수를 만드는 여러가지 방법
a, b = ('HDW', 'HAR')
print(a, b)
(a, b) = 'HDW', 'HAR'
print((a, b))
[a, b] = ['HDW', 'HAR']
print([a, b])
a = b = 'HDW'
print(a + b)

print("\n")

#두변수의 값 바꾸기
a = 3
b = 5
print(a, b)
a, b = b, a
print(a, b)

print("\n")

#리스트를 변수에 넣고 복사하고자 할 때
a = [1, 2, 3]
b = a
print(a, b)
a[1] = 4
print(a, b)

print("\n")

#1.[:] 이용
a = [1, 2, 3]
b = a[:]
print(a, b)
a[1] = 4
print(a, b)

print("\n")

#2.copy 모듈 이용
from copy import copy
b = copy(a)     #<-> b = a[:]
print(b is a)