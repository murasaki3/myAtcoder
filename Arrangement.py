def main():
    N = int(input())
    a = []
    for _ in range(N):
        a.append(int(input))
    ans = str(range(1,N+1))
    for i in range(N+1):
        if str(i+1) in ans == a[i]:
            ans[i+1], ans[i+2] = ans[i+2], ans[i+1]
    print(ans)

main()
