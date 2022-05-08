import math
from cmath import sqrt



def obliczanie_pola(ciag):
    if len(ciag) == 1:
        wynik = math.pi * ciag[0] * ciag[0]
    elif len(ciag) == 2:
        wynik = ciag[0] * ciag[1]
    elif len(ciag) == 3:
        p = ((ciag[0] + ciag[1] + ciag[2]) / 2)
        wynik = math.sqrt(p * (p-ciag[0]) * (p-ciag[1]) * (p-ciag[2]))
    else:
        return "Błąd: można podać maksymalnie 3 liczby"
    return wynik



liczba_figur = int(input())
wartosc_funkcji = 0


for i in range(liczba_figur):
    boki_figury = input().strip().split()
    for j in range(len(boki_figury)):
        boki_figury[j]=float(boki_figury[j])
    pole_figury = obliczanie_pola(boki_figury)
    if type(pole_figury) is not float:
        wartosc_funkcji=pole_figury
        break
    wartosc_funkcji = round(wartosc_funkcji + pole_figury, 2)

print(wartosc_funkcji)

