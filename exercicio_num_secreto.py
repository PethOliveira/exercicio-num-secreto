"""
Criando um jogo onde o usuário precisa advinhar o número secreto
"""
import os

while True:

    try:
        num_secreto = int(input('Digite um número de 0 a 100: '))

    except ValueError:
        print('Favor digite um número inteiro válido!')
        continue

    if num_secreto > 100:
        print('número secreto está entre 0 a 100!')

    elif num_secreto < 0:
        print('número secreto está entre 0 a 100!')
    
    elif num_secreto > 22:
        os.system('cls')
        print('Número digitado é maior que o número secreto!')
        continue

    elif num_secreto < 22:
        os.system('cls')
        print('Número digitado é menor que o número secreto!')
        continue

    elif num_secreto == 22:
        print('Parabéns você acertou o número secreto!')
        break
