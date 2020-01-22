def main():
    N = int(input())
    ans = 0
    P = [int(_) for _ in input().split()]
    for i in range(N):
        if i == 0:
            x = P[0]
        if P[i] <= x:
            ans += 1
            x = P[i]
    print(ans)
main()
