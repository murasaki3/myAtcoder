def main():
    a, b = [int(_) for _ in input().split()]
    x1 = int(str(a) * b)
    x2 = int(str(b) * a)
    print(max(x1, x2))
main()
