# 3. 정수를 입력 받아 변수 num에 대입한 후, 변수 num의 값이 100 보다 작을 경우 숫자를 출력해보자.
num = int(input("정수 : "))
if num < 100:
    print("정수 : {}".format(num))




# 4. 정수를 입력 받아 변수 num에 대입한 후, 변수 num의 값이 짝수인 경우 "짝수"를 출력해보자.
num = int(input("정수 : "))
if num % 2 ==0:
    print("짝수")




# 5. 정수를 입력 받아 변수 num에 대입한 후, 변수 num의 값이 짝수인 경우 "짝수"를, 홀수인 경우 "홀수"를 출력해보자.
num = int(input("정수 : "))
if num % 2 ==0:
    print("짝수")
else:
    print("홀수")




# 6. 정수를 입력 받아 변수 num에 대입한 후, 변수 num의 값이 100 보다 작을 경우 10% 감소한 값을 출력하고 그렇지 않으면 10% 증가한 값을 출력해보자.
num = int(input("정수 : "))
if num < 100:
    print(num * 0.9)
else:
    print(num * 1.1)




# 7. 두 정수를 입력 받아 변수 a, b에 각각 대입하고, a+b-b**2의 계산 결과가 0이거나 양수이면 결과를 출력하고, 음수이면 "음수"를 출력해보자.
a = int(input("a : "))
b = int(input("b : "))
tmp = (a + b - (b ** 2))
if tmp >= 0:
    print(tmp)
else:
    print("음수")




# 8. 정수를 입력 받아 변수 num에 대입한 후, 변수의 값이 2와 3으로 나누어질 경우 “나누어짐” 을 출력하고，그렇지 않으면 "나누어지지 않음"이라고 출력해보자.
num = int(input("정수 : "))
if (num % 2 == 0) and (num % 3 == 0):
    print("나누어짐")
else:
    print("나누어지지 않음")




# 9. a=5, b=3인 경우，+，- ，*, / 중 한 문자를 입력 받아 + 이면 두 변수의 더하고，-이면 두 변수를 빼고，*이면 두 변수를 곱하고，/이면 두 변수를 나누는 연산을 하여 그 결과를 출력해봐자.
a, b = 5, 3
oper = input("연산자 : ")
if oper == "+":
    print("5 + 3 =", a + b)
elif oper == "-":
    print("5 - 3 =", a - b)
elif oper == "*":
    print("5 * 3 =", a * b)
else:
    print("5 / 3 =", a / b)




# 10. 정수를 입력 받아 다음 수소 이온 지수(PH) 범위 내의 숫자일 경우 해당 용액의 종류를 출력 해보자.
ph = int(input("ph : "))
if (ph >= 0) and (ph <= 4):
    print("강산성")
elif (ph >= 5) and (ph <=6):
    print("약산성")
elif ph == 7:
    print("중성")
elif (ph >= 8) and (ph <= 9):
    print("약염기성")
else:
    print("강염기성")




# 11. 년도를 입력 받아 윤년인지 평년인지를 구분하여 출력해보자.
year = int(input("년도 : "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("윤년")
else:
    print("평년")




# 12. 키와 몸무게를 입력 받아 체질량지수(Body Mass Index, BMI)를 계산하여 출력해보자. BMI 계산은 몸무게(kg) / 키(m)2로 계산하며，BMI 판정 기준은 다음과 같다.
cm = int(input("키(cm) : "))
kg = int(input("몸무게(kg) : "))
bmi = kg / (cm * 0.01) ** 2
if bmi < 18.5:
    print("저체중")
elif (bmi >= 18.5) and (bmi < 23):
    print("정상")
elif (bmi >= 23) and (bmi < 25):
    print("과체중")
elif (bmi >= 25) and (bmi < 30):
    print("경도비만")
elif (bmi >= 30) and (bmi < 35):
    print("중등도비만")
else:
    print("고도비만")