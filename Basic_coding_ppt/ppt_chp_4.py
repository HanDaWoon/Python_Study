# 2. 정수를 입력 받아 변수 a, b에 저장한 후，다음과 같은 수식의 결과를 출력해보자.（파이썬 셸 대신에 파이썬 에디터를 사용하여 작성하고 실행해보자.)
a = int(input("숫자1 : "))
b = int(input("숫자2 : "))
print("%d / %d = " %(a, b), a / b)
print("%d // %d = " %(a, b), a // b)
print("%d %% %d = " %(a, b), a % b)


print("*"*50)


# 3. 원의 반지름을 입력 받아 변수 radius에 대입하고 원의 넓이를 구해보자.
import math
radius = int(input("반지름 : "))
math.pi
print("원의 넓이 : ", radius * math.pi)

# 4. 시간의 초를 입력 받아 변수 sec에 대입하고，분(minute)과 초(second)를 구해보자.
sec = int(input("초 : "))
minute = sec // 60
second = sec % 60
print("%d 초 = %d 분 %d 초" %(sec, minute, second))

# 5. 정수 값을 입력 받아 변수 a에 대입하고，하나의 대입문으로 변수 b, c, 선에 변수 a의 값을 대입한 후 모든 변수의 값을 출력해보자.
a = int(input("정수 : "))
b = c = d = a
print(a, b, c, d)

# 6. 다음 수식을 복합 대입 연산자를 이용하여 변경하고，a = 3, b = 2, c = 4의 경우 각 수식 이 실행 된 후의 변수 a 값을 구해보자.
# 생략

# 7. (1).4 빼기 3분의2, (2).(2+4)분의 (1+2), (3).(4빼기(3분의2))분의 (3*2)
# (1)
print(4 - (2 / 3))
# (2)
print((1 + 2) / (2 + 4))
# (3)
print((3 * 2) / (4 -(2 / 3)))