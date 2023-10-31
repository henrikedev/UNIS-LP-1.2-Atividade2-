def inverter_letras(frase):
    palavras = frase.split()  # Separa a frase em uma lista de palavras
    frase_invertida = ""

    for palavra in palavras:
        palavra_invertida = palavra[::-1]  # Inverte a ordem das letras da palavra
        frase_invertida += palavra_invertida + " "  # Adiciona a palavra invertida à frase resultante

    return frase_invertida.strip()  # Remove o espaço extra no final da frase

# Exemplo de uso
frase_original = str(input("Digite uma frase: "))
frase_invertida = inverter_letras(frase_original)

print(f"Frase original: {frase_original}")
print(f"Frase com letras invertidas: {frase_invertida}")
