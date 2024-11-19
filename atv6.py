texto = "Esta é uma frase com algumas palavras longas e curtas."

palavras_com_mais_de_3_letras = [
    palavra for palavra in texto.split() if len(palavra) > 3]

print(palavras_com_mais_de_3_letras)
