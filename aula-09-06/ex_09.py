def fat(n, res):
    if n==0:
        return res
    res = res * n
    return fat(n - 1, res)

fatorial = fat(5,1)

print(fatorial)