# 리스트 선언
array = [273, 32, 103, "문자열", True, False]

# 출력하기
print(array)

# 리스트의 요소 출력하기
print(array[0])
print(array[1])
print(array[2])
print(array[1:3])

# 리스트의 요소 변경
array[0] = "변경"

# 리스트 전체 출력
print(array)




print("="*50)




# 리스트 선언
array = [273, 32, 103, "문자열", True, False]

# 리스트 요소 출력
print(array[-1])
print(array[-2])
print(array[-3])




print("="*50)




## 리스트 연산자

# 리스트 선언
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 출력
print("# 리스트")
print("list_a = ", list_a)
print("list_b = ", list_b)
print()

# 기본 연산자
print("# 리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 = ", list_a * 3)
print()

# 함수
print("# 길이 구하기")
print("len(list_a) = ", len(list_a))




print("="*50)




## 리스트 요소추가

# 리스트 선언
list_a = [1, 2, 3]

# 출력
print("list_a =", list_a , "\n")

# 리스트 뒤에 요소 추가
print("# 리스트 뒤에 요소 추가")
list_a.append(4)
list_a.append(5)
print("list_a =", list_a , "\n")

# 리스트 중간에 요소 추가
print("# 리스트 중간에 요소 추가")
list_a.insert(0, 10)
print("list_a =", list_a , "\n")

## 여러요소를 추가

print("# 여러요소를 추가")
# 리스트 선언
list_a = [1, 2, 3]
print("list_a = ", list_a, "\n")
list_a.extend([4, 5, 6])
print("list_a.extend([4, 5, 6]) = ", list_a, "\n")




# 리스트 선언
list_a = [1, 2, 3]

# 연결 연산자로 리스트 연결
output = list_a + list_a
print("# 리스트 연결 연산자 사용")
print("# 원본 리스트:", list_a)
print("# 결과:", output)
print()

# extend() 함수로 리스트 연결
output = list_a.extend([1, 2, 3])
print("# extend() 함수 사용")
print("원본 리스트:", list_a)
print("연산 결과:", output)