import math
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

print(n + sum(map(lambda people: math.ceil(max(0, (people - b)) / c), a)))
