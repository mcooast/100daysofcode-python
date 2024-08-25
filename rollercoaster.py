print("==============================")
print("   V Ó R T E X   A É R E O   ")
print("==============================")

altura = int(input("Vamos ver se você tem altura o suficiente para andar na montanha-russa. Qual sua altura em cm? "))

if altura > 120:
    print("Prepare-se para uma aventura emocionante de tirar o fôlego. Segure-se firme e divirta-se!")
    idade = int(input("Para saber o valor do seu ingresso, informe a sua idade: "))
    
    if idade < 12:
        print("Seu ingresso custa R$5,00")
        conta = 5
    elif 12 <= idade < 18:
        print("Seu ingresso custa R$7,00")
        conta = 7
    elif 45 <= idade <= 55:
        print("Parabéns! Você não paga ingresso!")
        conta = 0
    elif idade >= 18:
        print("Seu ingresso custa R$12,00")
        conta = 12

    fotos = input("Para encerrar, você vai querer fotos dessa aventura? Digite S para sim e N para não: ")
    if fotos.upper() == "S":
        conta_final = conta + 3
        print(f"O total de sua conta foi R${conta_final:.2f}")
    else:
        print(f"O total de sua conta foi R${conta:.2f}")

else:
    print("Infelizmente, você ainda não tem a altura necessária para embarcar no Vórtex Aéreo. Continue crescendo, e logo você estará pronto(a) para essa aventura incrível!")