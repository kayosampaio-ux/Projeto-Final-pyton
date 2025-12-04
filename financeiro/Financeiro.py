def cadastrar_despesa():
    print("===cadastro de despesa===")
    agua = float(input("gasto com agua"))
    luz = float(input("gasto com luz"))
    salarios = float(input("gasto com salarios"))
    impostos = float(input("gasto com impostos"))
    
    despesa={"agua": agua, "luz": luz, "salarios": salarios, "impostos": impostos}
    
    return despesa