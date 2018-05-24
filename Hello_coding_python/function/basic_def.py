def sum_all(start, end):    # 함수 선언
    output = 0  # 변수 선언
    for i in range(start, end + 1): # 반복문을 이용, 숫자 더함
        output += i
    return output

print(sum_all(0, 100))
print(sum_all(0, 10000))
print(sum_all(50, 100))
print(sum_all(500, 10000))

print("*"*50)

def sum_all(start=0, end=100, step=1):    # 함수 선언
    output = 0  # 변수 선언
    for i in range(start, end + 1, step): # 반복문을 이용, 숫자 더함
        output += i
    return output

print(sum_all(0, 100, 10))
print(sum_all(end=100))
print(sum_all(end=100, step=2))