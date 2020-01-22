def main():
    N = int(input())
    A = [int(_) for _ in input().split()]
    A.sort(reverse=True)
    num = 0
    for i, a in enumerate(A,1):
        if i % 2 == 1:
            num += a
        else:
            num -= a
    print(num)
main()
