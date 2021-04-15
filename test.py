inp = input().split('\n')
for line in inp:
    n, m = line.split(' ')
    n, m = int(n), int(m)
    for i in range(m):
        res = n + round(n**0.5, 2)
    print(round(res,2))