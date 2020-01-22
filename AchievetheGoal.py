import sys
def main():
    N, K, M = [int(_) for _ in input().split()]
    A = [int(_) for _ in input().split()]
    ans = M * N - sum(A)
    if ans < 0:
        print(0)
    elif K < ans:
        print(-1)
    else:
        print(ans)
main()
