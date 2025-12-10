import os, json
from rh import contar_por_turno
from estoque import consumir_insumos
# Importa APENAS a função de registro do financeiro que é usada
from financeiro import registrar_custo_producao

ARQUIVO = "database/producao.json"

# Parâmetros de negócio
PEÇAS_POR_HORA_POR_FUNC = 8
HORAS_POR_TURNO = 8
TURNOS_POR_DIA = 3

# Garante que o arquivo e pasta existam
def garantir_arquivo():
    os.makedirs("database", exist_ok=True)
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f)

# Carrega a lista de produções
def carregar():
    garantir_arquivo()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

# Salva lista atualizada
def salvar(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

def capacidade_por_turno():
    cont = contar_por_turno()  
    cap = {}
    for t in ("manha","tarde","noite"):
        
        cap[t] = cont.get(t,0) * HORAS_POR_TURNO * PEÇAS_POR_HORA_POR_FUNC
    return cap

def cadastrar():
    producoes = carregar()
    cap = capacidade_por_turno()
    print("\n=== Cadastrar Produção ===")
    
    turno = input("Turno (manha/tarde/noite): ").strip().lower()
    if turno not in ("manha","tarde","noite"):
        print("Turno inválido. Cadastro cancelado.")
        return
        
    capacidade_max = cap.get(turno, 0)
    print(f"Capacidade estimada para este turno: {capacidade_max} peças")
    
    try:
        qtd = int(input("Quantidade produzida: ").strip())
        if qtd < 0: raise ValueError
    except ValueError:
        print("Quantidade inválida. Cadastro cancelado.")
        return

    
    if qtd > capacidade_max:
        print("ATENÇÃO: Quantidade maior que a capacidade estimada. Confirmar? (s/n)")
        if input().strip().lower() != "s":
            print("Cadastro cancelado.")
            return
            
    
    faltou = consumir_insumos(qtd)
    if faltou:
        print("Estoque insuficiente. Não foi possível registrar a produção.")
        return
        
    registro = {"turno": turno, "qtd": qtd, "dia": input("Data (ex 12/03/2025): ").strip()}
    producoes.append(registro)
    salvar(producoes)
    
    
    try:
        registrar_custo_producao(qtd)
    except Exception as e:
        print(f"Aviso: Não foi possível registrar no Financeiro: {e}")
        
    print("✔ Produção registrada e estoque atualizado.")

def listar():
    producoes = carregar()
    if not producoes:
        print("Nenhuma produção registrada.")
        return
    print("\n=== Produções Registradas ===")
    for r in producoes:
        print(f"{r['dia']} - {r['turno']} - {r['qtd']} peças")

def total_registrado():
    producoes = carregar()
    total = sum(p['qtd'] for p in producoes)
    print(f"Total de peças registradas: {total}")
    return total

def menu():
    while True:
        print("\n--- MENU OPERACIONAL ---")
        print("1 - Cadastrar produção")
        print("2 - Listar produções")
        print("3 - Capacidade por turno")
        print("4 - Total registrado")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            print(capacidade_por_turno())
        elif op == "4":
            total_registrado()
        elif op == "0":
            return
        else:
            print("Opção inválida.")