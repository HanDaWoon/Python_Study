import time

op = 0
tar_tk = time.time() + 5
while time.time() < tar_tk:
    op += 1

print("5초 동안 반복한 횟수 :", op)