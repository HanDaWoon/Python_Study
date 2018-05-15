# 인덱스로 제거하기

print("#리스트 선언")
list_a = [0, 1, 2, 3, 4, 5]
print("list_a =", list_a)
print()

print("# 리스트의 요소 하나 제거\n")

del list_a[1]
print("del list_a[1] \n=", list_a)
print()

list_a = [0, 1, 2, 3, 4, 5]

list_a.pop(3)
print("list_a.pop(3) \n=", list_a)
print()

list_a = [0, 1, 2, 3, 4, 5]

list_a.pop()
print("list_a.pop() \n=", list_a)


print()
print("-=-" * 50)
print()


print("#리스트 선언")
list_a = [0, 1, 2, 3, 4, 5]
print(list_a)
print()

print("# 리스트의 요소 여러개 제거\n")

del list_a[1:3]
print("del list_a[1:3]\n=", list_a)
print()

list_a = [0, 1, 2, 3, 4, 5]

del list_a[2:]
print("del list_a[2:]\n=", list_a)
print()

list_a = [0, 1, 2, 3, 4, 5]

del list_a[:2]
print("del list_a[:2]\n=", list_a)
print()

list_a = [0, 1, 2, 3, 4, 5]

del list_a[:]
print("del list_a[:]\n=", list_a)


print()
print("=+=" * 50)
print()


# 값으로 제거하기

print("#리스트 선언")
list_a = [0, 1, 2, 3, 4, 5]
print("list_a =", list_a)
print()

print("# 특정 값 제거\n")
list_a.remove(3)
print("list_a.remove(3)\n=", list_a)


print()
print("-=-" * 50)
print()


print("#리스트 선언")
list_a = [1, 2, 1, 2, 1, 2]
print("list_a =", list_a)
print()

list_a.remove(2)
print("list_a.remove(2)\n=", list_a)
print("# remove() 는 해당 값이 여러개여도 가장 먼저 발견된 값만 제거한다.")


print()
print("=+=" * 50)
print()


print("#리스트 선언")
list_a = [0, 1, 2, 3, 4, 5]
print("list_a =", list_a)
print()

print("# 모두 제거하기")
list_a.clear()
print("list_a.clear()\n=", list_a)