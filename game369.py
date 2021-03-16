# 3, 6, 9 게임
# 3, 6, 9가 포함된 숫자를 말할 때 박수치기 + (36, 39와 같이 두 개가 들어간 경우 박수 두 번)
# 추가) 박수 친 총 횟수 구하기
end = 100
total_clap = 0
for n in range(1, end + 1):
    s = str(n)
    if '3' in s or '6' in s or '9' in s:
        r = ""
        for c in s:
            r += "짝" if c == '3' or c == '6' or c == '9' else ""
        total_clap += r.count("짝")
        print(f"{r} ({s})")
    else:
        print(s)
print(total_clap)
