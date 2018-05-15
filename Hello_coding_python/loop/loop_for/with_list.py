# 리스트 선언
lst = [231, 56, "str", 546, False]

print("리스트 선언(고정) : lst =", lst, "\n")

"""for <요소를 담을 변수> in <리스트>:
        <코드>
"""
i = 0
for element in lst:
    print(element, i)
    i += 1