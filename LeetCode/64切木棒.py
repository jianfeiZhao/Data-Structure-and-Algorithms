def cutRod(p, n):
  if n == 0: return 0
  q = -1
  for i in range(1, n+1):
    q = max(q, p[i-1] + cutRod(p, n-i))
  return q

def memCutRod(p, n):
  r = [-1 for i in range(n+1)]
  def memCutRodAux(p, n, r):
    if r[n] >= 0: 
      #print(r[n])
      return r[n]
    if n == 0: q =0
    else: 
      q = -1
      for i in range(1, n+1):
        q = max(q, p[i-1] + memCutRodAux(p, n-i, r))
    r[n] = q
    return q
  res = memCutRodAux(p, n, r)
  return res

def BottomUp(p, n):
  r = [0 for i in range(n+1)]
  for j in range(1, n+1):
    q = -1
    for i in range(1, j+1):
      q = max(q, p[i-1] + r[j-i])
    r[j] = q
  return r

p = [1,5,8,9,10,17,17,20,24,30]
memCutRod(p, len(p))