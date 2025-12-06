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


