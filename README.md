# Análise de Dados para Negócios com Python e Google Colab

Bem-vindo ao material de apoio oficial do nosso curso em formato WebBook interativo!

Este curso foi desenhado especificamente para **estudantes de graduação e profissionais em negócios** (iniciantes sem experiência prévia com programação) que desejam aprender a utilizar o poder dos dados para a tomada de decisão.

## Objetivo Principal
No final desta jornada, você será capaz de usar o ambiente do **Google Colab** na nuvem para:
- Carregar rapidamente arquivos CSV e Excel externos com `pandas`.
- Inspecionar e limpar bases de dados, lidando com informações nulas e incompletas.
- Realizar análises estatísticas descritivas sólidas e testes de hipóteses validados com `pingouin`.
- Criar visualizações de dados profissionais e altamente personalizadas com `seaborn`.

## O que você será capaz de criar?
Você vai evoluir de planilhas complexas para código limpo e automatizado. Veja um exemplo real do que você vai construir e analisar:

```python
import pandas as pd
import pingouin as pg
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregando e limpando os dados de faturamento
df = pd.read_csv('faturamento_2024.csv')
df = df.dropna()

# 2. Resumo da média de vendas por região
vendas_resumo = df.groupby('Regiao')['Valor_Venda'].mean()
print(vendas_resumo)

# 3. Teste de Hipótese para verificar uma diferença de performance
pg.ttest(df[df['Regiao'] == 'Sul']['Valor_Venda'],
         df[df['Regiao'] == 'Norte']['Valor_Venda'])

# 4. Gráfico executivo focado para uma apresentação à diretoria
sns.set_theme(style='whitegrid')
sns.barplot(data=df, x='Regiao', y='Valor_Venda', errorbar=None)
plt.title("Performance de Vendas por Região (2024)", fontsize=14)
plt.show()
```

## Explorando os Módulos
Utilize o menu lateral esquerdo para navegar pelos capítulos:
1. **Módulo 1:** Fundamentos do Google Colab e Python
2. **Módulo 2:** Manipulação de Dados e Estatística Descritiva
3. **Módulo 3:** Visualização de Dados com Seaborn
4. **Módulo 4:** Testes de Hipóteses com Pingouin

Vamos começar? Clique em "Módulo 1" no menu!