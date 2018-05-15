# 리스트에 요소 추가하기

print("# 리스트 선언")
list_a = [1, 2, 3]
print("list_a =", list_a)
print()

# 리스트 마지막에 요소 추가
list_a.append(4)
print("list_a.append(4) =", list_a)
list_a.append(5)
print("list_a.append(5) =", list_a)
print()

# 리스트 중간에 요소 추가
print("# 0번째 위치에 0 추가")
list_a.insert(0, 0)
print("list_a.insert(0, 0) =", list_a)
print()

print("# -2번째 위치에 10 추가")
list_a.insert(-2, 10)
print(list_a)
print()

# 리스트에 리스트 추가하기
print("# 리스트 추가하기")
list_a = [1, 2, 3]
print("list_a =", list_a)
list_a.extend([4, 5, 6])
print("list_a.extend([4, 5, 6] =", list_a)
