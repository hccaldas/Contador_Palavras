def contador_palavras(texto):
    palavras = texto.split()
    return len(palavras)

# entrada de texto
texto = input("Digite um texto: ")

# exibir resultado da função contador_palavras
print(f"O texto tem {contador_palavras(texto)} palavras.")

def contador_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def contador_caracteres(texto):
    return len(texto)

def contador_frases(texto):
    frases = texto.split('.')
    return len([frase for frase in frases if frase.strip()])

def contador_palavras_unicas(texto):
    palavras = texto.split()
    palavras_unicas = set(palavras)
    return len(palavras_unicas)

def palavras_mais_frequentes(texto, n=5):
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    palavras_frequentes = sorted(frequencia.items(), key=lambda item: item[1], reverse=True)
    return palavras_frequentes[:n]

# entrada de texto
texto = input("Digite um texto: ")

# exibir resultados das funções
print(f"O texto tem {contador_palavras(texto)} palavras.")
print(f"O texto tem {contador_caracteres(texto)} caracteres.")
print(f"O texto tem {contador_frases(texto)} frases.")
print(f"O texto tem {contador_palavras_unicas(texto)} palavras únicas.")
print(f"As palavras mais frequentes são: {palavras_mais_frequentes(texto)}")