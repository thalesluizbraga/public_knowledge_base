1. Tipos dados

Variáveis: espaços em memoria que sao atualizados toda vez que o programa roda. Os tipos de dados primitivos que uma variavel pode receber sao:

Inteiros (int): Representam números inteiros. Operaçoes permitidas: +, -, /, *, **
Ponto Flutuante (float): Representam números reais. Operaçoes permitidas: +, -, /, *, **
Strings (str): Representam sequências de caracteres. Metodos permitidos: lower.(), strip(), upper(), split()
Booleanos (bool): Representam valores verdadeiros (True) ou falsos (False). Operaçoes permitidas: and, ou, not, == , !=

2. TypeError, Type Check, Type Conversion, try-except e if

2.1 Um TypeError ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

Exemplo de TypeError
Um exemplo clássico é tentar utilizar a função len() com um inteiro, o que resulta em TypeError, pois len() espera uma str, lista ou tupla pra contar o numero de caracteres e nao um inteiro.

2.2 Type Check
Para verificar o tipo de uma variavel usar type() ou isinstance().

2.3 Type Conversion
Para conversao de tipagem usar int(), float(), str(), etc.

2.4 try-except
Como python é uma linguagem scriptada (le linha a linha do codigo), se existir uma linha com erro ele logo para. Para contornar isso pode-se utilizar o try-except.

    try: o programa tenta tudo o que esta dentro do bloco de codigo.
    except: se algum erro dentro do try acontecer, um tratamento pelo except vai acontecer.

2.5 if
O codigo roda com base em condiçoes. Se ela for verdadeira, o que estiver identado na condicao sera executado, se nao, passara para outra condicao. 

    if: Avalia uma condição. Se a condição for verdadeira, executa o bloco de código associado.
    elif: Abreviação de "else if". Permite verificar múltiplas condições em sequência.
    else: Executa um bloco de código se todas as condições anteriores no if e elif forem falsa

3. Estruturas de Controle de Fluxo

3.1 FOR 
O loop for é utilizado para iterar sobre os itens de qualquer sequência, como listas, strings, ou objetos de dicionário, e executar um bloco de código para cada item. É especialmente útil quando você precisa executar uma operação para cada elemento de uma coleção.


3.2 WHILE
O loop while é uma estrutura de controle de fluxo fundamental em Python, permitindo executar um bloco de código repetidamente enquanto uma condição especificada é avaliada como verdadeira (True). Na engenharia de dados, o uso do while pode ser extremamente útil para diversas tarefas, como monitoramento contínuo de fontes de dados, execução de processos de ETL (Extract, Transform, Load) até que não haja mais dados para processar, ou mesmo para implementar tentativas de reconexão automáticas a serviços ou bancos de dados quando a primeira tentativa falha.

Exemplo de Uso do while em Engenharia de Dados
Um cenário comum em engenharia de dados é a necessidade de executar uma tarefa de maneira periódica, como verificar novos dados em um diretório, fazer polling de uma API para novas respostas ou monitorar mudanças em um banco de dados. Nestes casos, um loop while pode ser utilizado para manter o script rodando continuamente ou até que uma condição específica seja atingida (por exemplo, um sinal para desligar ou uma condição de erro).

Exemplo Prático: while True com Pausa
Um exemplo direto do uso de while True em Python é criar um loop infinito que executa uma ação a cada intervalo definido, como imprimir uma mensagem a cada 10 segundos. Isso pode ser útil para monitorar processos ou dados em tempo real com uma verificação periódica.

    import time

    while True:
        print("Verificando novos dados...")
        # Aqui você pode adicionar o código para verificar novos dados,
        # por exemplo, checar a existência de novos arquivos em um diretório,
        # fazer uma consulta a um banco de dados ou API, etc.
        
        time.sleep(10)  # Pausa o loop por 10 segundos

4. Type hint, Tipos complexos (Dicionários vs DataFrames Vs Tabelas Vs Excel) e Funções

4.1 Type Hint
O uso de Type Hint ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis. Na engenharia de dados, isso é especialmente útil para garantir que as funções de manipulação e análise de dados recebam os dados no formato correto, reduzindo erros em tempo de execução.


Na Python, a tipagem de funções é facilitada pelo uso de "Type Hints" (Dicas de Tipo), uma característica introduzida no Python 3.5 através do PEP 484. Os Type Hints permitem aos desenvolvedores especificar os tipos de dados esperados para os parâmetros de uma função e o tipo de dado que a função deve retornar. Embora essas dicas de tipo não sejam estritamente aplicadas em tempo de execução, elas são extremamente úteis para ferramentas de análise estática de código, melhorando a legibilidade do código e ajudando na detecção precoce de erros.

Tipagem Fraca vs. Forte
Tipagem Forte: Em linguagens com tipagem forte, uma vez que uma variável é atribuída a um tipo, não pode ser automaticamente tratada como outro tipo sem uma conversão explícita. Python é um exemplo de linguagem com tipagem forte. Isso significa que operações que misturam tipos incompatíveis (como adicionar um número a uma string) resultarão em erro.

Tipagem Fraca: Linguagens com tipagem fraca permitem maior flexibilidade nas operações entre diferentes tipos, fazendo conversões de tipo implícitas. JavaScript é um exemplo clássico, onde você pode adicionar números a strings sem erros, resultando em uma concatenação de texto.

Tipagem Estática vs. Dinâmica
Tipagem Estática: Linguagens de tipagem estática, como Java e C++, exigem que o tipo de cada variável seja declarado explicitamente no momento da compilação. Isso ajuda a detectar erros de tipo antes da execução do programa, aumentando a segurança do tipo e potencialmente melhorando o desempenho.

Tipagem Dinâmica: Python é um exemplo de linguagem com tipagem dinâmica, onde os tipos são inferidos em tempo de execução e não precisam ser declarados explicitamente. Isso oferece flexibilidade e rapidez no desenvolvimento, mas pode aumentar o risco de erros de tipo que só serão detectados em tempo de execução.

4.2 Tipos Complexos

Listas e Dicionários
Importância na Engenharia de Dados
Listas e dicionários são estruturas de dados versáteis que permitem armazenar e manipular coleções de dados de forma eficiente. Na engenharia de dados, essas estruturas são fundamentais para organizar dados coletados de diversas fontes, facilitando operações como filtragem, busca, agregação e transformação de dados.

Lendo arquivos
Para ler um arquivo CSV em Python utilizando o módulo nativo, você pode usar a combinação do comando with open... para abrir o arquivo e o método .reader() do módulo csv para ler o arquivo linha por linha. O uso de with assegura que o arquivo será fechado corretamente após sua leitura, mesmo que ocorram erros durante o processo. Abaixo está um exemplo básico de como realizar essa operação:

    import csv

    # Caminho para o arquivo CSV
    caminho_arquivo = 'exemplo.csv'

    # Inicializa uma lista vazia para armazenar os dados
    dados = []

    # Usa o gerenciador de contexto `with` para abrir o arquivo
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        # Cria um objeto leitor de CSV
        leitor_csv = csv.DictReader(arquivo)
        
        # Itera sobre as linhas do arquivo CSV
        for linha in leitor_csv:
            # Adiciona cada linha (um dicionário) à lista de dados
            dados.append(linha)

    # Exibe os dados lidos do arquivo CSV
    for registro in dados:
        print(registro)

4. Funções

Importância na Engenharia de Dados
Funções permitem modularizar e reutilizar código, essencial para processar e analisar grandes conjuntos de dados. Na engenharia de dados, funções são usadas para encapsular lógicas de transformação, limpeza, agregação e análise de dados, tornando o código mais organizado e mantendo a qualidade do código.

As funções em programação são abstrações poderosas que permitem encapsular blocos de código para realizar tarefas específicas. Elas servem não apenas para organizar o código e torná-lo mais legível, mas também para abstrair complexidades, permitindo que os programadores pensem em problemas em um nível mais alto. Uma função bem projetada pode ser vista como um "mini-programa" dentro de um programa maior, com sua própria lógica e dados de entrada e saída.

