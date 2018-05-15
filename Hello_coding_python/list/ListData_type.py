a = [1, 2, 3]       #리스트의 인덱싱
print(a)
print(a[0])
print(a[1]+a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]      #리스트의 인덱싱
print(a[0])
print(a[-1])
print((a[3]))

a = [1, 2, ['a', 'b', ['Life', 'is']]]      #삼중 리스트에서 인덱싱
print(a[2][2][0])

a = [1, 2, 3, 4, 5]     #리스트의 슬라이싱
print(a[0:2])
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]        #[중첩된 리스트에서 슬라이싱하기]
print(a[2:5])
print(a[3][:2])

a = [1, 2, 3]       #리스트 더하기
b = [3, 4, 5]
print(a+b)

a = [1, 2, 3]       #리스트 반복하기
print(a*3)

a = [1, 2, 3]       #리스트에서 하나의 값 수정하기
print(a)
a[2] = 4
print(a)
print(a[1:2])       #리스트에서 연속된 범위의 값 수정하기
a[1:2] = ['a', 'b', 'c']
print(a)
a[1:3] = [ ]        #[ ] 사용해 리스트 요소 삭제하기
print(a)
del a[1]            #del 함수 사용해 리스트 요소 삭제하기
print(a)

a = [1, 2, 3]       #리스트에 요소 추가(append)
print(a)
a.append(4)
a.append([5,6])
print(a)

a = [1, 4, 3, 2]    #리스트 정렬(sort)
print(a)
a.sort()
print(a)
a = ['b', 'c', 'a']
print(a)
a.sort()
print(a)

a = ['a', 'c', 'b'] #리스트 뒤집기(reverse)
print(a)
a.reverse()
print(a)

a = [1, 2, 3]       #위치 반환(index)
print(a)
print(a.index(3))
print(a.index(1))

a = [1, 2, 3]       #리스트에 요소 삽입(insert)
print(a)
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

a = [1, 2, 3, 1, 2, 3] #리스트 요소 제거(remove)
print(a)
a.remove(3)
print(a)
a.remove(3)
print(a)

a = [1, 2, 3]           #리스트 요소 끄집어내기(pop)
print(a)
print(a.pop())
print(a)

a = [1, 2, 3]           #리스트 요소 끄집어내기(pop)
print(a.pop(1))
print(a)

a = [1, 2, 3, 1]        #리스트에 포함된 요소 x의 개수 세기(count)
print(a.count(1))

a = [1, 2, 3]           #리스트 확장(extend)
print(a)
a.extend([4,5])
print(a)
b = [6, 7]
a.extend(b)
print(a)