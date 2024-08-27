import random

# Artes ASCII para as opções
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lista de opções
opcoes = [pedra, papel, tesoura]

# Entrada do jogador
print("Vamos jogar! O que você escolhe? Digite 0 para pedra, 1 para papel e 2 para tesoura")
escolha_jogador = int(input())

# Escolha do computador
escolha_pc = random.choice([0, 1, 2])

# Exibir as jogadas
print("Sua jogada foi:")
print(opcoes[escolha_jogador])

print("A jogada do computador foi:")
print(opcoes[escolha_pc])

# Determinar o resultado
if escolha_jogador == escolha_pc:
    print("Empate!")
elif (escolha_jogador == 0 and escolha_pc == 2) or (escolha_jogador == 1 and escolha_pc == 0) or (escolha_jogador == 2 and escolha_pc == 1):
    print("Você ganhou!")
else:
    print("Você perdeu!")