import functools

lines = input().split('\\n')
#print(lines)
l1 = lines[0].split(' ')
N, M, T = list(map(int, l1))
mat = []
for i in range(N):
    mat.append(list(map(int, lines[i+1].split(' '))))
ops = lines[-T:]
print(mat)
for op in ops:
    op = list(map(int, op.split(' ')))
    r1, r2, c1, c2, s, A = op
    tmp = []
    for i in range(r1-1, r2):
        tmp.append(mat[i][c1-1:c2])
    print(tmp)
    if A == 1:
        tmp.sort(key = functools.cmp_to_key(lambda x, y: 1 if x[s-c1]<y[s-c1] else -1))
    else:
        tmp.sort(key = functools.cmp_to_key(lambda x, y: 1 if x[s-c1]>y[s-c1] else -1))
    print(tmp)
    for i in range(r1-1,r2):
        mat[i][c1-1:c2] = tmp[i-r1+1]
for i in mat:
    out = ''
    for j in i:
        out = out + str(j) + ' '
    print(out[:-1])
#4 4 1\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n2 3 2 3 3 1