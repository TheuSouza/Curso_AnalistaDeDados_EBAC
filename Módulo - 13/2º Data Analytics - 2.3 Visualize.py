import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

brasil_df = pd.read_csv('brasil.csv', delimiter=';')

menos_populosas_df = brasil_df[[
    'cidade', 
    'populacao',
    'estado',
    'regiao'
    ]].sort_values('populacao')[:10]

populacao_regiao = brasil_df.groupby('regiao').agg({'populacao': 'sum'})

populacao_regiao.plot.pie(y='populacao', figsize=(300, 300))


# Seaborn:
plt.figure(figsize=(12, 6))
sns.barplot(
    data=menos_populosas_df,
    x='cidade', 
    y='populacao',
    hue='populacao', 
    palette='rocket_r',
    legend=False,
)
plt.title('10 cidades menos populosas do Brasil', fontdict={'fontsize': 20})
plt.xlabel('Cidades', fontsize= 16)
plt.ylabel('População', fontsize= 16)
plt.xticks(rotation= 45)
plt.grid(axis='y', linestyle='--', alpha= 0.4)
plt.tight_layout()
plt.show()


# Plotly:
fig01 = px.bar(
    data_frame=menos_populosas_df,
    x='cidade',
    y='populacao',
    color='populacao',
    labels={'populacao': 'População'},
    title='10 cidades menos populosas do Brasil',
    hover_data=['estado', 'regiao']
)
fig01.update_layout(
    width=1200,
    height=600,
    margin=dict(
        l=5,
        r=5,
        b=5,
        t=50,
))
fig01.show()
