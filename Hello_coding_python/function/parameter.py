# 매개변수
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 10)


# 가변 매개변수
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕", "탈주", "닌자")


# 기본 매개변수
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")


# 키워드 매개변수(기본 매개변수가 가변 매개변수보다 앞에 올 때)
def print_n_times(n=2, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕", "탈주", "닌자")


# 키워드 매개변수(가변 매개변수가 기본 매개변수보다 앞에 올 때)
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕", "탈주", "닌자", 3)


# 키워드 매개변수
def print_n_times(*values, n = 2):
    for i in range(n):  # n번 반복
        for value in values:
            print(value)
        print()

print_n_times("안녕", "탈주", "닌자",  n = 3)


# 키워드 매개변수의 다양한 사용
def test(a, b=10, c=100):
    print(a + b + c)

# 1) 기본 형태
test(10, 20, 30)
# 2) 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)
# 3) 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)
# 4) 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)