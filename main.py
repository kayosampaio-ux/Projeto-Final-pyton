# main.py - (mini-ERP)

from rh.rh import menu as menu_rh
from operacional.operacional import menu as menu_operacional
from estoque.estoque import menu as menu_estoque
from financeiro.financeiro import menu as menu_financeiro

def main():
    while True:
        print("\n" + "="*40)
        print("  MINI-ERP SIMPLES - Produção")
        print("="*40)
        print("1 - RH")
        print("2 - Operacional")
        print("3 - Estoque")
        print("4 - Financeiro")
        print("0 - Sair")
        op = input("Escolha: ").strip()
        if op == "1":
            menu_rh()
        elif op == "2":
            menu_operacional()
        elif op == "3":
            menu_estoque()
        elif op == "4":
            menu_financeiro()
        elif op == "0":
            print("Tchau! Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "_main_":
    main()