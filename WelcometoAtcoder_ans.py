N, M = list(map(int, input().split()))
correct = 0
incorrect = 0
Q = [0] * N
num_WA = [0] * N
for i in range(M):
    s, t = input().split()
    s = int(s)

    if t == 'AC':
        if Q[s-1] == 1:
            continue
        else:
            Q[s-1] = 1
            correct += 1
            incorrect += num_WA[s-1]
    else:
        num_WA[s-1] += 1
print(correct, incorrect)
