def eh_primo(k):
    primo = True
    divisor = 2
    while (divisor < k):
        if (k % divisor != 0):
            divisor += 1
        else:
            primo = False
            break
    return primo

def maior_primo(n):
    k = n
    while ((k >= 2) and (eh_primo(k) == False)):
        k -= 1
    return k
