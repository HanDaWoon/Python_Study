# 딕셔너리 선언
dict = {
    "name" : "DB-HDW",
    "type" : "computer",
    "element" : ["cpu", "gpu", "ram", "mainboard"]
}
print("딕셔너리 선언(고정) : dict =", dict, "\n")

# 딕셔너리 요소 제거
del dict["name"]
print('del dict["name"]')
print(dict, "\n")

dict = {
    "name" : "DB-HDW",
    "type" : "computer",
    "element" : ["cpu", "gpu", "ram", "mainboard"]
}

del dict[input("제거할  키값 입력 : ")]
print('del dict[input("제거할 키값 입력 : ")]')
print(dict)

dict = {
    "name" : "DB-HDW",
    "type" : "computer",
    "element" : ["cpu", "gpu", "ram", "mainboard"]
}

print('asd = input("딕셔너리 이름 :")')
asd = input("딕셔너리 이름 :")
del dict[asd]
print('del dict[asd]')
print(dict)