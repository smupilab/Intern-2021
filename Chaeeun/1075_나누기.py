N = int(input())
F = int(input())

N = N - (N % 100)

for i in range(100):
    if (N + i) % F == 0:
        if i < 10:
            print("0"+str(i))
            break
        else:
            print(i)
        break
