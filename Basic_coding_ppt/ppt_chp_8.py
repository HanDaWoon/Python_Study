"""1. 문자열을 입력 받아 문자열이 길이를 구하고, 문자열의 첫 번째 문자, 두 번째 문자, 마지막 문자를 출력해보자."""

strin = input("문자열 : ")
print("문자열의 길이 :", len(strin))
print("첫 번째 문자 :", strin[0])
print("두 번째 문자 :", strin[1])
print("마지막 문자 :", strin[len(strin)-1])


print()
print("/*-+"*50)
print()


"""2. 문자열을 입력 받아 for 문을 이용하여 개별 문자로 출력해보자. 그리고 for 문을 이용하여 입력받은 문자열의
    역순으로 개별 문자를 출력해보자."""

strin = input("문자열 : ")
print("개별 문자 출력 :", end="")
for i in range(len(strin)):
    print(strin[i], end="")

print("\n역순 개별 문자 출력 : ", end="")
for i in range(len(strin)-1, -1, -1):
    print(strin[i], end="")


print()
print()
print("/*-+"*50)
print()


"""3. 0~100 사이의 점수를 입력 받아 입력한 점수가 0~100인 경우 점수에 대한 A, B, C, D, F 등급을 출력하고, 범위에
    해당하지 않은 경우 "입력 가능한 점수 범위는 0~100입니다."를 출력해보자. 점수에 대한 등급 판정은 if-elif-else 문을
    이용하여 점수가 90~100일 때 "A"이고, 80~89일 때 "B", 70~79일 때 "C", 60~69일 때 "D", 0~59일 때 "F"로 판정한다."""

score = int(input("점수 : "))
if (score >= 0) and (score <= 100):
    if score >= 90:
        print(score, ": A")
    elif score >= 80:
        print(score, ": B")
    elif score >= 70:
        print(score, ": C")
    elif score >= 60:
        print(score, ": D")
    else:
        print(score, ": F")
else:
    print("입력 가능한 점수 범위는 0~100입니다.")


print()
print("/*-+"*50)
print()


"""4. 문제 3을 if-elif-else 문 대신에 딕셔너리를 이용하여 점수에 대한 등급을 출력해보자."""

score = int(input("점수 : "))
scr = score // 10
deg = {10:'A', 9:'A', 8:'B', 7:'C', 6:'D', 5:'F', 4:'F', 3:'F', 2:'F', 1:'F', 0:'F'}
print(score, ":", deg[scr])


print()
print("/*-+"*50)
print()


"""5. 딕셔너리를 이용하여 제품:값의 형태로 items = {"라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700}을
    선언해보자. while 문을 이용하여 무한 반복하면서 제품을 입력 받아 제품에 대한 값들의 합계를 구해 출력해보자. 아무
    것도 입력을 하지 않은 채로 Enter 키를 눌러 빈 문자열이 입력되면 무한 반복을 멈추고 전체 합계를 출력한다."""

items = {"라면": 650, "우유": 1100, "콜라": 1200, "캔커피": 500, "과자": 700}
s = 0
while True:
    it = input("제품명 : ")
    if (it != "") and (it in items):
        s += items[it]
        print("[%s:%d] > %d" % (it, items[it], s))
    elif (it != "") and (it not in items):
        print("%s 는 미등록 제품입니다." %(it))
    else:
        break

print("총 금액 : ", s)


print()
print("/*-+"*50)
print()


"""6. 딕셔너리를 이용하여 비어 있는 영한사전에 단어를 등록해보자. while 문을 이용하여 무한 반복하면서 영어 단어와 한글
        단어를 입력 받아 등록하고, 아무 것도 입력 하지 않은 채로 Enter 키를 눌러 영어 단어와 한글 단어에 빈 문자열이
        되면 무한 반복을 멈추고 딕셔너리에 등록된 모든 키와 값들을 출력한다."""

engkor_dict = dict()
while True:
    eng = input("영어 단어 : ")
    kor = input("한글 단어 : ")
    if (eng=="") and (kor==""):
        break
    engkor_dict[eng] = kor

print(engkor_dict)


print()
print("/*-+"*50)
print()


"""7. 문제 6번의 딕셔너리 engkor_dict을 활용하여 영어 단어를 입력할 경우 해당하는 한글 단어를 표시하도록 수정해보자.
    만약 딕셔너리가 비어 있을 경우 "사전이 비어 있습니다."를 출력하고, 비어 있지 않을 경우 검색을 하여 단어를 표시한다.
    만약 영어 단어가 등록되어 있지 않을 경우 "단어가 등록되어 있지 않습니다."를 출력하고, 딕셔너리가 비어 있을 경우나
    비어 있지 않더라도 영어 단어가 없을 경우 "단어를 추가합니다."를 출력하고 한글 단어를 추가로 입력 받아 딕셔너리에
    추가로 등록한다. while 문에 의한 무한 반복의 종료는 영어 단어가 빈 문자열로 입력되었을 경우 종료하고 딕셔너리에
    등록된 모든 키와 값들을 출력한다."""

engkor_dict = dict()
while True:
    eng = input("영어 단어 : ")
    if eng == "": break
    elif len(engkor_dict) == 0:
        print("사전이 비어있습니다.")
        print("단어를 추가합니다.")
        kor = input("한글 단어 : ")
        engkor_dict[eng] = kor
    elif eng in engkor_dict:
        print("한글 단어 :", engkor_dict[eng])
    else:
        print("%s 단어가 등록되어 있지 않습니다." % (eng))
        print("단어를 추가합니다.")
        kor = input("한글 단어 : ")
        engkor_dict[eng] = kor

print(engkor_dict)


print()
print("/*-+"*50)
print()

"""8. time 모듈을 import한 후, for 문을 이용하여 1부터 5까지의 숫자를 출력해보자. 각 숫자를 출력한 후 sleep() 함수를
    이용하여 프로그램을 1초간 멈추게 해보자."""

import time
for i in range(1, 6):
    print(i)
    time.sleep(1)


print()
print("/*-+"*50)
print()


"""9. math 모듈을 import한 후, 실수 값을 입력 받아 ceil()함수, floor()함수, trunc()함수 연산의 결과를 출력해보자."""

import math

num = float(input("실수 : "))

print("%s : %d" %(num, math.ceil(num)))
print("%s : %d" %(num, math.floor(num)))
print("%s : %d" %(num, math.trunc(num)))
