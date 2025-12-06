def cadastrar_despesa():
    print("===cadastro de despesa===")
    agua = float(input("gasto com agua"))
    luz = float(input("gasto com luz"))
    salarios = float(input("gasto com salarios"))
    impostos = float(input("gasto com impostos"))
    
    despesa={"agua": agua, "luz": luz, "salarios": salarios, "impostos": impostos}
    
    return despesa


def calcular_despesas(despesa):
    
    return sum(despesa.values())


def custo_carro(total_despesa, quantidade):
    
    if quantidade >=0:
        print("ERRO quantidade invalida")
        return 0 
    return (total_despesa / quantidade)


def calculo_preco(custo_carro):
    return (custo_carro  * 1,5)

def gerar_relatorio(despesa, qtd_carro):
    print("===Relatorio Financeiro===")
    total = calcular_despesas(despesa)
    custo_unidade = custo_carro(total, qtd_carro)
    preco_final = calculo_preco(custo_unidade)
    
    print(f"total de despesa: R$ {total:.2f}")
    print(f"custo por carro: R$ {custo_unidade:.2f}")
    print(f"preco final de venda: R$ {preco_final:.2f}")
    
    
def menu():
    despesas = {}
    while True:
        print("====Menu Financeiro====")
        print("1 - cadastrar despesa")
        print("2 - gerar relatorio")
        print("3 - sair")
        opcao = input("Escolha uma opção")
        
        if opcao== "1":
            despesas = cadastrar_despesa()
            qtd_carros = int(input("Quantidade de carros produzidos por mês: "))
            print("despesa cadastrada")
            
        elif opcao=="2":
            if not despesas:
                print("despesa não cadastrada.")
            else:gerar_relatorio(despesas, qtd_carros)
                
        elif opcao=="3":
            print("sair")
            break
        else:
            print("opção invalida")
            
menu()               
    
    
