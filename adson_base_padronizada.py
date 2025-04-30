import pandas as pd

# Criando um dataframe com os dados do arquivo fornecido
alunos_df = pd.read_csv('Base_despadronizada.csv')

# Verificando todas as possibilidades de respostas presentes na coluna "sexo"
print(alunos_df['sexo'].value_counts())

# Padronizando os valores presentes na coluna "sexo" a partir do valor já existente
alunos_df.loc[(alunos_df['sexo'] == 'M') | (alunos_df['sexo'] == 'masc') , 'sexo'] = 'Masculino'
alunos_df.loc[(alunos_df['sexo'] == 'F') | (alunos_df['sexo'] == 'fem') , 'sexo'] = 'Feminino'

#Substituindo as vírgulas por pontos para cálculo das médias
alunos_df['nota_matematica'] = alunos_df['nota_matematica'].str.replace(',','.')
alunos_df['nota_portugues'] = alunos_df['nota_portugues'].str.replace(',','.')

# Transformando todas as valores das colunas de notas de matemática e português para o tipo float para em seguida realizar cálculo da média
alunos_df['nota_matematica'] = alunos_df['nota_matematica'].astype(float)
alunos_df['nota_portugues'] = alunos_df['nota_portugues'].astype(float)

# Criando a coluna das médias dos alunos a partir do cálculo das notas e da frequência
alunos_df['Média'] = (alunos_df['nota_matematica'] + alunos_df['nota_portugues'] + (alunos_df['frequencia'] / 10) ) / 3

# Criando a coluna de 'Aprovado' e a preenchendo de acordo com a nota do aluno
alunos_df.loc[alunos_df['Média'] >= 7, 'Aprovado'] = 'Sim'
alunos_df.loc[alunos_df['Média'] < 7, 'Aprovado'] = 'Não'

# Padronizando de acordo com a formatação do Brasil, substituindo vírgulas por pontos com o uso do replace. Além de determinar as médias com 2 casas decimais
alunos_df['nota_matematica'] = alunos_df['nota_matematica'].apply(lambda x: f"{x}".replace('.', ','))
alunos_df['nota_portugues'] = alunos_df['nota_portugues'].apply(lambda x: f"{x}".replace('.', ','))
alunos_df['frequencia'] = alunos_df['frequencia'].apply(lambda x: f"{x}".replace('.', ','))
alunos_df['Média'] = alunos_df['Média'].apply(lambda x: f"{x:,.2f}".replace('.', ','))

alunos_df.to_csv('adson_base_padronizada.csv')