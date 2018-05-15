# 4. 좋아하는 과목 이름과 희망하는 점수를 다음과 같이 입력 받아 변수 subject와 변수 score 에 각각 대입하고，두 변수의 값을 다음 형태로 출력해보자.
subject = input("과목 : ")
score = int(input("점수 : "))
print("선호 과목 : %s , 희망 점수 : %d" %(subject, score))


print("*"*50)


# 5. 정수 3개를 입력 받아 변수 a, b, c에 각각 대입하고，합계를 구하여 변수 sum에 대입하고 평균을 구하여 변수 avg에 대입해보자. 그리고 다음과 같이 모든 변수의 값을 출력해보자.
a = int(input("정수1:"))
b = int(input("정수2:"))
c = int(input("정수3:"))
sum = a + b + c
avg = sum / 3
print("정수1: %d 정수2: %d 정수3: %d" %(a, b, c))
print("합: %d 평균: %d" %(sum, avg))


print("*"*50)



# 6. 정수를 입력 받아 변수 a에 저장한 후，변수 a의 값을 문자열로 변환하여 변수 b에 저장해보 자. 그리고 변수 a, b의 값과 자료형을 출력해보자.
a = int(input("정수:"))
b = str(a)
print(345, type(a), type(b))