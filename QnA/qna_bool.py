a = int(input("int_a:"))
b = int(input("int_a-1:")) + 1
c = input("str_c:")
d = input("str_d:")

print("아스키 코드 변환 a = %s, b = %s" %(chr(a), chr(b)))
print("객체의 고유 주소값 a = %d, b = %d" %(id(a), id(b)))

print("a == b : ", a == b)
print("a is b : ", a is b)

for i in range(len(c)):
    print(c[i], ord(c[i]))
print("객체의 고유 주소값 c : ", id(c))

for i in range(len(d)):
    print(d[i], ord(d[i]))
print("객체의 고유 주소값 d : ", id(d))

print("c == d : ", c == d)
print("c is d : ", c is d)