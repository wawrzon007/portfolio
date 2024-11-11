# Ustawienie stałych: p, A, B - wartości dla krzywej eliptycznej i punktów początkowych x1, y1, x2, y2.
p = 1183779584357076950937981497685946292711107412152534481102525547387604378262522402526266939
A = 239614427021073265587611886177902927263167863041565491257781227550405368115731464059190159
B = 447169285435982716467332439542997876345372330045685811964291613238129105735899852114277221
x1 = 18502295139256450820121679356081497119432285113022537352112212036328455845849821450355002
y1 = 47492217188301824000488054823300402924752658536899228863428280125642987844856092219548145
x2 = 259006325058733656579981790086212961218595267783766744626221411546527039150439907991842
y2 = 298134427471212122333857075721955719744082245593493662016782994577775855296458731751986286

# Ustawienie maksymalnej liczby rekurencji (przydatne dla dużych operacji).
import sys
sys.setrecursionlimit(10**9)

import random

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
def isPrime(n, k):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(k):  # Przeprowadzenie testów dla k losowych liczb
            a = random.randint(2, n // 2)
            if power(a, n - 1, n) != 1:
                return False
    return True

# Funkcja wyliczająca równania krzywej eliptycznej dla punktów (x1, y1) i (x2, y2)
def find_E(A, B, x1, x2, y1, y2):
    E1 = pow(x1,3) + A*x1 + B
    E2 = pow(x2,3) + A*x2 + B
    return E1, E2, pow(y1,2), pow(y2,2)

# Znajdowanie losowej liczby pierwszej xBob w zakresie p//2
while(1):
    xBob = random.randint(0, p // 2)
    if isPrime(xBob, 20):
        break  # Jeśli xBob jest liczbą pierwszą, wychodzimy z pętli

# Funkcja obliczająca rozszerzony algorytm Euklidesa
def ext_gcd(a, b):
    a0, a1 = a, b
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while a1 != 0:
        q = a0 // a1
        r, s, t = a1, x1, y1
        a1 = a0 % a1
        x1 = x0 - q * x1
        y1 = y0 - q * y1
        a0, x0, y0 = r, s, t

    return x0, y0, a0

# Funkcja obliczająca odwrotność modularną liczby a modulo mod
def inverse_mod(a, mod):
    va, y0, a0 = ext_gcd(a, mod)
    return va % mod

# Wykonywanie operacji double-and-add dla mnożenia punktu przez skalarną wartość xBob
n = xBob
while n > 0:
    if n % 2 == 1:  # Operacja dodawania punktu dla nieparzystego n
        if x1 == x2 and y1 == y2:  # Jeśli punkty są równe
            alfa = (((3 * pow(x2, 2)) + A) * inverse_mod(2 * y2, p)) % p  # Wylicz alfa
            x3 = (pow(alfa, 2) - (2 * x2)) % p
            y3 = (alfa * (x2 - x3) - y2) % p
            n -= 1
        elif x1 == x2 and y1 != y2:  # Punkty są przeciwne
            x3 = 0
            y3 = 0
            n -= 1
        else:  # Obliczenie sumy dwóch punktów różniących się od siebie
            alfa = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p
            x3 = (alfa ** 2 - x1 - x2) % p
            y3 = (alfa * (x1 - x3) - y1) % p
        x1 = x3  # Aktualizacja współrzędnych punktu x1, y1
        y1 = y3
        n -= 1
    else:  # Operacja podwojenia punktu dla parzystego n
        alfa = (((3 * pow(x2, 2)) + A) * inverse_mod(2 * y2, p)) % p
        x3 = (pow(alfa, 2) - 2 * x2) % p
        y3 = (alfa * (x2 - x3) - y2) % p
        x1 = x3  # Aktualizacja współrzędnych punktu x2, y2
        y1 = y3
        n = n // 2

# Wyświetlenie wyników
print("xBob= " + str(xBob))
print("x3= " + str(x3))
print("y3= " + str(y3))
