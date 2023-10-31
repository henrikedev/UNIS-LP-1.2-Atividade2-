def calcular_idade(dias):
    anos = dias // 365
    meses = (dias % 365) // 30
    dias = (dias % 365) % 30
    return anos, meses, dias

dias = int(input("Digite a idade em dias: "))

anos, meses, dias = calcular_idade(dias)

print(f"A idade é: {anos} anos, {meses} meses e {dias} dias.")
