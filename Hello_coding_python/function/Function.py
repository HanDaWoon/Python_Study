#default function
def sum(a, b):
    result = a + b
    return result

a = sum(3, 4)
print(a)


print("\n")


#Functions without input values
def say():
    return 'Hi'

a = say()
print(a)


print("\n")


#Functions without result values
def sum(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

sum(3, 4)       #3, 4의 합은 7입니다.

print("\n")

a = sum(3, 4)   #3, 4의 합은 7입니다.

print("\n")

print(a)        #None

print("\n")

#Functions without input and output
def say():
    print('Hi')

say()


print("\n")

#Create a function that accepts multiple input values
def sum_many(*args):
        sum = 0
        for i in args:
            sum = sum + i
        return sum

result = sum_many(1, 2, 3)
print(result)
result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

print("\n")

def sum_mul(choice, *args):
    if choice =="sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)
result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)

print("\n")

#kwargs
def func(**kwargs):
    print(kwargs)

func(a=1)
func(name="HDW", age="20")

print("\n")

def func(*args, **kwargs):
    print(kwargs)
    print(args)

func(1, 2, 3, name="HDW", age=20)


print("\n")

def nick_n(nick):
     if nick == "바보":
         return                         #return을 만나면 빠져나간다.
     print("나의 별명은 %s 입니다." %nick)

nick_n("HHH")
nick_n("바보")


print("\n")


def me(name, old, man=0):               #입력 인수에 초깃값 미리 설정하기
    print("My anme is %s" %name)
    print("I am %d years old" %old)
    if man:
        print("I am a man")
    else:
        print("I am a women")

me("HDW", 20)


print("\n")


#함수안에서 선언된 변수의 범위
a = 1
def range(a):
    a = a + 1

range(a)                                #함수안에서 선언된 변수는 함수 안에서만 사용된다.
print(a)


#함수 안에서 밖의 함수를 변경하는 방법
a = 1
def in_out(a):
    a = a + 1
    return a                            #return

a = in_out(a)
print(a)

a = 1
def in_out():
    global a                            #global
    a = a + 1

in_out()
print(a)