def main():
    N, A, B = [int(_) for _ in input().split()]
    ans = 0
    for i in range(N + 1):
        j = i
        sum_ = 0
        while j != 0:
            sum_ = sum_ + (j % 10)
            j = j // 10

        if A <= sum_ <= B:
            ans = ans + i

    print(ans)

main()
