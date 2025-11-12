def calcular_creditos(total_emissao_kg, preco_por_credito):
    total_emissao_ton = total_emissao_kg / 1000
    creditos = total_emissao_ton
    custo = creditos * preco_por_credito
    return total_emissao_ton, creditos, custo


def calcular_transporte(opcao, distancia, combustivel=None):
    opcao = (opcao or "").lower()
    if opcao == "carro":
        if not combustivel:
            raise ValueError("É preciso informar o tipo de combustível para carro.")
        combustivel = combustivel.lower()
        emissoes_por_km = {
            "gasolina": 0.192,
            "etanol": 0.12,
            "diesel": 0.171,
            "gnv": 0.165
        }
        fator = emissoes_por_km.get(combustivel)
        if fator is None:
            raise ValueError("Tipo de combustível inválido.")
    elif opcao == "moto":
        fator = 0.09
    elif opcao in ("onibus", "ônibus"):
        fator = 0.105
    elif opcao == "aviao":
        fator = 0.255
    else:
        raise ValueError("Opção de transporte não reconhecida.")
    return distancia * fator


def calcular_energia(consumo_kwh):
    try:
        consumo = float(consumo_kwh)
    except (TypeError, ValueError):
        return 0.0
    return consumo * 0.07


def calcular_gas(botijoes_mes):
    try:
        qtd = float(botijoes_mes)
    except (TypeError, ValueError):
        return 0.0
    return qtd * 33


def calcular_residuos(lixo_kg):
    try:
        lixo = float(lixo_kg)
    except (TypeError, ValueError):
        return 0.0
    return lixo * 1.5


def preco_credito(tipo_projeto):
    if not tipo_projeto:
        return 50
    tipo = tipo_projeto.lower()
    if tipo == "reflorestamento":
        return 45
    elif tipo in ("solar", "energia solar"):
        return 50
    elif tipo in ("amazonia", "conservacao"):
        return 60
    return 50
