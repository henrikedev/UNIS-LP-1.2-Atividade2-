def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Testa os números de 1 a 100
for i in range(1, 101):
    if eh_primo(i):
        print(f"{i} é primo")
    else:
        print(f"{i} não é primo")
