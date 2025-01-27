# Consumo de Energia Elétrica no Brasil

## Coleta de Dados
O projeto utiliza dados de consumo de energia elétrica no Brasil provenientes do **Ministério de Minas e Energia (MME)**. A coleta foi realizada a partir de fontes públicas disponíveis no [basedosdados.org](https://basedosdados.org/dataset/3e31e540-81ba-4665-9e72-3f81c176adad?table=b955feef-1649-428b-ba46-bc891d2facc2), com importação para análise.

## Modelagem
Foi realizada uma **análise exploratória** dos dados, seguida de transformações utilizando a biblioteca **Pandas** para a criação de modelos de previsão com **scikit-learn**. O módulo **LinearRegression** foi utilizado para identificar a tendência do consumo de energia no Brasil.

Para visualização dos dados, foram utilizadas as bibliotecas **Matplotlib** e **Seaborn** para exibir o consumo de energia e as tendências.

## Conclusões
As conclusões destacam os seguintes pontos principais:

- **Sazonalidade** é o principal fator que afeta o consumo de energia, independentemente do setor.
- A expansão da **energia elétrica para áreas rurais** e locais anteriormente sem abastecimento contribuiu para um aumento significativo no número de consumidores residenciais.
- O **aumento no consumo residencial** também está ligado à maior acessibilidade de **eletrodomésticos e tecnologias**, que antes não estavam ao alcance da população.

Em relação ao consumo comercial:
- O consumo **comercial** apresenta tendência de crescimento, um pouco menor que o residencial, com aumento à medida que as áreas urbanas se expandem.

No setor **industrial**:
- O número de consumidores industriais é relativamente estável, mas ao observar os dados, é possível identificar uma leve tendência de crescimento, especialmente a cada 8 anos.

