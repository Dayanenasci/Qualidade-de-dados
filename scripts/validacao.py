import pandas as pd
import re

df = pd.read_csv("data/clientes.csv")

erros = []

# Verificar valores nulos
if df["email"].isnull().any():
    erros.append("Existem emails nulos.")

if df["idade"].isnull().any():
    erros.append("Existem idades nulas.")

# Validar formato de email
email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
emails_invalidos = df[~df["email"].fillna("").str.match(email_regex)]

if not emails_invalidos.empty:
    erros.append("Existem emails com formato inválido.")

# Verificar duplicidade
if df.duplicated().any():
    erros.append("Existem registros duplicados.")

# Gerar relatório
with open("relatorios/relatorio_qualidade.txt", "w") as f:
    if erros:
        for erro in erros:
            f.write(erro + "\n")
    else:
        f.write("Nenhum erro encontrado.")

print("Validação concluída!")