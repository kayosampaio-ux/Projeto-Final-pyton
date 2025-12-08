
# MAIN DO SISTEMA INTEGRADO


# Importa funções dos módulos
from operacional.operacional import (
    cadastrar_producao,
    excluir_producao,
    calcular_total_semanal,
    calcular_media_por_dia,
    calcular_media_por_turno,
    simular_mensal_anual,
    
)

from estoque.Estoque import (
    cadastrar_produto,
    pesquisar,
    calcular_custos,
    mostrar_todos,
    alterar_produto,
    excluir_produto
)

from financeiro.Financeiro import (
    cadastrar_despesa,
    calcular_despesas,
    custo_por_carro,
    calculo_preco,
    gerar_relatorio,
    adicionar_despesa,
    excluir_despesa
)

# Banco de dados central
producoes = []         # vindo do Operacional
produtos = {}          # vindo do Estoque
despesas = {}          # vindo do Financeiro


def menu_operacional():
    while True:
        print("\n==== MÓDULO OPERACIONAL ====")
        print("1 - Cadastrar produção")
        print("2 - Excluir produção")
        print("3 - Total semanal")
        print("4 - Média por dia")
        print("5 - Média por turno")
        print("6 - Simulação (mensal/anual)")
        print("7 - Voltar")

        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_producao()
        elif opc == "2":
            excluir_producao()
        elif opc == "3":
            calcular_total_semanal()
        elif opc == "4":
            calcular_media_por_dia()
        elif opc == "5":
            calcular_media_por_turno()
        elif opc == "6":
            simular_mensal_anual()
        elif opc == "7":
            return
        else:
            print("Opção inválida.")


def menu_estoque():
    while True:
        print("\n==== MÓDULO ESTOQUE ====")
        print("1 - Cadastrar produto")
        print("2 - Atualizar produto")
        print("3 - Excluir produto")
        print("4 - Calcular custo total dos produtos")
        print("5 - Calcular custos integrados ao Operacional")
        print("6 - Voltar")

        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_produto(produtos)
        elif opc == "2":
            atualizar_produto(produtos)
        elif opc == "3":
            excluir_produto(produtos)
        elif opc == "4":
            calcular_custo_total_produtos(produtos)
        elif opc == "5":
            calcular_custos_integrado(produtos, producoes)
        elif opc == "6":
            return
        else:
            print("Opção inválida.")


def menu_financeiro():
    while True:
        print("\n==== MÓDULO FINANCEIRO ====")
        print("1 - Cadastrar despesas")
        print("2 - Gerar relatório financeiro")
        print("3 - Voltar")

        opc = input("Escolha: ")

        if opc == "1":
            global despesas
            despesas = cadastrar_despesa()
        elif opc == "2":
            if not despesas:
                print("Nenhuma despesa cadastrada.")
            else:
                qtd = int(input("Quantidade total de carros produzidos no mês: "))
                gerar_relatorio(despesas, qtd)
        elif opc == "3":
            return
        else:
            print("Opção inválida.")


# FUTURO MÓDULO RH — já preparado
def menu_rh():
    print("\n=== MÓDULO RH ===")
    print("Ainda será integrado quando o Dev terminar o módulo.")


# === MAIN PRINCIPAL ===

def main():
    while True:
        print("\n==============================")
        print(" SISTEMA DE PRODUÇÃO - FÁBRICA ")
        print("==============================")
        print("1 - Operacional (produção)")
        print("2 - Estoque")
        print("3 - Financeiro")
        print("4 - RH (em breve)")
        print("5 - Sair")

        opc = input("Escolha: ")

        if opc == "1":
            menu_operacional()
        elif opc == "2":
            menu_estoque()
        elif opc == "3":
            menu_financeiro()
        elif opc == "4":
            menu_rh()
        elif opc == "5":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")


main()