def obter_entrada_usuario():
    print("Bem-vindo ao Conversor de Moedas!")
    while True:
        try:
            valor = float(input("Digite o valor em reais (BRL) que deseja converter: "))
            if valor <= 0:
                print("Por favor, insira um valor maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número.")

    moeda_destino = input("Digite a moeda de destino (ex: USD, EUR): ").strip().upper()
    if not moeda_destino.isalpha() or len(moeda_destino) != 3:
        print("Moeda inválida. Certifique-se de digitar um código de moeda válido (ex: USD, EUR).")
        return obter_entrada_usuario()

    print(f"\nResumo:")
    print(f"Valor a ser convertido: R$ {valor:.2f}")
    print(f"Moeda de destino: {moeda_destino}")
    confirmar = input("Os dados estão corretos? (S/N): ").strip().lower()

    if confirmar != 's':
        print("Vamos reiniciar o processo.\n")
        return obter_entrada_usuario()

    return valor, moeda_destino

# Chamada principal
valor, moeda_destino = obter_entrada_usuario()
print(f"\nVocê deseja converter R$ {valor:.2f} para {moeda_destino}.")
print("Em breve, integração com taxas de câmbio em tempo real!")
Adiciona confirmação de dados inseridos pelo usuário
