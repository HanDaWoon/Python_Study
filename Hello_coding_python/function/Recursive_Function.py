# 반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

print("*"*50)

# 재귀 함수로 팩토리얼 구하기
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))