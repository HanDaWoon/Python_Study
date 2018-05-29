# 1번.
a = b = c = 1   # 전역 변수

def func():
    a = b = c = 2   # 지역 변수
    print("func:", a, b, c)


print("main:", a, b, c)
func()
print("main:", a, b, c)


# 2번.
a = b = c = 1   # 전역 변수

def func():
    global a, b, c  # 전역 변수 참조
    a = b = c = 2   # 지역 변수
    print("func:", a, b, c)


print("main:", a, b, c)
func()
print("main:", a, b, c)


# 3번.
a = b = c = 1   # 전역 변수

def func1():
    a = b = c = 2
def func2():
    global a, b
    a = b = 3
    c = 3

print(a, b, c)
func1()
print(a, b, c)
func2()
print(a, b, c)


# 4번.
quotient = None
remainder = None
def div_qr():
    global quotient, remainder
    a = int(input("정수1 : "))
    b = int(input("정수2 : "))
    quotient = a // b
    remainder = a % b
    print("몫: %d 나머지: %d" %(quotient, remainder))


# 5번.
def div_qr():
    a = int(input("정수1 : "))
    b = int(input("정수2 : "))
    quotient = a // b
    remainder = a % b
    return (quotient, remainder)

(q, r) = div_qr()
print("몫: %d 나머지: %d" % (q, r))



# 6번.
data = [21, 7, 43, 65, 2, 8, 72, 52, 9]
for i in data:
    print(i, end=" ")


# 7번.
data = [21, 7, 43, 65, 2, 8, 72, 52, 9]

while True:
    find = int(input("찾을 값 : "))
    if find in data:
        print("위치:", data.index(find))
        break
    else:
        print("찾지 못함")
        continue


# 8번.
data = [
    [21, 7, 43, 65],
    [2, 8, 72, 52]
]
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=" ")
    print()


# 9번.
data = [
    [21, 7, 43, 65],
    [2, 8, 72, 52]
]
find = int(input("찾을 값 : "))
for i in range(len(data)):
    for j in range(len(data[i])):
        if find == data[i][j]:
            print("위치: %s행 %s열" %(i+1, j+1))
            break


# 10번.
import copy

s7seg_num = [[1, 1, 1, 1, 1, 1, 0],  # 0
             [0, 1, 1, 0, 0, 0, 0],  # 1
             [1, 1, 0, 1, 1, 0, 1],  # 2
             [1, 1, 1, 1, 0, 0, 1],  # 3
             [0, 1, 1, 0, 0, 1, 1],  # 4
             [1, 0, 1, 1, 0, 1, 1],  # 5
             [1, 0, 1, 1, 1, 1, 1],  # 6
             [1, 1, 1, 0, 0, 0, 0],  # 7
             [1, 1, 1, 1, 1, 1, 1],  # 8
             [1, 1, 1, 1, 0, 1, 1]]  # 9

s7seg_num_anode = copy.deepcopy(s7seg_num)
change = {0: 1, 1: 0}
for i in range(len(s7seg_num)):
    for j in range(len(s7seg_num[i])):
        s7seg_num_anode[i][j] = change[s7seg_num_anode[i][j]]


# 11번.
import turtle

default_shape = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
user_shape = ["7s0.gif", "7s1.gif", "7s2.gif"]
for i in default_shape:
    turtle.shape(i)
for i in user_shape:
    turtle.addshape(i)
    turtle.shape(i)