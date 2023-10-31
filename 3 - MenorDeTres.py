def encontrar_menor_numero(a, b, c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor

# Solicita ao usuário que insira os três números inteiros
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

# Chama a função para encontrar o menor número
menor_numero = encontrar_menor_numero(a, b, c)

# Exibe o menor número
print(f"O menor número é: {menor_numero}")
