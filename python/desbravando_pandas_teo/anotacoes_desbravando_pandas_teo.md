

-- .iloc pega pela posição e .loc pelo index (e o index pode mudar).
-- df.rename() para renomear colunas.
-- df.drop_duplicates() para remover duplicadas.
-- df.sort_values() para ordenar uma ou mais colunas.
    
    df = df.sort_values('dt_transaction', ascending=False).drop_duplicates(subset=['id_customer'], keep='first') >>  ultima transação de cada cliente

-- df.astype() para mudar tipos de dados.
-- df.merge() para fazer join de dois datasets.
-- pd.concat() para appendar dois datasets (pelos index).
-- df.apply() para aplicar uma funcao no dataset. É possivel usar uma funçao dentro do apply como argumento (ver doc de exemplos)
-- df.isna().sum() para obter o numero de nas.
-- df.fillna() para preencher os nas com algo. Da para colocar uma coluna preenchendo o na pela media e outra com zero por exemplo.
-- df.dropna() para dropar linhas com na. Da para colocar como argumento mais de uma coluna a ser considerada para dropar ou nao a linha, ou seja, se uma linha tiver na em mais de uma coluna, ela é dropada, se nao, nao. 