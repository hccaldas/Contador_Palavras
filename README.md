# Contador de Palavras em Python

Este repositório contém um script em Python que realiza várias análises em um texto fornecido pelo usuário, incluindo contagem de palavras, caracteres, frases, palavras únicas e palavras mais frequentes.

## Funcionalidades

- Contagem de palavras em um texto.
- Contagem de caracteres em um texto.
- Contagem de frases em um texto.
- Contagem de palavras únicas em um texto.
- Exibição das palavras mais frequentes em um texto.

## Pré-requisitos

- Python 3.x

## Como usar

1. Clone este repositório ou copie o código para o seu ambiente local.
2. Certifique-se de ter o Python 3.x instalado no seu sistema.
3. Execute o script.
4. Insira o texto quando solicitado.
5. O script exibirá os resultados das análises realizadas no texto.

## Exemplo de Uso

```python
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
        if palavra em frequencia:
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
