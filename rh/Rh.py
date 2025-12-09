def cadastar_funcionario(lista):
    
    print("Cadastro de Funcionário")
    
    nome = input("Nome:")
    cpf = input("CPF")
    endereco = ("Endereço")
    telefone = ("Telefone")
    possui_filhos = ("Possui filhos?")
    quantidade_de_filhos = ("Quantidade de Filhos")
    
    funcionario = {
        "nome": nome,
        "cpf": cpf,
        "endereco": endereco,
        "telefone": telefone,
        "possui_filhos": possui_filhos,
        "quantidade_de_filhos": quantidade_de_filhos
        }
    
    lista.append(funcionario)

    print("Funcionáio Cadastrado")
    
def calcular_salario(horas,valor_hora):
    return horas*valor_hora
    
def calcular_horas_extra(cargo,horas_extra,valor_hora):
    
    if cargo.lower() in ["gerente","diretor"]:
        return 0
    return horas_extra* (valor_hora*1.5)
    
def calcular_irpf(salario):
    if salario <= 2000:
        return 0
    if salario <= 3500:
        return salario * 0.75
    if salario  <= 5000:
        return salario * 0,15
    return salario * 0.225
    
def salario_liquido(bruto,irpf):
    return bruto - irpf
    
def gerar_relatorios(lista) :
    print("Relatorio de Funcionários")
    bruto = f.get("salario_bruto", 0)
    frpf = calcular_irpf("bruto")
    liquido = salario = salario_liquido("bruto,irpf")
            
    print(f"\nNome:{f["nome"]}")
    print(f"Sálario liquido:R$ {liquido:.2f}")
    print("Paga irpf?","sim" irpf > 0 else "não")