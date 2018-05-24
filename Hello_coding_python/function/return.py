# 리턴 기본
def return_test():
    print("A 위치")
    return
    print("B 위치")

return_test()

# 자료와 함께 리턴
def return_test():
    return 100

value = return_test()
print(value)