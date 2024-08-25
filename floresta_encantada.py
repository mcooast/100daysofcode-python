def enchanted_forest():
    # Arte ASCII - https://ascii.co.uk/art/tree
    print("""
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\\88/8o
   ,%&\\%&&%&&%,@@@\\@@@/@@@88\\88888/88'
   %&&%&%&/%&&%@@\\@@/ /@@@88888\\88888'
   %&&%/ %&%%&&@@\\ V /@@' `88\\8 `/88'
   `&%\\ ` /%&'   |.|        \\ '|8'
       |o|        | |         | |
       |.|        | |         | |
\\_ \\/ ._\\//_/_/  ,\\_//__\\/ .\\_//""")

    print("Bem-vindo à Floresta Encantada! Está pronto(a) para essa aventura?")
    print("Sua missão é encontrar a saída da floresta.")

    choice1 = input("Você encontra uma trifurcação. Por onde você vai seguir? Trilha sombria, trilha iluminada ou trilha coberta de névoa? ").lower()

    if choice1 == "trilha sombria":
        print("Você foi capturado por criaturas da escuridão. Fim de jogo.")
        return
    elif choice1 == "trilha iluminada":
        choice2 = input("Você encontra um rio. Deseja construir uma balsa, procurar uma ponte ou tentar nadar? ").lower()

        if choice2 == "construir balsa":
            print("Sua balsa não era resistente e você se afogou. Fim de jogo.")
            return
        elif choice2 == "procurar ponte":
            choice3 = input("Você encontra uma velha cabana. Deseja entrar, seguir em frente, ou explorar ao redor? ").lower()

            if choice3 == "entrar":
                print("A cabana estava amaldiçoada. Você ficou preso para sempre. Fim de jogo.")
                return
            elif choice3 == "seguir em frente":
                print("Você encontrou a saída da floresta. Parabéns!")
                return
            elif choice3 == "explorar ao redor":
                print("Você encontrou um mapa secreto que mostra a saída. Parabéns!")
                return
            else:
                print("Escolha inválida. Fim de jogo.")
                return
        elif choice2 == "tentar nadar":
            print("Você foi pego por uma correnteza forte. Fim de jogo.")
            return
        else:
            print("Escolha inválida. Fim de jogo.")
            return
    elif choice1 == "trilha coberta de névoa":
        choice2 = input("A névoa fica mais densa. Deseja continuar, retornar, ou acender uma tocha? ").lower()

        if choice2 == "continuar":
            print("Você se perdeu na névoa e nunca mais foi visto. Fim de jogo.")
            return
        elif choice2 == "retornar":
            print("Você voltou ao início da floresta e está seguro, mas não encontrou a saída. Fim de jogo.")
            return
        elif choice2 == "acender tocha":
            choice3 = input("A tocha revela uma trilha secreta. Deseja segui-la ou apagar a tocha e continuar na névoa? ").lower()

            if choice3 == "segui-la":
                print("A trilha secreta leva você a uma clareira segura e pode sair da floresta. Parabéns, você sobreviveu!")
                return
            elif choice3 == "apagar a tocha":
                print("Você se perdeu na névoa e nunca mais foi visto. Fim de jogo.")
                return
            else:
                print("Escolha inválida. Fim de jogo.")
                return
        else:
            print("Escolha inválida. Fim de jogo.")
            return
    else:
        print("Escolha inválida. Fim de jogo.")
        return

enchanted_forest()
