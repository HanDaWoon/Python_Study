test_list = ['one', 'two', 'tree']
for i in test_list:
    print(i)

print("\n")

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

print("\n")

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)

print("\n")

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

print("\n")

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

print("\n")

