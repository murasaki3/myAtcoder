def main():
    N = int(input())
    music = []
    m_time = []
    for _ in range(N):
        a, b = input().split()
        music.append(a)
        m_time.append(int(b))
    X = input()
    ans = 0
    for i, a in enumerate(music):
        if a == X:
            for j in range(i+1, N):
                ans += m_time[j]
    print(ans)
main()
