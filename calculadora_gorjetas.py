print("--- Calculadora de gorjetas ---")
conta = float(input("Qual o valor total da conta? R$ "))
gorjeta = int(input("De quantos por cento será a gorjeta? 10, 12 ou 15? Digite apenas o número, sem sinal de porcentagem: "))
pessoas = int(input("Quantas pessoas vão dividir a conta? "))

conta_com_gorjeta = conta * (1 + gorjeta / 100)
conta_por_pessoa = conta_com_gorjeta / pessoas

print(f"Cada pessoa deve pagar R$ {conta_por_pessoa:.2f}")