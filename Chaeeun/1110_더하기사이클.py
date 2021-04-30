num = int(input())
result = num
cycle = 0
new = 0
temp = 0
while True:
    temp = num // 10 + num % 10
    new = (num % 10) * 10 + temp % 10 
    num = new
    cycle += 1

    if new == result:
        break

print(cycle)
