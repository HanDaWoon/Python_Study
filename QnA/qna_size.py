import sys

a = input()
b = sys.stdin.readline()

print([a], [b])

print(sys.getsizeof(a), sys.getsizeof(b))

print(type(a), type(b))

print("\n")

a = int(a)
b = int(b)

print([a], [b])

print(sys.getsizeof(int(a)), sys.getsizeof(int(b)))

print(type(a), type(b))
