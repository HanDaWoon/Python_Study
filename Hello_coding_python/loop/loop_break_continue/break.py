i = 0

while True:
    print("%d 번째 반복" %i)
    i += 1
    in_txt = input("> 종료하시겠습니까?(y): ")
    if in_txt in ["y", "Y"]:
        print("반복 종료")
        break