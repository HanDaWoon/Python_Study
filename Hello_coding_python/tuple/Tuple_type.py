# t1 = ()
# t2 = (1,)
# t3 = (1, 2, 3)
# t4 = 1, 2, 3
# t5 = ('a', 'b', ('ab', 'cd'))
# print(t1, t2, t3, t4, t5)


#인덱싱하기
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

#슬라이싱하기
t1 = (1, 2, 'a', 'b')
print(t1[1:])

#튜플 더하기
t2 = (3, 4)
print(t1 + t2)

#튜플 곱하기
print(t2*3)