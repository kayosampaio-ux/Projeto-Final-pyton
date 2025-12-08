# main.py — Sistema integrado (versão compatível com os arquivos que você subiu)

# IMPORTS (use os nomes reais dos arquivos que estão na sua pasta)
from operacional.operacional import (
    cadastrar_producao,
    excluir_producao,
    calcular_total_semanal,
    calcular_media_por_dia,
    calcular_media_por_turno,
    simular_mensal_anual
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


# Bancos de dados compartilhados do MAIN
# Nota: o módulo operacional guarda sua própria lista interna de produções.
produtos = []   # lista que passamos para funções do estoque
despesas = {}   # dicionário passado para o financeiro


# ===== Menus por módulo =====

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
        print("2 - Pesquisar produto")
        print("3 - Calcular custos (por código)")
        print("4 - Mostrar todos (máx.10)")
        print("5 - Alterar produto")
        print("6 - Excluir produto")
        print("7 - Voltar")

        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_produto(produtos)
        elif opc == "2":
            pesquisar(produtos)
        elif opc == "3":
            # calcular_custos no seu módulo pede o código e retorna um dict
            resultado = calcular_custos(produtos)
            # a função calcular_custos já imprime os custos pelo que vi, mas ficamos seguros:
            if resultado is None:
                print("Cálculo não realizado (produto não encontrado).")
        elif opc == "4":
            mostrar_todos(produtos)
        elif opc == "5":
            alterar_produto(produtos)
        elif opc == "6":
            excluir_produto(produtos)
        elif opc == "7":
            return
        else:
            print("Opção inválida.")


def menu_financeiro():
    global despesas
    while True:
        print("\n==== MÓDULO FINANCEIRO ====")
        print("1 - Cadastrar despesas")
        print("2 - Gerar relatório financeiro")
        print("3 - Adicionar/Alterar despesa")
        print("4 - Excluir/Resetar despesas")
        print("5 - Voltar")

        opc = input("Escolha: ")

        if opc == "1":
            despesas = cadastrar_despesa()
        elif opc == "2":
            if not despesas:
                print("Nenhuma despesa cadastrada.")
            else:
                # pedir número de carros para cálculo (o professor pede 1000 pallets, mas o dev pede carros)
                qtd = int(input("Quantidade total de carros produzidos no mês (ex: 1000): "))
                gerar_relatorio(despesas, qtd)
        elif opc == "3":
            if not despesas:
                print("Nenhuma despesa cadastrada. Use a opção 1 para cadastrar.")
            else:
                despesas = adicionar_despesa(despesas)
        elif opc == "4":
            if not despesas:
                print("Nenhuma despesa cadastrada.")
            else:
                despesas = excluir_despesa(despesas)
        elif opc == "5":
            return
        else:
            print("Opção inválida.")


def menu_rh():
    print("\n=== MÓDULO RH ===")
    print("Módulo RH será integrado depois. Quando chegar, eu conecto aqui.")


# ===== MAIN =====
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


if __name__ == "__main__":
    main()