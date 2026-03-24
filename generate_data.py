import pandas as pd
import numpy as np

# A "semente" garante que os dados aleatórios sejam os mesmos toda vez que o código rodar.
# Isso é perfeito para aulas, pois todos os alunos terão os mesmos gráficos e valores-p!
np.random.seed(42)

print("Iniciando a geração das bases de dados sintéticas...")

# ---------------------------------------------------------
# 1. vendas.csv (Para Módulo 3 - Gráfico de Barras com 'hue')
# ---------------------------------------------------------
anos = [2022, 2023] * 100
regioes = np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], size=200)
# Faturamento entre 100k e 500k, com um leve aumento em 2023
faturamento = np.random.uniform(100000, 400000, size=200) + (np.array(anos) == 2023) * 50000 

df_vendas = pd.DataFrame({
    'Ano': anos,
    'Regiao': regioes,
    'Faturamento': np.round(faturamento, 2)
})
df_vendas.to_csv('vendas.csv', index=False)
print("✅ vendas.csv gerado!")


# ---------------------------------------------------------
# 2. rh_salarios.csv (Para Módulo 3 - Histograma)
# ---------------------------------------------------------
# Distribuição normal (Média 5000, Desvio Padrão 1500)
salarios = np.random.normal(loc=5000, scale=1500, size=300)
# Garantindo que não tenha salário menor que um salário mínimo hipotético
salarios = np.clip(salarios, 1400, None) 

df_rh = pd.DataFrame({'Salario': np.round(salarios, 2)})
df_rh.to_csv('rh_salarios.csv', index=False)
print("✅ rh_salarios.csv gerado!")


# ---------------------------------------------------------
# 3. marketing.csv (Para Módulo 3 - Gráfico de Dispersão)
# ---------------------------------------------------------
investimento = np.random.uniform(5000, 50000, size=150)
# Vendas dependem do investimento (correlação positiva) + um ruído aleatório
vendas_mkt = (investimento * 3.5) + np.random.normal(0, 20000, size=150)
vendas_mkt = np.clip(vendas_mkt, 1000, None) # Evita vendas negativas

df_marketing = pd.DataFrame({
    'Investimento': np.round(investimento, 2),
    'Vendas': np.round(vendas_mkt, 2)
})
df_marketing.to_csv('marketing.csv', index=False)
print("✅ marketing.csv gerado!")


# ---------------------------------------------------------
# 4. teste_ab_vendas.csv (Para Módulo 4 - Teste T)
# ---------------------------------------------------------
# Vamos forçar o Anúncio B a ser um pouco melhor para que o Valor-P dê < 0.05 na aula!
vendas_A = np.random.normal(loc=120, scale=25, size=250)
vendas_B = np.random.normal(loc=130, scale=25, size=250) # Média levemente maior

df_ab = pd.DataFrame({
    'Anuncio': ['A']*250 + ['B']*250,
    'Vendas': np.concatenate([vendas_A, vendas_B])
})
df_ab['Vendas'] = np.round(df_ab['Vendas'], 2)
# Embaralhando as linhas para parecer uma base real
df_ab = df_ab.sample(frac=1).reset_index(drop=True) 
df_ab.to_csv('teste_ab_vendas.csv', index=False)
print("✅ teste_ab_vendas.csv gerado!")


# ---------------------------------------------------------
# 5. embalagens.csv (Para Módulo 4 - ANOVA)
# ---------------------------------------------------------
# A embalagem Verde terá um desempenho claramente superior às outras
vendas_vermelha = np.random.normal(loc=50, scale=10, size=100)
vendas_azul = np.random.normal(loc=52, scale=10, size=100)
vendas_verde = np.random.normal(loc=65, scale=10, size=100) # Campeã de vendas

df_embalagens = pd.DataFrame({
    'Design_Embalagem': ['Vermelho']*100 + ['Azul']*100 + ['Verde']*100,
    'Vendas': np.concatenate([vendas_vermelha, vendas_azul, vendas_verde])
})
df_embalagens['Vendas'] = np.round(df_embalagens['Vendas'], 0)
df_embalagens = df_embalagens.sample(frac=1).reset_index(drop=True)
df_embalagens.to_csv('embalagens.csv', index=False)
print("✅ embalagens.csv gerado!")


# ---------------------------------------------------------
# 6. descontos.csv (Para Módulo 4 - Correlação Pingouin)
# ---------------------------------------------------------
# Descontos de 5% a 50%
descontos = np.random.uniform(5, 50, size=200)
# Unidades vendidas sobem conforme o desconto sobe (Correlação forte)
unidades = (descontos * 8) + np.random.normal(0, 30, size=200)
unidades = np.clip(unidades, 10, None) # Mínimo de 10 unidades

df_descontos = pd.DataFrame({
    'Desconto_Oferecido': np.round(descontos, 1),
    'Unidades_Vendidas': np.round(unidades, 0).astype(int)
})
df_descontos.to_csv('descontos.csv', index=False)
print("✅ descontos.csv gerado!")

print("\n🎉 Todas as 6 bases de dados foram criadas com sucesso na pasta atual!")