import numpy as np

x = input("Podaj macierz Laplace'a (macierz stopni D - sąsiedztwa A) grafu (kolejno wszystkie liczby z rzędu pierwszego, później drugiego itd oddzielając je spacją): ")
y = input("Podaj wymiary tej macierzy (pierw ilość wierszy, później kolumn, oddzielone spacjami): ")

tabx = x.split(" ")
dimy = y.split(" ")

for a in range(len(tabx)):
    tabx[a] = int(tabx[a])
for b in range(len(dimy)):
    dimy[b] = int(dimy[b])

macierz = np.array(tabx).reshape(dimy[0], dimy[1])
macierz = np.delete(macierz, (0), axis=0)
macierz = np.delete(macierz, (0), axis=1)

print("Ilość drzew spinających tego grafu wynosi:",str(int(np.linalg.det(macierz))), sep=" ")
input("Kliknij ENTER żeby wyjść")