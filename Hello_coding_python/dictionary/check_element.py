# 딕셔너리 선언
dict = {
    "name" : "DB-HDW",
    "type" : "computer",
    "element" : ["cpu", "gpu", "ram", "mainboard"]
}
print("딕셔너리 선언(고정) : dict =", dict, "\n")

key = input("key : ")
if  key in dict:
    print(dict[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")