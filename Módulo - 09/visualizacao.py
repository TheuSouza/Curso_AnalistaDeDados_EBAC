from sys import argv

import pandas as pd
import seaborn as sns

df = pd.read_csv('./Módulo - 09/taxa-cdi.csv')

grafico = sns.lineplot(data=df, x='Hora', y='Taxa', color='pink')
grafico.grid(axis='y', linestyle='--', alpha=0.5)
grafico.tick_params(axis='x', labelrotation=45)
grafico.get_figure().savefig(f'{argv[1]}.png')