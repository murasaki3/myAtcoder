def main():
    N = int(input())
    ans = 0
    for A in range(1,N+1):
        for B in range(1,N+1):
            if str(A)[-1:] == str(B)[:1] and str(A)[:1] == str(B)[-1:]:
                ans += 1
    print(ans)
main()
