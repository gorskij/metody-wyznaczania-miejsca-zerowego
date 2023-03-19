import matplotlib.pyplot as plt
from metody import *

def rysuj(wybor, a, b, miejsce_zerowe):
    x = np.arange(a, b, 0.1)
    y = wartosc_funkcji(wybor, x)

    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.axhline(y=0, color="#cccccc")
    plt.axvline(x=0, color="#cccccc")
    plt.xticks([i for i in range(int(-b), int(b), 1)])

    plt.plot(x, y)
    plt.scatter(miejsce_zerowe, 0, c="red", marker="*", s=50)
    plt.title(funkcja_napis(wybor))
    plt.show()
