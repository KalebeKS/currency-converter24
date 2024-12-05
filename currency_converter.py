print("Bem-vindo ao Conversor de Moedas!")
valor = float(input("Digite o valor em reais (BRL) que deseja converter: "))
moeda_destino = input("Digite a moeda de destino (ex: USD, EUR): ")

print(f"Você deseja converter R$ {valor:.2f} para {moeda_destino.upper()}.")
# Próximo passo: integração com API para taxa de câmbio
