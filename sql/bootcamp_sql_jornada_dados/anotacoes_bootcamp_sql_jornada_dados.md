# 1 - Conceitos Gerais

Diferentemente do python, o SQL é uma linguagem declarativa que busca a otimizaçao. Existe um plano de execuçao das queries, buscando sempre a execuçao que tome o menor tempo e esforço. O python nao possui isso, seguindo apenas a ordem do codigo escrito, pelo fato de ser uma linguagem scriptada.

O Postgre trabalha num modelo client x servidor, em que o cliente com uma aplicaçao (dbeaver, pageadmin, vscode) faz as solicitaçoes ao servidor onde esta o banco de dados.

No mundo real, o client nao esta na mesma maquina do servidor, e entao a comunicaçao dos dois é feita por meio de conexao de rede TCP/IP.

Dentro da linguagem SQL existem os subtipos que englobam comandos com objetivos diferentes como (DDL, DML, DQL, DCL, TCL). 

    - DDL (Definition Data Language) > Comandos com o intuito de alterar a forma do banco.
    Exemplos: Create, Alter, Drop, Truncate.
    Responsável: DBA.

    - DML (Data Manipulation Language) > Comandos com o intuito de atualizar ou deletar registros.
    Exemplos: Insert, Update, Delete, Merge. 
    Responsável: Devs, analistas de dados.

    - DQL (Data Query Language) > Comandos com o intuito de consultar registros.
    Exemplos: Select, Group By, Order By. 
    Responsável: Analista de dados, cientistas de dados.

    - DCL (Data Control Language) > Comandos com o intuito de garantir controles e acessos.
    Exemplos: Grant, Revoke. 
    Responsável: DBA.
 
    - TCL (Transaction Control Language) > Comandos com o intuito de garantir a execução e confiabilidade das transaçoes no banco.
    Exemplos: Commit, Rollback, Savepoint. 
    Responsável: DBA.
 
# 2 - Join e Having

Existem alguns tipos de joins no SQL que sao:

    - inner join
    - right join
    - left join
    - full join

O having é o where para group by. So pode ser usado depois do group by e filtra grupos, nao linhas coo o where.

# 3 - Window Functions

Possibilitam calculos a partir de partiçoes para agregar ou rankear dados. A sintaxe é:

window_function() over (partition by nome_coluna order by nome_coluna)

O comando de partition by é opcional na window function, o resto é obrigatorio. Exemplo:

'''
sql 

SELECT DISTINCT order_id,
   COUNT(order_id) OVER (PARTITION BY order_id) AS unique_product,
   SUM(quantity) OVER (PARTITION BY order_id) AS total_quantity,
   SUM(unit_price * quantity) OVER (PARTITION BY order_id) AS total_price
FROM order_details
ORDER BY order_id;

'''

Window functions mais utilizadas:

    - rank() > em caso de empate no rank, duas linhas podem ficar em primeiro e a linha apos em terceiro.
    - dense_rank() > em caso de empate, duas linhas podem ficar em primeiro e a linha apos em segundo.
    - row_number() > em caso de empate, o proprio postgre define um criterio de desempate para as linhas. Portanto, nao existe a possibilidade de duas linhas ficarem em primeiro.
    - lead() > traz a linha anterior para a atual. 
    - lag() > traz a linha atual para a anterior.

# 4 - CTE vs Subqueries vs Views vs Temporary Tables vs Materialized Views

CTEs sao recomendadas quando é necessario dividir uma consulta em partes mais gerenciáveis ou quando deseja reutilizar uma subconsulta várias vezes na mesma consulta principal.

    Vantagens: Permitem escrever consultas mais legíveis e organizadas, dividindo a lógica em partes distintas.Podem ser referenciadas várias vezes na mesma consulta.
    Desvantagens: Podem não ser tão eficientes quanto outras técnicas, especialmente se a CTE for referenciada várias vezes ou se a consulta for muito complexa.

Subqueries são úteis quando você precisa de resultados intermediários para filtrar ou agregar dados em uma consulta principal.

    Vantagens: São simples de escrever e entender, especialmente para consultas SIMPLES.
    Podem ser aninhadas dentro de outras subqueries ou consultas principais.
    Desvantagens: Pode tornar consultas complexas difíceis de entender e manter.
    Em algumas situações, podem não ser tão eficientes quanto outras técnicas, especialmente se as subqueries forem executadas várias vezes.

Views são úteis quando você precisa reutilizar uma consulta em várias consultas ou quando deseja simplificar consultas complexas dividindo-as em partes menores.

    Vantagens: Permitem abstrair a lógica de consulta complexa em um objeto de banco de dados reutilizável.Facilitam a segurança, pois você pode conceder permissões de acesso à view em vez das tabelas subjacentes.
    Desvantagens: As views não armazenam dados fisicamente, então elas precisam ser reavaliadas sempre que são consultadas, o que pode impactar o desempenho.Se uma view depende de outras views ou tabelas, a complexidade pode aumentar.

Temporary Tables / Staging / Testes ETL são úteis quando você precisa armazenar dados temporários para uso em uma sessão de banco de dados ou em uma consulta específica.
    
    Vantagens: Permitem armazenar resultados intermediários de uma consulta complexa para reutilização posterior.Podem ser indexadas para melhorar o desempenho em consultas subsequentes.
    Desvantagens: Podem consumir recursos do banco de dados, especialmente se forem grandes.Exigem gerenciamento explícito para limpar os dados após o uso. Os dados sao perdidos depois do fim da sessao.

Materialized Views / Snapshot são úteis quando você precisa pré-calcular e armazenar resultados de consultas complexas para consultas frequentes ou análises de desempenho.
    
    Vantagens: Permitem armazenar fisicamente os resultados de uma consulta, melhorando significativamente o desempenho em consultas subsequentes.Reduzem a carga no banco de dados, já que os resultados são pré-calculados e armazenados.
    Desvantagens: Precisam ser atualizadas regularmente para manter os dados atualizados, o que pode consumir recursos do sistema. A introdução de dados redundantes pode aumentar os requisitos de armazenamento.

# 5-  Stored Procedures

As Stored Procedures são abstrações de transações que consistem em um conjunto de instruções SQL pré-compiladas e armazenadas no banco de dados.

Elas são usadas para encapsular operações de banco de dados mais complexas, como atualizações, inserções, exclusões e outras transações.

As Stored Procedures podem aceitar parâmetros de entrada e retornar valores de saída, o que as torna altamente flexíveis e reutilizáveis em diferentes partes de um aplicativo. Elas oferecem maior controle sobre as operações de banco de dados e permitem a execução de lógica de negócios no lado do servidor.


Exemplo de procedure que fornece uma visão detalhada do extrato bancário de um cliente, incluindo seu saldo atual e as informações das últimas 10 transações realizadas. Esta operação recebe como entrada o ID do cliente e retorna uma mensagem com o saldo atual do cliente e uma lista das últimas 10 transações, contendo o ID da transação, o tipo de transação (depósito ou retirada), uma breve descrição, o valor da transação e a data em que foi realizada.


'''
sql

CREATE OR REPLACE PROCEDURE ver_extrato(
    IN p_cliente_id INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    saldo_atual INTEGER;
    transacao RECORD;
    contador INTEGER := 0;
BEGIN
    -- Obtém o saldo atual do cliente
    SELECT saldo INTO saldo_atual
    FROM clients
    WHERE id = p_cliente_id;

    -- Retorna o saldo atual do cliente
    RAISE NOTICE 'Saldo atual do cliente: %', saldo_atual;

    -- Retorna as 10 últimas transações do cliente
    RAISE NOTICE 'Últimas 10 transações do cliente:';
    FOR transacao IN
        SELECT *
        FROM transactions
        WHERE cliente_id = p_cliente_id
        ORDER BY realizada_em DESC
        LIMIT 10
    LOOP
        contador := contador + 1;
        RAISE NOTICE 'ID: %, Tipo: %, Descrição: %, Valor: %, Data: %', transacao.id, transacao.tipo, transacao.descricao, transacao.valor, transacao.realizada_em;
        EXIT WHEN contador >= 10;
    END LOOP;
END;
$$;

'''

# 6-  Triggers

Triggers são procedimentos armazenados, que são automaticamente executados ou disparados quando eventos específicos ocorrem em uma tabela ou visão. Sao executados em resposta a comandos de insert, update e delete.

O maior objetivo do trigger é automatizar uma atualizaçao no banco.

Exemplo de trigger:

'''
sql
-- Criação da tabela Produto
CREATE TABLE Produto (
    cod_prod INT PRIMARY KEY,
    descricao VARCHAR(50) UNIQUE,
    qtde_disponivel INT NOT NULL DEFAULT 0
);

-- Inserção de produtos
INSERT INTO Produto VALUES (1, 'Basica', 10);
INSERT INTO Produto VALUES (2, 'Dados', 5);
INSERT INTO Produto VALUES (3, 'Verao', 15);

-- Criação da tabela RegistroVendas
CREATE TABLE RegistroVendas (
    cod_venda SERIAL PRIMARY KEY,
    cod_prod INT,
    qtde_vendida INT,
    FOREIGN KEY (cod_prod) REFERENCES Produto(cod_prod) ON DELETE CASCADE
);

'''

''' 
sql

-- Criação de um TRIGGER
CREATE OR REPLACE FUNCTION verifica_estoque() RETURNS TRIGGER AS $$
DECLARE
    qted_atual INTEGER;
BEGIN
    SELECT qtde_disponivel INTO qted_atual
    FROM Produto WHERE cod_prod = NEW.cod_prod;
    IF qted_atual < NEW.qtde_vendida THEN
        RAISE EXCEPTION 'Quantidade indisponivel em estoque'
    ELSE
        UPDATE Produto SET qtde_disponivel = qtde_disponivel - NEW.qtde_vendida
        WHERE cod_prod = NEW.cod_prod;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_verifica_estoque 
BEFORE INSERT ON RegistroVendas
FOR EACH ROW 
EXECUTE FUNCTION verifica_estoque();

'''

'''
sql

-- Tentativa de venda de 5 unidades de Basico (deve ser bem-sucedida, pois há 10 unidades disponíveis)
INSERT INTO RegistroVendas (cod_prod, qtde_vendida) VALUES (1, 5);

-- Tentativa de venda de 6 unidades de Dados (deve ser bem-sucedida, pois há 5 unidades disponíveis e a quantidade vendida não excede o estoque)
INSERT INTO RegistroVendas (cod_prod, qtde_vendida) VALUES (2, 5);

-- Tentativa de venda de 16 unidades de Versao (deve falhar, pois só há 15 unidades disponíveis)
INSERT INTO RegistroVendas (cod_prod, qtde_vendida) VALUES (3, 16);

'''

# 7 - Transação

Uma transaçao é uma coleção de queries.Uma unidade de trabalho Muitas vezes precisamos mais de uma "querie" para querer o que queremos ex: para fazer uma transação financeira, precisamos selecionar uma conta e verificar se ela possui o dnheiro (SELECT), fazer a remoção do dinheiro da conta que irá transferir o dinheiro (UPDATE) e fazer o incremento do dinheiro na conta alvo (UPDATE). Tudo isso precisa estar dentro da mesma transação.

Toda transação inicia com um BEGIN.Toda transação finaliza com um COMMIT (em memória).Toda transação, pode falhar, precisa de um ROLLBACK.Normalmente transações são usadas para MODIFICAR dados, mas é possível ter uma transação com somente leitura , exemplo: você quer gerar um relatório e quer que esses dados sejam confiáveis e ter uma SNAPSHOT.

Conceito de ACID:

Atomicidade > A transaçao deve ser indivisível. Nao existe uma transaçao meio certa. Ou ela deu certo e aconteceu, ou nao deu certo e nao aconteceu.

Consistencia > Caso o banco faça uma tansaçao invalida, ele volta para o estado anterior e ela nao acontece. As operações serão legítimas se passarem por todas as verificações do banco de dados, incluindo todas as restrições inseridas nele (gatilhos, funções, procedimentos, entre outros). Ou seja, se eu tenho 100 reais na conta e tento tirar 110, a transação tem que falhar porque nao passou nos constraints do banco.

Isolamento > Uma transação nao pode afetar a outra. Vários usuários podem ler e gravar na mesma tabela ao mesmo tempo, mas as transações são isoladas para que as simultâneas não interfiram ou afetem umas às outras. Na verdade, cada solicitação é tratada como se estivesse ocorrendo de forma independente, mesmo que ocorram simultaneamente.

Durabilidade > A transaçao realizada perdura no tempo. 


# 8 - Ordem de consulta

Antes de executar a consulta, o mecanismo SQL cria um plano de execução para reduzir o consumo de recursos. Este plano oferece detalhes valiosos como custos estimados, algoritmos de junção, ordem das operações e mais. Este é um resultado abrangente, e pode ser acessado se necessário. A ordem de execução segue abaixo:

    1.FROM
    2.JOIN (e ON)
    3.WHERE
    4.GROUP BY
    5.HAVING
    6.SELECT
    7.ORDER BY
    8.LIMIT

No entanto, o Postgre usa o limit em todas as etapas do processo de execuçao para otimizar a consulta. Ou seja, o limit aparecendo na ultima etapa do plano de execuçao é uma mentirinha.

# 9- Indexing

Índices em bancos de dados são estruturas utilizadas para melhorar a eficiência de consultas, permitindo acesso rápido aos dados. Por exemplo, considere uma tabela de alunos em um banco de dados escolar. Sem índices, uma consulta para encontrar o aluno com um determinado ID exigiria uma busca sequencial na tabela. Com um índice, o banco de dados pode ir diretamente para a linha correspondente ao ID especificado.

Existem vários tipos de índices, incluindo índices de árvore B, índices hash e índices de bitmap. Cada tipo tem suas próprias características e utilizações adequadas.

Os índices são geralmente criados com base em uma ou mais colunas de uma tabela. Quando uma consulta é feita usando uma dessas colunas, o banco de dados pode usar o índice correspondente para localizar rapidamente as linhas relevantes na tabela.

As vantagens dos índices incluem consultas mais rápidas e eficientes, enquanto as desvantagens incluem custo adicional de armazenamento e sobrecarga de atualização durante operações de inserção, atualização e exclusão.

Estruturas de Dados B-Tree

Uma B-Tree é uma árvore balanceada que é frequentemente usada em bancos de dados e sistemas de arquivos. Ela é projetada para permitir inserções, exclusões e pesquisas eficientes em grandes conjuntos de dados, mantendo a árvore balanceada e otimizando a profundidade da árvore.

Uma B-Tree consiste em nós, onde cada nó pode ter várias chaves e vários ponteiros para outros nós. Cada nó tem um número mínimo e máximo de chaves e ponteiros, mantendo a árvore balanceada.

As operações básicas em uma B-Tree incluem inserção, remoção e busca. Por exemplo, durante uma busca, a árvore é percorrida de acordo com a chave procurada, reduzindo eficientemente o espaço de busca a cada passo.

As B-Trees possuem várias propriedades, como balanceamento automático, garantindo que a profundidade da árvore seja mantida em um nível aceitável, mesmo com muitas inserções e remoções.

As B-Trees são amplamente utilizadas em bancos de dados para índices, como índices de chaves primárias e secundárias, devido à sua eficiência e capacidade de manipular grandes volumes de dados.

# 10 - Partition

O particionamento de dados é uma abordagem empregada para estender o armazenamento de dados dentro de um esquema existente. Na verdade, trata-se de um conceito relativamente simples – se você tiver problemas para acessar grandes volumes de dados, simplesmente divida os objetos de armazenamento (geralmente, as tabelas) em objetos menores.