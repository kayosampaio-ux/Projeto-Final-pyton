#Feito por Kayo Dev1
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

def excluir_producao(producoes):
  print("\n === EXCLUIR UMA PRODUÃO")
  if not producoes:
    print('Não há produções cadastradas.')
    return producoes
  
  dia = input("Digite o dia da produção pra excluir: (ex: 25/05/2023): ")
  turno = input("Digite o turno (manhã / tarde / noite): ")

  # procurar produção correspondente
  for p in producoes:
    if p['dia'] == dia and p['turno'].lower() == turno.lower():
      print("\nProdução encontrada:")
      print(f"Dia: {p['Dia']}")
      print(f"Turno: {p['turno']}")
      print(f"quantidade: {p['quantidade']}")

      confirmar = input("Excluir esta produção? (s/n): ").lower()
      if confirmar == 's':
        producoes.remove(p)
        print("Produção excluída com sucesso.")
      else:
        print("Exclusão cancelada.")
        return producoes
      print("Nenhuma produção encontrada com essas informações.")
      return producoes
    
#Feito por Kayo Dev1
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
  print(f"\n Nenhuma produção cadastrada para a semana {semana}.")
else:
  print:(f'\n Total produzido na semana {semana}: {total} unidades.')

#Feito por Kayo Dev1

def calcular_media_por_dia():
  if not producao:
    print("\nNenhuma produção cadastrada ainda.")
    return
  
  print("\n === CALCULAR MÈDIA POR DIA ===")
  dia = input("Digite o dia em que deseja consultar (ex: 12/03/2025): ")
  total = 0
  contagem = 0
  
  for prod in producao:
    if prod['dia'] == dia:
     total += prod['quantidade']
    contagem += 1

  if contagem == 0:
    print(f"\nNenhuma produção cadastrada para o dia {dia}.")
    return
  
  media = total / contagem
  print(f"\nA média de produção no dia {dia} foi de `{media:.2f} unidades.")
  return


#Feito por Kayo Dev1

def calcular_media_por_turno():
  if not producao:
    print('\nNenhuma produção cadastrada ainda.')
    return
  
  print('\n ---CALCULAR MÉDIA POR TURNO ---')
  turno = input('Digiteo turno (manhã / tarde / noite): ').lower

  #Fltrar produções do turno escolhido
  producoes_turno = [prod['quantidade'] for prod in producao if prod ['turno'].lower() == turno]

  if not producoes_turno:
    print(f"Nenhuma produção encontrada para o turno '{turno}'.")
    return
  
  media = sum(producoes_turno) / len(producoes_turno)

  print(f"\nA média de produção no turno '{turno}' é: {media:.2f}")

def simular_mensal_anual():
  if not producao:
    print('\n Nenhuma produção cadastrada ainda.')
    return
  
  print('\n ---SIMULAÇÂO MENSAL E ANUAL ---')

  #pega somente as quantidades registradas
  quantidades = [prod['quantidade'] for prod in producao]

  #Calcular média geral
  media_geral = sum(quantidades) / len(quantidades)

  #simulações
  simulacão_mensal = media_geral * 30 #aqui eu to supondo que seja 30 dias

  simulação_anual = media_geral *365 #supondo 365 dias

  print(f"\nMédia diária geral:{media_geral:.2f}")
  print(f"\nProdução estimada menstal (30 dias): {simulacão_mensal:.2f}")
  print(f"\nProdução estimada anual (365 dias): {simulação_anual:.2f}")

def calcular_producao_ideal(producao):
  if not producao:
    print("Nenhuma produção cadastrada para calcular a produção ideal!")
    return
  
total = 0
dias_contados = 0

for dia in producao:
 for turno in producao[dia]:
   total += producao[dia][turno]
   dias_contados += 1

media_diaria = total / dias_contados
producao_ideal = media_diaria * 7

print("\n===== PRODUÇÃO IDEAL=====")
print(f"Média diária real: {media_diaria:.2f} unidades")
print(f"Produção ideal estimada (1 semana): {producao_ideal:.2f} unidades")

def gerar_relatorio(producao):
  if not producao:
    print("Nenhuma produção cadastrada! O relatório não pode ser gerado.")
    return
  print("\n================RELATÓRIO DE PRODUÇÃO =================")

  total_geral = 0
  dias_contados = 0
  turno_soma = {"manha": 0, "tarde": 0, "noite": 0}
  turnos_contagem = {"manha": 0, "tarde": 0, "noite": 0}

  for dia in producao:
    print("f\n DIA: {dia}")
    dias_contados += 1

  for turno in producao[dia]:
    quantidade = producao[dia] [turno]
    print(f"{turno.captalize()}: {quantidade} Unidades.")

    total_geral += quantidade
    turno_soma[turno] += quantidade
    turnos_contagem[turno] += 1

    media_diaria = total_geral / dias_contados

    media_turno = {}
    for turno in turno_soma:
      if turnos_contagem[turno] > 0:
        media_turno[turno] = turno_soma[turno] / turnos_contagem[turno]
      else:
        media_turno[turno] = 0

        print("\n ==================RESUMO FINAL=================")
        print(f"Total produzido: {total_geral} unidades")
        print(f"Média por dia:{media_diaria:.2f} unidades")
        
        print("\nMédia por turno:")
        for turno in media_turno:
          print(f" - {turno.capitalize()}: {media_turno[turno]:.2f} unidades")

          print("\n===============================================================")
