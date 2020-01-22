import sys
def main():
    N, K, S = [int(_) for _ in input().split()]
    A = []
    if K == 0:
        A = [S+1] * N
        print(*A)
        sys.exit()
    for i in range(N):
        if i < K:
            A.append(S)
        else:
            A.append(S+1)
    print(*A)
main()
