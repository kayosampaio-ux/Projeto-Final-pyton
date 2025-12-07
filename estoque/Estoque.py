# I Verifica se o produto já está cadastrado

def produto_existe(lista, codigo, nome):
    for p in lista:
        if p["codigo"] == codigo or p["nome"].lower() == nome.lower():
            return True
    return False

# II - Cadastrar produto

def cadastrar_produto(lista):
    print("== CADASTRAR PRODUTO ==\n")
    
    codigo = input("Código: ")
    nome = input("Nome: ")

    if produto_existe(lista, codigo, nome):
        print("Produto já cadastrado!\n")
        return

    data_fab = input("Data de fabricação: ")
    fornecedor = input("Fornecedor: ")
    quantidade = int(input("Quantidade: "))
    valor_compra = float(input("Valor de compra por unidade (R$): "))

    produto = {
        "codigo": codigo,
        "nome": nome,
        "data_fab": data_fab,
        "fornecedor": fornecedor,
        "quantidade": quantidade,
        "valor_compra": valor_compra
    }

    lista.append(produto)
    print("Produto cadastrado com sucesso!\n")

# III - Pesquisar produto

def pesquisar(lista):
    print("== PESQUISAR PRODUTO ==\n")
    tipo = input("Pesquisar por (1) Nome ou (2) Código: ")

    if tipo == "1":
        termo = input("Digite o nome: ").lower()
        for p in lista:
            if p["nome"].lower() == termo:
                print("\n🔎 Produto encontrado:")
                print(p)
                return
    elif tipo == "2":
        termo = input("Digite o código: ")
        for p in lista:
            if p["codigo"] == termo:
                print("Produto encontrado:\n")
                print(p)
                return

    print("Produto não encontrado.\n")

# IV - Calcular custos

def calcular_custos(lista):
    print("== CALCULAR CUSTOS ==\n")
    codigo = input("Digite o código do produto: ")

    for p in lista:
        if p["codigo"] == codigo:
            custo_semanal = p["quantidade"] * p["valor_compra"]
            custo_mensal = custo_semanal * 4
            custo_anual = custo_mensal * 12

            custos = {
                "custo_semanal": custo_semanal,
                "custo_mensal": custo_mensal,
                "custo_anual": custo_anual
            }

            print("CUSTOS CALCULADOS:\n")
            print(custos)
            return custos

    print("Produto não encontrado.\n")
    return None

# V - Mostrar todos os produtos cadastrados

def mostrar_todos(lista):
    print("== LISTA DE PRODUTOS (máx. 10) ==\n")

    if not lista:
        print("Nenhum produto cadastrado.")
        return

    for i, p in enumerate(lista[:10], start=1):
        print(f"""
Produto {i}

Código: {p['codigo']}
Nome: {p['nome']}
Data fabricação: {p['data_fab']}
Fornecedor: {p['fornecedor']}
Quantidade: {p['quantidade']}
Valor compra: R$ {p['valor_compra']:.2f}
""")

# VI Alterar produto

def alterar_produto(lista):
    print("== ALTERAR PRODUTO ==\n")
    codigo = input("Digite o código do produto a ser alterado: ")

    for p in lista:
        if p["codigo"] == codigo:
            print("Produto encontrado:\n")
            print(p)

            nome = input("Novo nome : ")
            if nome:
                p["nome"] = nome

            data_fab = input("Nova data de fabricação : ")
            if data_fab:
                p["data_fab"] = data_fab

            fornecedor = input("Novo fornecedor : ")
            if fornecedor:
                p["fornecedor"] = fornecedor

            quantidade = input("Nova quantidade : ")
            if quantidade:
                p["quantidade"] = int(quantidade)

            valor_compra = input("Novo valor de compra : ")
            if valor_compra:
                p["valor_compra"] = float(valor_compra)

            print("Produto alterado com sucesso!\n")
            return

    print("Produto não Localizado.\n")

# VII Excluir produto cadastrado

def excluir_produto(lista):
    print("== EXCLUIR PRODUTO ==\n")
    codigo = input("Digite o código do produto para excluir: ")

    for p in lista:
        if p["codigo"] == codigo:
            lista.remove(p)
            print("Produto excluído com sucesso!\n")
            return

    print("Produto não encontrado.\n")

# VII Menu de opções

def exibir_menu():
    print("""
    === MENU ===
    1 - Cadastrar Produto
    2 - Pesquisar Produto
    3 - Calcular Custos
    4 - Mostrar Todos
    5 - Alterar Produto
    6 - Excluir Produto
    0 - Sair
    """)

def main():
    produtos = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            pesquisar(produtos)
        elif opcao == "3":
            calcular_custos(produtos)
        elif opcao == "4":
            mostrar_todos(produtos)
        elif opcao == "5":
            alterar_produto(produtos)
        elif opcao == "6":
            excluir_produto(produtos)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()