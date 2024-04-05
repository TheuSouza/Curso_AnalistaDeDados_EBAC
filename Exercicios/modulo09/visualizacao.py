from sys import argv

import pandas as pd
import seaborn as sns

df = pd.read_csv('./taxa-cdi.csv')

grafico = sns.lineplot(x=df['Hora'], y=df['Taxa'])
grafico.tick_params(axis='x', labelrotation=45)
grafico.get_figure().savefig(f'{argv[1]}.png')