# rh/rh.py - módulo simples de RH 
#Dev Ezequiel
import os, json

ARQUIVO = "database/funcionarios.json"

# Garante que o arquivo e pasta existam
def garantir_arquivo():
    os.makedirs("database", exist_ok=True)
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f)

# Carrega a lista de funcionários
def carregar():
    garantir_arquivo()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

# Salva lista atualizada
def salvar(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

def cadastrar():
    funcionarios = carregar()
    print("\n=== Cadastrar Funcionário ===")
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    
    turno = input("Turno (manha/tarde/noite): ").strip().lower()
    if turno not in ("manha","tarde","noite"):
        print("Turno inválido, cadastrando como 'manha'.")
        turno = "manha"
    
    try:
        salario = float(input("Salário bruto mensal (R$): ").strip() or 0)
    except ValueError:
        print("Valor inválido. Registrando salário como 0.")
        salario = 0

    funcionarios.append({
        "id": len(funcionarios)+1,
        "nome": nome,
        "cpf": cpf,
        "turno": turno,
        "salario_bruto": salario
    })
    salvar(funcionarios)
    print("✔ Funcionário cadastrado.")

def listar():
    funcionarios = carregar()
    if not funcionarios:
        print("Nenhum funcionário registrado.")
        return
    print("\n=== Funcionários Cadastrados ===")
    for f in funcionarios:
        print(f"ID:{f['id']} - {f['nome']} - Turno:{f['turno']} - Salário:R${f['salario_bruto']:.2f}")

def contar_por_turno():
    funcionarios = carregar()
    cont = {"manha":0,"tarde":0,"noite":0}
    for f in funcionarios:
        t = f.get("turno","manha")
        if t in cont:
            cont[t] += 1
    return cont

def folha():
    funcionarios = carregar()
    if not funcionarios:
        print("Nenhum funcionário para calcular folha.")
        return 0
    total = 0
    print("\n=== Folha Salarial (Simples) ===")
    for f in funcionarios:
        bruto = f.get("salario_bruto",0)
        print(f"{f['nome']}: bruto R${bruto:.2f}")
        total += bruto
    print(f"\nTotal folha (bruta): R${total:.2f}")
    return total

def menu():
    while True:
        print("\n--- MENU RH ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Contagem por turno")
        print("4 - Folha")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            print(contar_por_turno())
        elif op == "4":
            folha()
        elif op == "0":
            return
        else:
            print("Opção inválida.")