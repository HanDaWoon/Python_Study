input_year = int(input("태어난 년도:"))      # 태어난 년도 정수형으로 입력받기
year = input_year % 12                      # 입력받은 년도를 12로 나누기
if year == 0:
    print("원숭이띠입니다.")
elif year == 1:
    print("닭띠입니다.")
elif year == 2:
    print("개띠입니다")
elif year == 3:
    print("돼지띠입니다.")
elif year == 4:
    print("쥐띠입니다.")
elif year == 5:
    print("소띠입니다.")
elif year == 6:
    print("범띠입니다.")
elif year == 7:
    print("토끼띠입니다.")
elif year == 8:
    print("용띠입니다.")
elif year == 9:
    print("뱀띠입니다.")
elif year == 10:
    print("말띠입니다.")
else:
    print("양띠입니다.")