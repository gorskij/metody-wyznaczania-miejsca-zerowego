import numpy as np

def horner(wspolczynniki, rozmiar, x):
    wynik = wspolczynniki[0]
    for i in range(1, rozmiar):
        wynik = wynik * x + wspolczynniki[i]
    return wynik


def wartosc_funkcji(wybor, x):

    match wybor:
        case 1:
            wspolczynniki = [5, -2, 0, 1]  # 5x^3 - 2x^2 + 1
            return horner(wspolczynniki, len(wspolczynniki), x)
        case 2:
            return 5 * np.cos(x) - 4 * np.sin(x)  # 5cos(x) - 4sin(x)
        case 3:
            return 2 ** x - 4 ** (-2*x) - 1  # 2^x - 4^-2x - 1
        case 4:
            return np.cos(x) - 2 ** -x  # cos(x) - 2^-x

def bisekcja(wybor, a, b, epsilon=0, iteracje=0):
    if wartosc_funkcji(wybor, a) * wartosc_funkcji(wybor, b) > 0:
        print("Funkcja przyjmuje te same znaki na krancach przedzialu")
        return

    else:

        x1 = (a + b) / 2
        if epsilon != 0:
            while abs(wartosc_funkcji(wybor, x1)) > epsilon:
                iteracje += 1
                x1 = (a + b) / 2

                if wartosc_funkcji(wybor, x1) * wartosc_funkcji(wybor, a) < 0:
                    b = x1
                elif wartosc_funkcji(wybor, x1) * wartosc_funkcji(wybor, b) < 0:
                    a = x1

            print(f"Znaleziono pierwiastek rownania rowny {x1} po {iteracje} iteracjach")
            return x1

        elif iteracje != 0:
            for i in range(iteracje):
                x1 = (a + b) / 2

                if wartosc_funkcji(wybor, x1) * wartosc_funkcji(wybor, a) < 0:
                    b = x1
                elif wartosc_funkcji(wybor, x1) * wartosc_funkcji(wybor, b) < 0:
                    a = x1

            print(f"Znaleziono pierwiastek rownania rowny {x1} po {iteracje} iteracjach z dokladnoscia "
                  f"{abs(wartosc_funkcji(wybor, x1))}")
            return x1

def pochodna_funkcji(wybor, x):
    match wybor:
        case 1:
            # 5x^3 - 2x^2 + 1, pochodna x(15x−4)
            return x * (15 * x - 4)
        case 2:
            # 5cos(x)-4sin(x), pochodna -5sin(x)-4cos(x)
            return -5 * np.sin(x) - 4 * np.cos(x)
        case 3:
            # 2^x - 4^-2x - 1, pochodna ln(2)2 ** x + 2ln(4) / (4 ** (2x))
            return np.log(2) * (2 ** x) + ((2 * np.log(4)) / 4 ** (2 * x))
        case 4:
            # cos(x) - 2^-x, pochodna ln(2) / (2 ** x) - sin(x)
            return (np.log(2) / (2 ** x)) - np.sin(x)


def styczne(wybor, a, b, epsilon=0, iteracje=0):
    if wartosc_funkcji(wybor, a) * wartosc_funkcji(wybor, b) > 0:
        print("Funkcja przyjmuje te same znaki na krancach przedzialu")
        return

    x = a

    if epsilon != 0:
        while abs(wartosc_funkcji(wybor, x)) > epsilon:
            iteracje += 1

            x = x - (wartosc_funkcji(wybor, x) / pochodna_funkcji(wybor, x))

        print(f"Znaleziono pierwiastek rownania rowny {x} po {iteracje} iteracjach")
        return x

    elif iteracje != 0:
        for i in range(iteracje):
            x = x - (wartosc_funkcji(wybor, x) / pochodna_funkcji(wybor, x))

        print(f"Znaleziono pierwiastek rownania rowny {x} po {iteracje} iteracjach z dokladnoscia "
              f"{abs(wartosc_funkcji(wybor, x))}")
        return x

def funkcja_napis(wybor):
    match wybor:
        case 1:
            return "f(x) = 5x^3 - 2x^2 + 1"
        case 2:
            return "f(x) = 5cos(x) - 4sin(x)"
        case 3:
            return "f(x) = 2^x - 4^-2x - 1"
        case 4:
            return "f(x) = cos(x) - 2^-x"
