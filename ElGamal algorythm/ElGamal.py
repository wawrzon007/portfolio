import math
import random

numTrials=20

def power(a, n, p):
    res = 1
    a = a % p 
     
    while n > 0:
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2
             
    return res % p
     
def isPrime(n, k):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
     
    else:
        for i in range(k):
            a = random.randint(2, n - 2)
             
            if power(a, n - 1, n) != 1:
                return False
                 
    return True

q= 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668163451
p= 21430172143725346418968500981200036211228096234110672148875007767407021022498722449863967576313917162551893458351062936503742905713846280871969155149397149607869135549648461970842149210124742283755908364306092949967163882534797535118331087892154125829142392955373084335320859663305248773674411336326903

def find(q,k):
    while(1):
        p = 2*q + 1
        if(isPrime(q,k)):
            if(isPrime(p,k)):
                g = random.randrange(1,p)
                if(g^2==1):
                    continue
                if(power(g,q,p)==1):
                    continue
                x = random.randrange(1,p-1)
                y = power(g,x,p)
                print("sukces")
                print("klucz publiczny")
                print(f"p: {p}")
                print(f"g: {g}")
                print(f"y: {y}")
                print("klucz tajny")
                print(f"p: {p}")
                print(f"x: {x}")
                break
        q += 1
    return p, g, y, x
    
p, g, y, x = find(q,numTrials)
def szyfrowanie(p, g, y):
    k = random.randrange(1, p-1)  # Losowa wartość k
    wiadomosc = int(input("podaj liczbe do zaszyfrowania: "))
    c1 = power(g, k, p)  # c1 = g^k mod p
    c2 = (wiadomosc * power(y, k, p)) % p  # c2 = m * y^k mod p
    print(f"\nc1= {c1}")
    print(f"c2= {c2}")
    return (c1, c2)

def odszyfrowanie(p, x, c1, c2):
    s = power(c1, x, p)  # s = c1^x mod p
    s_inv = power(s, p - 2, p)  # Inwersja s mod p
    m = (c2 * s_inv) % p  # m = c2 * s^-1 mod p
    print(f"odszyfrowana wiadomosc= {m}")
    return m
    
c1, c2 = szyfrowanie(p, g, y)
m = odszyfrowanie(p, x, c1, c2)