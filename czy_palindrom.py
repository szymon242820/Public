palindrom = input("Podaj liczbę/wyraz, który chcesz sprawdzić: ")
if str(palindrom) == str(palindrom)[::-1]:
    print(palindrom,"jest palindromem.",sep=" ")
else:
    print(palindrom,"nie jest palindromem.",sep=" ")
input("Kliknij ENTER żeby wyjść")
