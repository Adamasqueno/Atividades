import pandas as pd

arquivo = pd.read_excel(r'C:\Users\Guilherme\Desktop\python\Analise_de_dados\Analise de Dados.xlsx')

depositos_por_maquina = arquivo['ID MÁQUINA'].value_counts()
pontos_totais = arquivo['PONTOS'].sum()

print("\nDepósitos por máquina:")
print(depositos_por_maquina)

print(f"\nPontos totais distribuídos: {pontos_totais}")