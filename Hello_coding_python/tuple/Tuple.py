# 튜플 기본
tuple_test = (10, 20, 30)

print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])

tuple_test = (10, ) # 요소를 하나만 가질때

# 튜플을 사용한 할당
# 리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)

print("a:", a)
print("a:", b)
print("a:", c)
print("a:", d)

# 괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print("tulpe_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

# 괄호가 없는 튜플 활용
a, b, c = 10, 20, 30
print("a:", a)
print("b:", b)
print("c:", c)


# 튜플을 사용한 여러 개의 값 리턴
def test():
    return (10, 20)

a, b = test()

print("a:", a)
print("b:", b)