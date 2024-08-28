import string
import random

# Lista com o alfabeto
alfabeto = list(string.ascii_letters) #biblioteca string, o ascii_letters contem todos os caracteres alfabeticos

# Lista com caracteres especiais
caracteres_especiais = list("!@#$%^&*()_+-=[]{}|;':\",./<>?`~")

# Lista com números de 0 a 9
numeros = list(map(str, range(10))) # converte em string

print("===== Gerador de senhas seguras =====")
print("Selecione as quantidades de cada tipo de caracter que você deseja")
num_letras = int(input("Quantas letras?"))
num_simbolos = int(input("Quantos símbolos?"))
num_numeros = int(input("Quantos números?"))

senha_lista = []

# uma boa pratica para contadores no loop (variavel que não será usada) é utilizar o _

for _ in range(0, num_letras):
    senha_lista.append(random.choice(alfabeto))

for _ in range(0, num_simbolos):
    senha_lista.append(random.choice(caracteres_especiais))

for _ in range(0, num_numeros):
    senha_lista.append(random.choice(numeros))

print(senha_lista) # na sequencia
random.shuffle(senha_lista) # embaralhando

# Converte a senha_lista em uma string usando um loop for
senha_final = ''
for char in senha_lista:
    senha_final += char

# Também podemos converter em string usando o .join
# senha_final = ''.join(senha_lista) 

print("Senha gerada:", senha_final)

