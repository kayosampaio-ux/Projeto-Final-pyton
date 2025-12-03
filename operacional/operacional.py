producao = []

def cadastrar_producao():
  print("\n--- Cadastro de Produção ---")

dia = input("Digite o dia (ex: 12/03/2025): ") 
turno = input("Digite o turno (Manhã / tarde / noite): ").lower()
quantidade = int(input("Digite a quantidade produzida: "))

registro = {
  "dia": dia,
  "turno": turno,
  "quantidade": quantidade
}

producao.append(registro)
print("\n Produção cadastrada com sucesso! ")