# 1. for 문을 이용하여 리스트 [1，3, 5, 7, 9]의 원소들의 합을 순서대로 다음과 같이 출력해보자.
ls = [1, 3, 5, 7, 9]
s = 0
for i in ls:
    s = s + i
    print(i, s)


print("="*50)


# 2. for 문을 이용하여 subject 리스트 ["국어", "영어", "수학", "과학", "한국사"]의 원소를 순서 대로 출력해보자.
subject = ["국어", "영어", "수학", "과학", "한국사"]
for i in subject:
    print(i, end=" "+"\n")


print("="*50)


# 3. for 문을 이용하여 name 리스트 ["홍길동", "임꺽정"]과 subject 리스트 ["국어", "영어", "수학"]의 원소를 교차 반복 출력해보자.
name = ["홍길동", "임꺽정"]
subject = ["국어", "영어", "수학"]
for i in name:
    for j in subject:
        print(i, end=" ")
        print(j)


print("="*50)


# 4. for 문과 rangeO 함수를 이용하여 1 부터 100까지의 모든 수의 합을 출력해보자.
s = 0
for i in range(1, 101):
    s += i
print(s)

# sum 함수 이용 리스트 한번에 입력 받기
print("값 : ", sum([i for i in  range(1, 101)]))

print("="*50)

# 5. for 문과 range 함수를 이용하여 1 부터 10까지의 모든 홀수의 합과짝수의 합을 각각 계산하여 출력해보자.
s = 0
h = 0
for i in range(1, 11):
    if i % 2 == 0:
        s += i
    else:
        h += i
print("홀수 합 :", h)
print("짝수 합 :", s)


print("="*50)


# 6. for 문과 range() 함수를 이용하여 3부터 -3 까지의 모든 수를 한 줄에 나열하여 출력하고，모든 수의 합을 계산하여 출력해보자.
s = 0
for i in range(3, -4, -1):
    print(i, end=" ")
    s += i
print("")
print(s)


print("="*50)


# 7. for 문을 이용하여 반복하면서 num 리스트 [8, 7, 3, 2, 9, 4, 1, 6, 5]의 원소 중 값이 가장 큰 수와 가장 작은 수를 출력해보자.
import sys
mx = -sys.maxsize-1
mm = sys.maxsize
num = [8, 7, 3, 2, 9, 4, 1, 6, 5]
for i in num:
    if i > mx:
        mx = i
    if i < mm:
        mm = i
print("최댓값 :", mx)
print("최솟값 :", mm)

# 파이썬에서 리스트 중 최대값을 구하는 함수
print(max(num))
# 파이썬에서 리스트 중 최소값을 구하는 함수
print(min(num))

print("num : ", num)
print("sorted(num) : ", sorted(num))

print(sorted(num)[-1])
print(sorted(num)[0])

print("="*50)


# 8. 두 개의 for 문을 중첩하여 반복하면서 다음 모양을 출력해보자.
for i in range(1, 6):
    for j in range(1, 5):
        print("*", end="")
    print("")


print("="*50)


# 9. 바깥쪽 한 개의 for 문과 안쪽 두 개의 for 문을 중첩하여 반복하면서 다음 모양을 출력해보자.
for i in range(1, 6):
    for j in range(1, 1+i):
        print("*", end="")
    print("")


print("="*50)


# 10. 두 개의 for 문을 중첩하여 반복하면서 다음 모양을 출력해보자.
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for n in range(1, i + 1):
        print("*", end="")
    print("")


print("="*50)


# 11. 바깥쪽 한 개의 for 문과 안쪽 세 개의 for 문을 중첩하여 반복하면서 다음 모양을 출력해보자.
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for n in range(1, i + 1):
        print("*", end="")
    for o in range(1, i):
        print("*", end="")
    print()

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for n in range(1, i * 2):
        print("*", end="")
    print()


print("="*50)


# 12. while 문을 이용하여 반복하면서 정수를 입력받아 입력된 모든 수의 합을 출력해보자. 단, 입력한 정수 값이 0이 아니면 반복을 계속 진행하고，0이면 반복을 종료한다.
s = 0
n = None
while n != 0:
    n = int(input("정수 : "))
    s += n
print("합 :", s)


print("="*50)


# 13. while 문을 이용하여 비밀번호를 입력받아 "pwpass”가 아닐 경우 계속 비밀번호를 입력받고，“pwpass”가 입력될 경우 “Login Pass!!”를 출력해보자.
pw = None
while pw != "pwpass":
    pw = input("비밀번호 : ")
print("LogIn Pass!!")


print("="*50)


# 14. while 문을 이용하여 무한 반복을 하면서 정수를 입력 받아 합을 계산해보자. 단，입력한 정수 값이 양수이면 합을 구하고, 음수이면 합을 구하지 말고 계속 반복을 진행한다. 단，0인 경우 반복을 종료하고 계산된 합을 출력한다.
s = 0
while True:
    n = int(input("정수 : "))
    if n > 0: s += n
    if n == 0: break
print(s)

print("="*50)


# 15. 종이를 한 번 접으면 원래 두께의 2배로 두꺼워진다. 이렇게 접은 종이를 또 다시 접으면 종이두께는 원래 종이 두께의 4배가 된다. 또 다시 접으면 8배가 된다. n번 접으면 원래 두께에 2n 을 곱한 수만큼 두께가 커지게 된다. 이런 과정을 계속하여 접은 두께가 100m(100000mm) 를 넘으려면 두께가 1 mm인 종이를 몇 번 접어야 할지 계산해보자.
thickness = 1
n = 0
while thickness < 100000:
    thickness = thickness * 2
    n += 1
    print("%d 번 접으면 %d mm" % (n, thickness))
print("횟수 : %d 두께 : %d" % (n, thickness))
