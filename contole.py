import pandas as pd
import os

controle = pd.DataFrame({
    'entrada': ['salario', 'vale combustivel', 'vale alimentacao'],
    'valor': [2000, 300, 500]
})

controle2 = pd.DataFrame({
    'saida': ['fumo', 'total mensal'],
    'valor': [400, 1320]


print(controle)
print(controle2)

# SALVA TUDO EM UM SÓ ARQUIVO - CORREÇÃO AQUI
with pd.ExcelWriter('controle_completo.xlsx') as writer:
    controle.to_excel(writer, sheet_name='Entradas', index=False)
    controle2.to_excel(writer, sheet_name='Saidas', index=False)

print("Arquivo Excel salvo com sucesso!")

# Abre o Excel automaticamente
os.startfile('controle_completo.xlsx')