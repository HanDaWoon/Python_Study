print("킬로그램(kg) 단위를 입력받아 파운드(pound) 단위를 구하는 코드를 작성해주세요(1kg = 2.20462262pound).")
kg = int(input("kg = "))                # kg 단위를 정수로 입력받기
pound = kg*2.20462262                   # pound 단위 구하기
print("%dkg = %spound" %(kg, pound))    # 출력하기