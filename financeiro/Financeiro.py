# financeiro.py
# DEV 3 : Davi
# Objetivo: Calcular despesas, custo e preço de venda dos carros. 

import os, json
ARQUIVO = "database/financeiro.json"

"""Garante que o arquivo e pasta existam"""
def garantir_arquivo():
    os.makedirs("database", exist_ok=True)
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump({"despesas": [], "producao": []}, f, indent=2)

"""Carrega o dicionário financeiro"""
def carregar():
    garantir_arquivo()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

"""Salva o dicionário atualizado"""
def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def cadastrar_despesa():
    financeiro = carregar()
    print("=== Cadastrar Despesa ===")
    tipo = input("Tipo (agua/luz/compra/folha/outros): ").strip()
    
    try:
        valor = float(input("Valor (R$): ").strip() or 0)
    except ValueError:
        print("Valor inválido. Registrando como 0.")
        valor = 0
        
    financeiro["despesas"].append({"tipo": tipo, "valor": valor})
    salvar(financeiro)
    print("Despesa registrada.")


def excluir_despesa():
    financeiro = carregar()

    if not financeiro["despesas"]:
        print("Nenhuma despesa cadastrada.")
        return

    print("=== EXCLUIR OU ADICIONAR DESPESA ===")
    print("1 - Excluir despesa específica")
    print("2 - Adicionar uma despesa específica (rápido)")
    print("3 - Excluir todas as despesas")
    print("0 - Cancelar")
    op = input("Escolha: ").strip()

    
    if op == "1":
        print("Despesas cadastradas:")
        for i, d in enumerate(financeiro["despesas"]):
            print(f"{i} - {d['tipo']} | R${d['valor']:.2f}")

        try:
            indice = int(input("Informe o índice da despesa para excluir: ").strip())
            if 0 <= indice < len(financeiro["despesas"]):
                removido = financeiro["despesas"].pop(indice)
                salvar(financeiro)
                print(f"Despesa '{removido['tipo']}' removida.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida.")

    elif op == "2":
        tipo = input("Tipo da despesa: ").strip()
        try:
            valor = float(input("Valor (R$): ").strip())
        except ValueError:
            print("Valor inválido. Registrado como 0.")
            valor = 0

        financeiro["despesas"].append({"tipo": tipo, "valor": valor})
        salvar(financeiro)
        print("Despesa adicionada.")

    elif op == "3":
        print("ATENÇÃO: Esta operação removerá todas as despesas cadastradas.")
        confirma = input("Confirma exclusão de todas as despesas? (s/N): ").strip().lower()
        if confirma == "s" or confirma == "sim":
            financeiro["despesas"] = []
            salvar(financeiro)
            print("Todas as despesas foram removidas.")
        else:
            print("Operação cancelada. Nenhuma despesa foi removida.")

    elif op == "0":
        return
    else:
        print("Opção inválida.")



def calcular_total_despesas():
    financeiro = carregar()
    total = sum(item["valor"] for item in financeiro["despesas"])
    print(f"Total despesas: R${total:.2f}")
    return total

def registrar_custo_producao(qtd):
    """Usado pelo módulo Operacional para registrar uma produção."""
    financeiro = carregar()
    financeiro["producao"].append({"qtd": qtd})
    salvar(financeiro)

def gerar_relatorio():
    # IMPORTAÇÕES LOCAIS: Evita dependência circular
    from rh.rh import carregar as rh_carregar
    from estoque.estoque import carregar as estoque_carregar
    from operacional.operacional import carregar as producao_carregar
    
    financeiro = carregar()
    print("\n=== RELATÓRIO FINANCEIRO (SIMPLES) ===")
    
    total_desp = sum(d["valor"] for d in financeiro["despesas"])

    prods = producao_carregar()
    total_prod = sum(p.get("qtd", 0) for p in prods)

    funcs = rh_carregar()
    folha = sum(f.get("salario_bruto", 0) for f in funcs)

    est = estoque_carregar()
    mat = est.get("insumos", {}).get("material", 0)
    
    print("-" * 30)
    print(f"Total Despesas Registradas: R${total_desp:.2f}")
    print(f"Total Folha (Bruta/RH): R${folha:.2f}")
    print(f"Produção Registrada (Peças): {total_prod}")
    print(f"Insumo 'Material' Restante: {mat}")
    print("-" * 30)

    if financeiro["despesas"]:
        print("Despesas detalhadas:")
        for d in financeiro["despesas"]:
            print(f" - {d['tipo']}: R${d['valor']:.2f}")

def menu():
    while True:
        print("=== MENU FINANCEIRO ===")
        print("1 - Cadastrar despesa")
        print("2 - Mostrar total despesas")
        print("3 - Gerar relatório")
        print("4 - Excluir ou adicionar despesa")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar_despesa()
        elif op == "2":
            calcular_total_despesas()
        elif op == "3":
            gerar_relatorio()
        elif op == "4":
            excluir_despesa()
        elif op == "0":
            return
        else:
            print("Opção inválida.")
