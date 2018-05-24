# 재귀 함수의 문제

# 재귀 함수로 구현한 파보나치 수열
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(1)", fibonacci(1))
print("fibonacci(2)", fibonacci(2))
print("fibonacci(3)", fibonacci(3))
print("fibonacci(4)", fibonacci(4))
print("fibonacci(5)", fibonacci(5))


# 피보나치 함수의 문제 찾기
counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(35)
print("---")
print("fibonacci(35) 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))


# 메모화
dictionary = {
    1: 1,
    2: 2
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

print("fibonacci(10)", fibonacci(10))
print("fibonacci(20)", fibonacci(20))
print("fibonacci(30)", fibonacci(30))
print("fibonacci(40)", fibonacci(40))
print("fibonacci(50)", fibonacci(50))


# 마지막에 리턴하기
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

# 조기 리턴
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]

    output = fibonacci(n - 1) + fibonacci(n - 2)
    dictionary[n] = output
    return output