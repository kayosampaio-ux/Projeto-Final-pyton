# Feito por Kayo Dev1 

producao = []


def cadastrar_producao():
    print("\n--- Cadastro de Produção ---")
    
    dia = input("Digite o dia (ex: 12/03/2025): ")
    turno = input("Digite o turno (manhã / tarde / noite): ").lower()
    quantidade = int(input("Digite a quantidade produzida: "))
    semana = int(input("Digite o número da semana: "))

    registro = {
        "dia": dia,
        "turno": turno,
        "quantidade": quantidade,
        "semana": semana
    }

    producao.append(registro)
    print("\nProdução cadastrada com sucesso!")


def excluir_producao():
    print("\n=== EXCLUIR UMA PRODUÇÃO ===")

    if not producao:
        print("Nenhuma produção cadastrada.")
        return

    dia = input("Dia da produção a excluir: ")
    turno = input("Turno (manhã/tarde/noite): ").lower()

    for p in producao:
        if p["dia"] == dia and p["turno"] == turno:
            print("\nProdução encontrada:")
            print(f"Dia: {p['dia']}")
            print(f"Turno: {p['turno']}")
            print(f"Quantidade: {p['quantidade']}")

            confirmar = input("Excluir esta produção? (s/n): ").lower()
            if confirmar == "s":
                producao.remove(p)
                print("Produção excluída!")
            else:
                print("Exclusão cancelada.")
            return

    print("Nenhuma produção encontrada.")


def calcular_total_semanal():
    if not producao:
        print("\nNenhuma produção cadastrada.")
        return None

    print("\n=== CALCULAR TOTAL SEMANAL ===")
    semana = input("Digite o número da semana: ")

    try:
        semana = int(semana)
    except:
        print("Semana inválida! Digite apenas números.")
        return None

    total = 0
    for prod in producao:
        if prod["semana"] == semana:
            total += prod["quantidade"]

    if total == 0:
        print(f"Nenhuma produção encontrada na semana {semana}.")
    else:
        print(f"Total produzido na semana {semana}: {total} unidades.")

    return total 


def calcular_media_por_dia():
    if not producao:
        print("\nNenhuma produção cadastrada.")
        return

    print("\n=== CALCULAR MÉDIA POR DIA ===")
    dia = input("Digite o dia (ex: 12/03/2025): ")

    valores = [p["quantidade"] for p in producao if p["dia"] == dia]

    if not valores:
        print(f"Nenhuma produção cadastrada no dia {dia}.")
        return

    media = sum(valores) / len(valores)
    print(f"\nA média no dia {dia} foi de {media:.2f} unidades.")



def calcular_media_por_turno():
    if not producao:
        print("\nNenhuma produção cadastrada.")
        return

    print("\n=== CALCULAR MÉDIA POR TURNO ===")
    turno = input("Turno (manhã/tarde/noite): ").lower()

    valores = [p["quantidade"] for p in producao if p["turno"] == turno]

    if not valores:
        print(f"Nenhuma produção encontrada no turno '{turno}'.")
        return

    media = sum(valores) / len(valores)
    print(f"Média do turno '{turno}': {media:.2f} unidades.")


def simular_mensal_anual():
    if not producao:
        print("\nNenhuma produção cadastrada.")
        return

    print("\n=== SIMULAÇÃO MENSAL E ANUAL ===")

    quantidades = [p["quantidade"] for p in producao]
    media_geral = sum(quantidades) / len(quantidades)

    simulacao_mensal = media_geral * 30
    simulacao_anual = media_geral * 365

    print(f"Média diária geral: {media_geral:.2f}")
    print(f"Produção estimada mensal: {simulacao_mensal:.2f}")
    print(f"Produção estimada anual: {simulacao_anual:.2f}")


