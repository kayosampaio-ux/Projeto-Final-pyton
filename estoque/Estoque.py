# estoque/estoque.py - módulo simples de estoque (database/estoque.json)
import os, json

ARQUIVO = "database/estoque.json"

# Garante que o arquivo e pasta existam
def garantir_arquivo():
    os.makedirs("database", exist_ok=True)
    if not os.path.exists(ARQUIVO):
        inicial = {"insumos": {"material": 1000}, "produtos": []}
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(inicial, f, indent=2, ensure_ascii=False)

# Carrega o dicionário de estoque
def carregar():
    garantir_arquivo()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

# Salva o dicionário atualizado
def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def cadastrar_produto():
    estoque = carregar()
    print("\n=== Cadastrar Produto ===")
    codigo = input("Código: ").strip()
    nome = input("Nome: ").strip()
    
    try:
        qtd = int(input("Quantidade: ").strip())
        valor = float(input("Valor de compra por unidade: ").strip() or 0)
    except ValueError:
        print("Valores inválidos. Registrando com Qtd=0 e Valor=0.")
        qtd = 0
        valor = 0
        
    estoque["produtos"].append({
        "codigo": codigo,
        "nome": nome,
        "quantidade": qtd,
        "valor_compra": valor
    })
    salvar(estoque)
    print("✔ Produto cadastrado.")

def mostrar_produtos():
    estoque = carregar()
    if not estoque["produtos"]:
        print("Nenhum produto cadastrado.")
        return
    print("\n=== Produtos Cadastrados ===")
    for p in estoque["produtos"]:
        print(f"Cód:{p['codigo']} - {p['nome']} - Qtd:{p['quantidade']} - R${p['valor_compra']:.2f}")

def pesquisar_produto():
    estoque = carregar()
    chave = input("Pesquisar por código: ").strip()
    for p in estoque["produtos"]:
        if p["codigo"] == chave:
            print(p)
            return p
    print("Produto não encontrado.")
    return None

def consumir_insumos(qtd_pecas):
    """
    Usado pelo operacional: consome 1 unidade de 'material' por peça.
    Retorna True se FALTAR insumo (ou seja, NÃO foi possível consumir).
    """
    estoque = carregar()
    disponivel = estoque["insumos"].get("material", 0)
    if disponivel >= qtd_pecas:
        estoque["insumos"]["material"] = disponivel - qtd_pecas
        salvar(estoque)
        return False  # não faltou
    else:
        return True  # FALTou

def entrada_insumo():
    estoque = carregar()
    try:
        qtd = int(input("Quantidade a entrar no insumo 'material': ").strip())
        if qtd < 0: raise ValueError
    except ValueError:
        print("Quantidade inválida.")
        return
        
    estoque["insumos"]["material"] = estoque["insumos"].get("material",0) + qtd
    salvar(estoque)
    print("✔ Entrada de insumo registrada.")

def menu():
    while True:
        print("\n--- MENU ESTOQUE ---")
        print("1 - Cadastrar produto")
        print("2 - Mostrar produtos")
        print("3 - Pesquisar produto")
        print("4 - Entrada de insumo")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar_produto()
        elif op == "2":
            mostrar_produtos()
        elif op == "3":
            pesquisar_produto()
        elif op == "4":
            entrada_insumo()
        elif op == "0":
            return
        else:
            print("Opção inválida.")