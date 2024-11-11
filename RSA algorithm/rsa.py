import random
from os import system, name

p = int(input("podaj p:"))
q = int(input("podaj q:"))
liczba = int(input("podaj liczbe do zaszyfrowania:"))

# Funkcja obliczająca NWD dla dwóch liczb
def nwd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

# Funkcja potęgowania modularnego
def power(a, n, p):
    res = 1  # Inicjalizacja wyniku
    a = a % p  # Ustawienie a w zakresie mod p
     
    while n > 0:
        if n % 2:  # Jeśli n jest nieparzyste
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p  # W przypadku parzystego n podnosimy a do kwadratu mod p
            n = n // 2
    return res % p

# Funkcja sprawdzająca, czy liczba n jest pierwsza
def is_prime(n):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(20):  # Przeprowadzenie testów dla 20 losowych liczb
            a = random.randint(2, n // 2)
            if power(a, n - 1, n) != 1:
                return False
    return True

# Funkcja obliczania odwrotności modulo n
def odwr_mod(a,n):
    p0 = 0
    p1 = 1
    a0 = a
    n0 = n
    q  = n0//a0
    r  = n0%a0
    while r > 0:
        t = p0-q*p1
        if t >= 0:
            t = t%n
        else:
            t = n-((-t)%n)
            p0 = p1
            p1 = t
            n0 = a0
            a0 = r
            q  = n0//a0
            r  = n0%a0
    return p1

# Procedura generowania kluczy RSA
def klucze_RSA(p,q):
    p, q = p, q
    phi = (p-1)*(q-1)
    n   = p*q

# wyznaczamy wykładniki e i d
    e = 3
    while nwd(e,phi) != 1:
        e += 2
    d = odwr_mod(e,phi)
    return e, d

# Funkcja oblicza a^w mod n
def pot_mod(a,w,n):
    pot,wyn,q = a,1,w
    while q > 0:
        if q%2 != 0:
            wyn = (wyn*pot)%n
        pot = (pot*pot)%n # kolejna potęga
        q //= 2
    return wyn

# Procedura kodowania danych RSA
def kodowanie_RSA():
    e, d = klucze_RSA(p, q)
    n = p * q
    t = liczba
    kod = pot_mod(t,e,n)
    
    if not is_prime(p) or not is_prime(q):
        print("podana liczba nie jest liczba prime")
        exit() 
    if liczba >= n:
        print("liczba do zaszyfrowania musi byc mniejsza niz p * q")
        exit()
    print("\nWynik kodowania =", kod)
    print("Liczba odszyfrowana =", pot_mod(kod,e,n))
    
kodowanie_RSA()