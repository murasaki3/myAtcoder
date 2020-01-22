def main():
    N = int(input())
    d = []
    for _ in range(N):
        d.append(int(input()))

    count = 0
    ex_a = 0
    d.sort()

    for i, a in enumerate(d):
        if a != ex_a:
            count += 1
        ex_a = a

    print(count)

main()
