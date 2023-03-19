from metody import *
from wykres import rysuj

while True:
    print("-------------------------------------------------------")
    print("1. Funkcja wielomianowa (f(x) = 5x^3 - 2x^2 + 1)")
    print("2. Funkcja trygonometryczna (f(x) = 5cos(x) - 4sin(x))")
    print("3. Funkcja wykladnicza (f(x) = 2^x - 4^-2x - 1)")
    print("4. Funkcja wielomianowa (f(x) = cos(x) - 2^-x)")
    print("5. Wyjdz")
    print("-------------------------------------------------------")

    poziom = True
    wybor = int(input("Wybor: "))
    if wybor == 5:
        quit(0)

    a, b = [int(i) for i in input("Okresl przedzial poszukiwania: ").split()]
    iteracje = False

    print("Wybierz kryterium stopu")
    print("1. Dokladnosc")
    print("2. Iteracje")

    warunek = int(input("Wybor: "))
    wartosc = 0.1
    match warunek:
        case 1:
            wartosc = float(input("Podaj epsilon: "))
        case 2:
            wartosc = int(input("Podaj liczbe iteracji: "))
            iteracje = True
        case _:
            print("Bledny warunek!\nDomyslnie epsilon=0.1")

    x1 = 0
    x2 = 0
    if iteracje:
        print("Metoda bisekcji")
        x1 = bisekcja(wybor, a, b, iteracje=wartosc)
        print("Metoda stycznych")
        x2 = styczne(wybor, a, b, iteracje=wartosc)
    else:
        print("Metoda bisekcji")
        x1 = bisekcja(wybor, a, b, epsilon=wartosc)
        print("Metoda stycznych")
        x2 = styczne(wybor, a, b, epsilon=wartosc)

    rysuj(wybor, a, b, x1)
    rysuj(wybor, a, b, x2)




