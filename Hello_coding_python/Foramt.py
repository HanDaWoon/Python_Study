format_out_a = "{}원".format(3000)
format_out_b = "{} {} {}".format(1, 2, 3)
format_out_c = "{} {} {}".format(1, "문자열", True)
print(format_out_a)
print(format_out_b)
print(format_out_c)

print("-"*50)

output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("#기본")
print(output_a)
print("#특정 칸에 출력하기")
print(output_b)
print(output_c)
print("#빈 칸을 0으로 채우기")
print(output_d)
print(output_e)

print("-"*50)

output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

print("#기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

print("-"*50)

output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

print("-"*50)

output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)  #15칸 만들기
output_c = "{:+15f}".format(52.273) #15칸에 부호 추가하기
output_d = "{:015f}".format(52.273) #15칸에 부호 추가하고 0으로 채우기
output_e = "{:+015f}".format(52.273) #15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)

print("-"*50)

output_f = "{:15.3f}".format(52.273)
output_g = "{:+15.2f}".format(52.273)
output_h = "{:+015.1f}".format(52.273)

print(output_f)
print(output_g)
print(output_h)

print("-"*50)

#의미없는 소수점 제거하기
output_a = 52.0
output_b = "{:g}".format(52.0)

print(output_a)
print(output_b)