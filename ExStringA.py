texto = input("Informe uma texto: ")

#deixamos por padrão escolhido minuscula para diminuir a contagem dos casos 'A' para 'a'
contagem_a = texto.lower().count('a')

if contagem_a > 0:
    print(f"A letra 'a' aparece {contagem_a} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
