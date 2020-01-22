import sys
def main():
    N, Y = [int(_) for _ in input().split()]

    for n_10k in range(N + 1):
        for n_5k in range(N - n_10k + 1):
            n_1k = N - n_10k - n_5k
            if 10000 * n_10k + 5000 * n_5k + 1000 * n_1k == Y:
                print(n_10k, n_5k, n_1k)
                sys.exit()
    print(-1, -1, -1)

main()
