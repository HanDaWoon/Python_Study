print("원의 반지름을 입력받아 원의 둘레와 넓이를 구하는 코드를 작성해주세요.")
diameter = float(input("diameter = "))      # 반지름 입력받기
diameter_round = float(diameter*2*3.14)     # 둘레 구하기
diameter_area = float((diameter**2)*3.14)   # 넓이 구하기
print("반지름: %g, 둘레: %g, 넓이: %g" %(diameter, diameter_round, diameter_area))     # 출력하기