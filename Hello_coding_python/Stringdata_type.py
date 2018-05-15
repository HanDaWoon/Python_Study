print('Hello"world"')   #문자열 안에 따음표 포함시키기

print("\"Hello\" world")    #문자열 안에 따음표 포함시키기

print("Hello\nworld")   #줄바꿈

print("""Hello
        world""")   #줄바꿈

print('''Hello
        world''')   #줄바꿈

head = "Hello"
tail = "world"
print(head + tail)  #문자열 연결하기

a = "Hello"
print(a*2)  #문자열 곱하기

b = "Hello, world!"
print(b[4])
print(b[-1])
print(b[0:5])
print((b[7:]))  #문자열 인덱싱

c = "20180323Sunny"
date = c[:8]
weather = c[8:]
print(date)
print(weather)  #문자열 슬라이싱

asd = "Pithon"
print(asd[:1])
print(asd[2:])
print(asd[:1] + 'y' + asd[2:])  #문자열 슬라이싱

print("My name is %s" %"HDW")
print("My student ID is %d" %2018575070)
print("KYUNGSUNG-NAME: %s, Student ID: %d" %("HDW", 2018575070))    #문자열 포매팅

print("%10s" % "hi")
print("%-10sjane." % 'hi')
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)    #문자열 포매팅

a = "Hello, world!"
print(a.count("l"))     #문자 개수 세기

a = "Hello, world!"
print(a.find("e"))
print(a.find("w"))      #위치알려주기

a = ","
print(a.join('HELLO'))      #문자열 삽입

a = "hello"
print(a.upper())    #대문자로 바꾸기

a = "Hello"
print(a.lower())    #소문자로 바꾸기

a = "  Hello  "
print(a.lstrip())   #왼쪽공백 지우기
print(a.rstrip())   #오른쪽공밳 지우기
print(a.strip())    #양쪽공백 지우기

a = "Hello, man!"
print(a.replace("man", "world"))    #문자열 바꾸기

a = "Nice too meet you"
print(a.split())
a = "a:b:c:d"
print(a.split(':'))     #문자열 나누기

print("I'm {0} years old".format(20))           #문자열 포메팅
print("I'm {0} years old".format("twenty"))
number = 20
print("I'm {0} years old".format(number))
number = 10
name = "HDW"
print("I'm {0} years old. My name is {1}".format(number, name))
print("I'm {number} years old. My name is {name}".format(number=20, name="HDW"))
print("I'm {0} years old. My name is {name}".format(number, name="HDW"))