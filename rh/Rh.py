import json

arquivo = "funcionarios.json"

def carregar():
    try: with open(arquivo,'r',encoding= "utf-8") as f:
        return json.load(f)
    except:
        return[]
    
def salvar(lista):  
    with open(arquivo,"w",enconding = "utf-8") as f:
        json.dump(lista,f,indent = 2)

def cadastrar():
    lista = carregar()
        print("\n=== CADASTRAR FUNCIONÁRIO===")
        nome = input("nome")
        cpf = input("CPF:")
        turno = input("Turno(Manhã/Tarde/Noite):")
        salario = float(input("Salário"))
        
        novo = {
            "id":len(lista)
            "nome":nome,
            "cpf":cpf,
            "turno":turno,
            "salario":salario
        }
        
lista.append(novo)
salvar(lista)
print("Funcionário cadastrado!\n")

def listar():
    lista = carregar()
    print("\n=== LiSTA DE FUNCIONÁRIOS===")
    if len(lista ==0:)
    print("Nenhum funcionário cadastrado.")
    else:
        print(f"id:{f["id"]} | {f["nome"]}) | CPF:{f["cpf"]} | Turno: {f["turno"]} | {f["salario"]}")
    print()
    
def buscar ():
    lista = carregar()
    nome = input("\n Digite o nome para Buscar: ").lower()
    achou = false
    
    for f in lista:
        if nome in f["nome"].lower():
            print(f "ID:{f["id"]} - {f["nome"]} - {f["turno"]} - {f["salario"]}")
            achou = True 
        if not achou:
            print ("Nenhum Funcionário encontrado.\n")
            
    print()
    
    def editar ():
        lista = carregar()
        listar()
        
        try:
            id_escolhido = int(input("ID para editar: "))
        except:
            print("ID inválido.\n")
            return
        
        for f in lista:
            if f["id"] == id_escolhido:
                print("Deixe Vazio para manter o valor atual.\n")
            nome = input("Nome novo: ")
            cpf = input("CPF novo : ")
            turno = input("Turno novo: ")
            salario = input("Salário novo: ")   
        
        if nome ! = "":
            f["nome"] = nome
        if cpf ! = "":
            f["cpf"] = cpf
        if turno ! = "":
            f["turno"] = turno
        if salario ! = "":
            f["salario"] = float(salario)
            
            salvar(lista)
            print("Editado com sucesso\n")
            return
        print ("ID não encontrado.\n")
        
        def remover():
            lista = carregar()
            lista()
            
            try: 
                id_escolhido = int(input("ID para remover:))
            except:
            print("ID inválido.\n")
            return
            
        nova_lista = []
        removido = false
        for f in lista:
        if f["id"] == id_escolhido:
         removido = true
        else nova_lista.append(f)
         
        nova_lista.append(f)
        if removido:
        salvar(nova_lista)
        print("Funcionário removido!\n")
        else: 
        print("ID não encontrado.")
        
        def contar_por_turno():
        lista = carregar ()
        cont = {"manha":0,"tarde":0,"noite":0}
        
        for f in lista: turno = f ["turno"]
        if turno in cont:
        cont[turno] + = 1
        
        print("\n===CONTAGEM POR TURNO===")
        print(cont)
        print()
        
        def folha():
        lista = carregar ()
        print("\n===FOLHA SALARIAL===")
        total = 0
        
    for f in lista:
    print(f"{f["nome"]} - R${f["salario"]}")
    total + = f["salario"]
    
    print("\nTotal da Folha: R$",total,"\n")