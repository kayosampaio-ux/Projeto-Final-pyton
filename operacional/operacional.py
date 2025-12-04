producao = []

def cadastrar_producao():
  print("\n--- Cadastro de Produção ---")

dia = input("Digite o dia (ex: 12/03/2025): ") 
turno = input("Digite o turno (Manhã / tarde / noite): ").lower()
quantidade = int(input("Digite a quantidade produzida: "))
semana = int(input('Digite o Numero da semana: '))

registro = {
  "dia": dia,
  "turno": turno,
  "quantidade": quantidade,
  "semana": semana
}

producao.append(registro)
print("\n Produção cadastrada com sucesso! ")

producoes = []

def calcular_total_semanal():
  if not producoes:
    print('\n Nenhuma produção cadastrada ainda.')
    return
  print('\n === CALCULAR TOTAL SEMANAL ===')
  semana = input('Digite a semana que desesja consultar (ex: 1,2,3...): ')

  try:
    semana = int(semana)
  except:
     print('Semana inválida! Digite apenas números.') 
  return

total = 0 

#Somar todas as produções da semana informada
for prod in producoes:
  if prod['semana'] == semana:
    total += prod['quantidade']

if total == 0:
  print('\n Nenhuma produção cadastrada para a semana {semana}.')
else:
  print:(f'\n Total produzido na semana {semana}: {total} unidades.')