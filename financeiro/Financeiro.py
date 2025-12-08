# financeiro.py
# Autor: Davi
# Objetivo: Calcular despesas, custo e preço de venda dos carros. 

 # === MÓDULO FINANCEIRO ===

def cadastrar_despesa():
    print("=== CADASTRO DE DESPESAS ===")
    agua = float(input("Gasto com água: R$ "))
    luz = float(input("Gasto com luz: R$ "))
    salarios = float(input("Gasto com salários: R$ "))
    impostos = float(input("Gasto com impostos: R$ "))
    
    despesas = {"agua": agua, "luz": luz, "salarios": salarios, "impostos": impostos }
    
    return despesas


def calcular_despesas(despesas):
    """Soma todas as despesas cadastradas."""
    return sum(despesas.values())


def custo_por_carro(total_despesa, quantidade_carros):
    """Calcula o custo unitário de produção."""
    if quantidade_carros <= 0:
        print("ERRO: quantidade de carros inválida.")
        return 0
    
    return total_despesa / quantidade_carros


def calculo_preco(custo_unitario):
    """Aplica margem de 50% no preço final."""
    return custo_unitario * 1.5


def gerar_relatorio(despesas, quantidade_carros):
    """Gera o relatório financeiro completo."""
    print("=== RELATÓRIO FINANCEIRO ===")

    total = calcular_despesas(despesas)
    custo_unitario = custo_por_carro(total, quantidade_carros)
    preco_final = calculo_preco(custo_unitario)

    print(f"Total de despesas: R$ {total:.2f}")
    print(f"Custo por carro: R$ {custo_unitario:.2f}")
    print(f"Preço final de venda: R$ {preco_final:.2f}")


def adicionar_despesa(despesas):
    """Atualiza o valor de uma despesa existente."""
    nome = input("Nome da despesa (agua, luz, salarios, impostos): ").lower()
    
    if nome not in despesas:
        print("ERRO: despesa inválida.")
        return despesas
    
    valor = float(input(f"Informe o novo valor para {nome}: R$ "))
    despesas[nome] = valor
    print(f"Despesa '{nome}' atualizada com sucesso.\n")
    
    return despesas


def excluir_despesa(despesas):
    """Exclui uma despesa específica ou todas."""
    print("=== EXCLUIR DESPESA ===")
    print("1 - Excluir uma despesa específica")
    print("2 - Excluir todas as despesas")
    print("3 - Adicionar/Alterar despesa")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome da despesa para excluir: ").lower()
        if nome in despesas:
            del despesas[nome]
            print("Despesa excluída.")
        else:
            print("Despesa não encontrada.")
    
    elif opcao == "2":
        despesas.clear()
        print("Todas as despesas foram excluídas.")
    
    elif opcao == "3":
        despesas = adicionar_despesa(despesas)
    
    else:
        print("Opção inválida.")
    
    return despesas


