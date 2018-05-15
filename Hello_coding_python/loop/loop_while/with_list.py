# 리스트 선언
lst = [1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, ]
# 리스트에서 없에고자 하는 요소 입력(1 또는 2)
val = int(input("없에고자 하는 요소 입력(1 또는 2):"))

# while 사용
while val in lst:
    lst.remove(val)

# 출력
print(lst)