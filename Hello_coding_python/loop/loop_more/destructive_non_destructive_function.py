# 문자열의 비파괴적 함수
print("# 문자열의 비파괴적 함수")
string = "Howowo Python"
print('string = "Howowo Python"')

output = string.upper()
print("string.upper() :", output)

output = string.lower()
print("string.lower() :", output)

output = string.split(" ")
print('output = string.split(" ") :', output)


print("\n", "=+*"*50, "\n")

# 리스트의 파괴적 함수
print("# 리스트의 파괴적 함수")
lst = [1, 2, 3, 4]

lst.append(1)
print("lst.append(1)", lst)

lst.remove(2)
print("lst.remove(2)", lst)

lst.pop()
print("lst.pop()", lst)


print("\n", "=+*"*50, "\n")


# 문자열의 함수
str = "Howowo Python"
output = str.upper()

print("# 문자열의 함수 확인")
print("str :", str)
print("str.upper()의 결과 :", output)
print("str :", str)


print("\n", "=+*"*50, "\n")


# 리스트의 함수
lst = [1, 2, 3, 4]
output = lst.append(1)

print("# 리스트의 함수 확인")
print("lst :", lst)
print("lst.append()의 결과 :", output)