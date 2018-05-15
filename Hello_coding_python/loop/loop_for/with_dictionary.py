# 딕셔너리 선언
dict = {
    "name" : "DB-HDW",
    "type" : "computer",
    "element" : ["cpu", "gpu", "ram", "mainboard"]
}
print("딕셔너리 선언(고정) : dict =", dict, "\n")

"""for <키 변수> in <딕셔너리>:
        <코드>
"""

for key in dict:
    print(key, ":", dict[key])