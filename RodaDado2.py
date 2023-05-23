import random

rolagem = int(input('Quantas vezes que você quer rolar os dados?'))

def dados(rolagem):
    for dado in rolagem:
        dado = random(1,6)
        
    print('O valor do dado foi: ',dado)

print(dados)