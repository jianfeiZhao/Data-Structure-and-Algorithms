import random
import matplotlib.pyplot as plt

def test(n, m):   # n: number of people, m: number of transactions
    i = 0
    ls_init = [100 for i in range(n)]
    ls = ls_init
    while i < m:
        id1 = random.randint(0, n-1)
        ls[id1] -= 2
        id2 = random.randint(0, n-1)
        ls[id2] += 2
        i += 1
    
    plt.plot(n*[100])
    plt.plot(ls, 'g^')
    plt.show()

test(10000, 10000)