primesL = []
avg = []
results = []
done = []

num = int(input())
for i in range(num):
    avg.append(int(input()))
'''for i in range(4, 1000):
    avg.append(i)'''
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

for n in avg:
    ne = n * 2
    for i in range(1, ne + 1):
        '''if n in done:
            break'''
        if(len(primes(i)) == 1):
            if(len(primes(ne - i)) == 1):
                results.append([i, ne-i])
                done.append(n)
                break

for i in results:
    for j in i:
        print(j, end='')
        print(' ', end='')
    print('')