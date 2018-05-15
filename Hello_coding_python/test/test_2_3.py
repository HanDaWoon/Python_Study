print("# inch 단위를 입력받아 cm 단위를 구하는 코드를 작성해 주세요(1inch=2.54cm)")

inch = int(input("inch = "))        # inch 단위를 정수로 입력받기
cm = inch*2.54                      # cm 단위 구하기
print("%dinch = %scm" %(inch, cm))  # 출력