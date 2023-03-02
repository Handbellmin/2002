import sys

input = sys.stdin.readline

n = int(input())

in_car = {}
out_car = {}
car_ls = []
cnt = 0
for i in range(n):
  in_car[input().rstrip()] = i
for i in range(n):
  out_car[input().rstrip()] = i

for i in out_car:
  if out_car[i] != in_car[i]:
    cnt += 1
    for j in in_car:
      if in_car[j] < in_car[i]:
        in_car[j] = in_car[j] + 1
print(cnt)
