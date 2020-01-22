def main():
    N, A, B = [int(_) for _ in input().split()]
    ans = 0
    sum_ = 0
    for i in range(1, N + 1):
        sum_ = sum(map(int, list(str(i))))
        if A <= sum_ <= B:
            ans = ans + i

    print(ans)

main()
