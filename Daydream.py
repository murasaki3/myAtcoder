def main():
    S = input()
    while len(S) >= 5:
        if 'dream' == S[-5:]:
            S = S[:-5]
        if 'dreamer' == S[-7:]:
            S = S[:-7]
        if 'erace' == S[-5:]:
            S = S[:-5]
        if 'eraser' == S[-6:]:
            S = S[:-6]
        else:
            break
    if S == '':
        print("YES")
    else:
        print("NO")

main()
