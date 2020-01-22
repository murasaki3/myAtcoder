import sys
def main():
    N = int(input())
    A = [int(_) for _ in input().split()]
    count = 0

    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            else:
                print(count)
                sys.exit()
        count += 1

main()
