# SOlicitar numero n y calcular n + nn + nnn

# n=3 -> 3 + 33 + 333

n= input('Numero:')

total = int(n) + int(n+n) + int(n+n+n)
print(total)