price = int(input("Стоимость биткоина в рублях:"))
A = price % 1000
symbol = A // 100
print(symbol)