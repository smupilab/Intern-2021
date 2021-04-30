ex = [input() for h in range(8)]
result = 0
for i in range (1, 8, 2):
    for y in range (1, 8, 2):
        if ex[i][y] == 'F':
            result += 1
for i in range (0, 8, 2):
    for x in range (0, 8, 2):
        if ex[i][x] == 'F':
            result += 1

print(result)