import requests
from api_config import API_BASE_URL

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

    return valor, moeda_destino

def converter_moeda(valor, moeda_destino):
    print("Obtendo taxas de câmbio...")
    try:
        response = requests.get(f"{API_BASE_URL}BRL")
        if response.status_code != 200:
            print("Erro ao acessar a API. Tente novamente mais tarde.")
            return None

        taxas = response.json().get("rates", {})
        taxa_conversao = taxas.get(moeda_destino)

        if not taxa_conversao:
            print(f"A moeda {moeda_destino} não é suportada.")
            return None

        valor_convertido = valor * taxa_conversao
        return valor_convertido

    except Exception as e:
        print(f"Erro: {e}")
        return None

# Chamada principal
valor, moeda_destino = obter_entrada_usuario()
resultado = converter_moeda(valor, moeda_destino)

if resultado:
    print(f"\nR$ {valor:.2f} é igual a {moeda_destino} {resultado:.2f}.")
else:
    print("Não foi possível realizar a conversão.")
