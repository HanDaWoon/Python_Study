# 딕셔너리 선언
dict = {
    "name" : "DB-HDW",
    "type" : "computer",
    "element" : ["cpu", "gpu", "ram", "mainboard"]
}

print("딕셔너리 선언한다.\ndictionary =", dict, "\n")

print("# 출력한다.")
print("name :", dict["name"])
print("type :", dict["type"])
print("element :", dict["element"])
print()

print("# 값 바꾼다.")
dict["name"] = "DB-HDW-DT"
print('dictionary["name"] = DB-HDW-DT')
print("name :", dict["name"])