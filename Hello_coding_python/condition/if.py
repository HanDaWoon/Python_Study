# 입력을 받습니다.
number = int(input("정수입력> "))

# 양수 조건
if number > 0:
    print("양수입니다")
# 음수조건
if number < 0:
    print("음수입니다")
# 0 조건
if number == 0:
    print("0입니다")



print("="*50)



# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")



print("-"*50)



# 오전 구분
if now.hour < 12:
    print("현재 시간은 %d시로 오전입니다." %now.hour)

# 오후 구분
if now.hour > 12:
    print("현재 시간은 %d시로 오후입니다." %now.hour)

# 봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 %d월로 봄입니다!" %now.month)

# 여름 구분
if 6 <= now.month <= 8:
    print("이번 달은 %d월로 여름입니다!" % now.month)

# 가을 구분
if 9 <= now.month <= 11:
    print("이번 달은 %d월로 가을입니다!" % now.month)

# 겨울 구분
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 %d월로 겨울입니다!" % now.month)



print("-"*50)



# # 입력을 받습니다.
# number = int(input("정수입력> "))
#
# # 문자열로 변환
# number = str(number)
# # 마지막 자리 숫자를 추출
# last_character = number[-1]
# # 숫자로 변환하기
# last_number = int(last_character)
#
# # # 짝수확인
# # if last_number == 0 \
# #     or last_number == 2 \
# #     or last_number == 4 \
# #     or last_number == 6 \
# #     or last_number == 8:
# #     print("짝수입니다.")
# #
# # # 홀수확인
# # if last_number == 1 \
# #     or last_number == 3 \
# #     or last_number == 5 \
# #     or last_number == 7 \
# #     or last_number == 9:
# #     print("홀수입니다.")



print("="*50)



number = int(input("정수를 입력하세요> "))
# 짝수일떄
if number % 2 == 0:
    print("짝수입니다.")
# 홀수일때
if number % 2 != 0:
    print("홀수입니다.")