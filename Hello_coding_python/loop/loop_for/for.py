# 리스트 선언
lst = [12, 31, "hhh", 54, 123, "hdw"]

# 반복문 적용
for i in range(len(lst)):
    print("%d 번째 리스트 :" %i, lst[i])

print("*"*50)

# 역반복문
for i in reversed(range(10)):
    print("%d 번째 반복" %i)