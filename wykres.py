import matplotlib.pyplot as plt
from metody import *

def rysuj(wybor, a, b, miejsce_zerowe_bisekcja, miejsce_zerowe_styczne):
    x = np.arange(a, b, 0.1)
    y = wartosc_funkcji(wybor, x)

    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.axhline(y=0, color="#cccccc")
    plt.axvline(x=0, color="#cccccc")
    plt.xticks([i for i in range(int(-b), int(b), 1)])

    plt.plot(x, y)
    plt.title(funkcja_napis(wybor)+f"\nMiejsce zerowe bisekcja: {miejsce_zerowe_bisekcja}\n"
                                   f"  Miejsce zerowe styczne: {miejsce_zerowe_styczne}")

    b = plt.scatter(miejsce_zerowe_bisekcja, 0, c="red", marker="*", s=50)
    s = plt.scatter(miejsce_zerowe_styczne, 0, c="green", marker="*", s=50)

    plt.legend((b, s), ("Bisekcja", "Styczne"), loc="upper left")

    plt.show()
