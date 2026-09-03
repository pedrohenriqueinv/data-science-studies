# 🗄️ Fundamentos de SGBD & Modelagem Relacional — Guia de Estudos Definitivo

> **Disciplina:** Sistemas Gerenciadores de Banco de Dados (SGBD)  
> **Formato:** Manual Didático Prático com Estudo de Caso (*Biblioteca Universitária* / PostgreSQL)  
> **Conteúdo:** Propriedades ACID • Subgrupos SQL • Manipulação DML • Transações • Panorama de SGBDs • 15 Questões Comentadas (Preparatório AV1)

---

## 📑 Sumário do Conteúdo Programático

1. [Semana 1: Introdução aos Bancos de Dados, SGBDs e Modelos Históricos](#semana-1-introdução-aos-bancos-de-dados-sgbds-e-modelos-históricos)
2. [Semana 2: Propriedades ACID, Arquitetura Interna e Modelo Cliente-Servidor](#semana-2-propriedades-acid-arquitetura-interna-e-modelo-cliente-servidor)
3. [Semana 3: Linguagem SQL e os 5 Subgrupos (DDL, DML, DQL, DCL, TCL)](#semana-3-linguagem-sql-e-os-5-subgrupos)
4. [Semana 4: Manipulação de Dados (DML), Integridade Referencial (PK/FK) e Transações](#semana-4-manipulação-de-dados-dml-integridade-referencial-e-transações)
5. [Semana 5: Seminário Comparativo dos Principais SGBDs Relacionais](#semana-5-seminário-comparativo-dos-principais-sgbds-relacionais)
6. [Semana 6: Resumo Estratégico, Mapa Mental e Pegadinhas Clássicas de Prova](#semana-6-resumo-estratégico-mapa-mental-e-pegadinhas-clássicas)
7. [Semana 7: Bateria de 15 Questões de Fixação com Gabarito Comentado](#semana-7-bateria-de-15-questões-de-fixação-com-gabarito-comentado)

---

## SEMANA 1: Introdução aos Bancos de Dados, SGBDs e Modelos Históricos

Toda aplicação de software moderna necessita de uma forma confiável, estruturada e segura de armazenar informações. Sem sistemas especializados, os dados seriam mantidos em arquivos de texto soltos, sujeitos a corrupção catastrófica, falhas de segurança e perda irreversível em quedas de energia.

### 1.1 Dados vs. Informação: A Matéria-Prima e o Significado

* **📦 Dado (Elemento Bruto):**  
  É o registro isolado, cru e sem contexto. Não transmite conhecimento por si só.  
  *Exemplos:* "25"\, "02/09/2026"\, "Aline"\, "True"\.

* **💡 Informação (Dado Processado):**  
  É o dado organizado, contextualizado e útil para a tomada de decisão.  
  *Exemplo:* *"A aluna Aline retirou o livro de ID 25 em 02/09/2026 e a devolução está pendente."*

> 🍞 **Analogia do Dia a Dia (Farinha vs. Bolo Pronto):**  
> O **Dado** é o trigo e o açúcar no armário: matéria-prima solta.  
> A **Informação** é o bolo de aniversário confeitado, fruto do processamento inteligente dos ingredientes.

---

### 1.2 O que é um Banco de Dados e o que é um SGBD?

* **Banco de Dados (*Database*):** Coleção estruturada de dados logicamente correlacionados que modelam aspectos do mundo real (ex.: o acervo e os alunos de uma universidade).
* **SGBD (Sistema Gerenciador de Banco de Dados / *DBMS*):** Software responsável por intermediar todas as ações entre os usuários/aplicações e os arquivos físicos no disco. Ele controla acesso, integridade, concorrência e segurança.

---

### 1.3 As 4 Grandes Funções de um SGBD Moderno

1. **Criação e Definição de Estruturas:** Definição de tabelas, tipos de dados, chaves primárias e relacionamentos.
2. **Manipulação e Consulta de Dados:** Inserção, alteração, exclusão e consultas rápidas com filtros complexos.
3. **Controle de Acesso e Segurança:** Autenticação, controle de permissões granulares por usuário e criptografia.
4. **Integridade e Recuperação de Falhas:** Garantia de que panes elétricas ou travamentos não corrompam os dados (*Backup* e logs transacionais).

---

### 1.4 A Evolução Histórica dos Modelos de Dados

| Modelo & Época | Estrutura e Conceito | Vantagens | Desvantagens / Limitações |
| :--- | :--- | :--- | :--- |
| **1. Hierárquico**<br>*(Anos 1960 - IMS/IBM)* | Organizado em **Árvore** (Pai e Filho). Cada filho possui estritamente um único pai. | Rápido para hierarquias estáticas simples. | Rigidez extrema; não suporta relacionamentos N:N naturalmente. |
| **2. Em Rede**<br>*(Anos 1970 - CODASYL)* | Organizado em **Grafo / Rede**. Registros filhos podem ter múltiplos registros pais. | Maior flexibilidade para modelar conexões complexas. | Navegação manual por código com ponteiros complexos em disco. |
| **3. Relacional**<br>*(Anos 1980 - Edgar Codd)* | Organizado em **Tabelas bidimensionais (Relações)** interligadas por chaves. Linguagem SQL declarativa. | Simplicidade matemática, independência física/lógica e padrão universal. | Necessidade de migrações em esquemas altamente variáveis. |
| **4. Orientado a Objetos**<br>*(Anos 1990 - ODBMS)* | Armazena classes, objetos, atributos, métodos, herança e polimorfismo diretamente. | Integração nativa com linguagens orientadas a objetos (POO). | Alta complexidade de administração e baixa padronização no mercado. |

---

### 1.5 Bancos Relacionais (SQL) vs. Bancos Não-Relacionais (NoSQL)

* **Bancos Relacionais (SQL):** Esquema estrito (tabelas e colunas fixas), integridade referencial rígida e conformidade às Propriedades ACID (*PostgreSQL, MySQL, Oracle, SQL Server*). Ideais para finanças, e-commerce e ERPs.
* **Bancos NoSQL (*Not Only SQL*):** Esquema flexível/dinâmico, escalabilidade horizontal massiva para grandes volumes:
  * **Documentos (JSON):** *MongoDB* — catálogos dinâmicos e conteúdo flexível.
  * **Chave-Valor:** *Redis* — altíssima velocidade em memória RAM para cache e sessões.
  * **Grafos:** *Neo4j* — conexões complexas entre nós (redes sociais, motores de recomendação).
  * **Colunares:** *Apache Cassandra* — análise massiva de séries temporais e Big Data.

---

## SEMANA 2: Propriedades ACID, Arquitetura Interna e Modelo Cliente-Servidor

Para que um banco de dados seja confiável em cenários de alta concorrência (milhares de acessos simultâneos) e imune a panes elétricas, ele deve implementar o conceito de **Transação** e seguir rigorosamente as quatro **Propriedades ACID**.

### 2.1 O que é uma Transação?
Uma **Transação** é uma sequência lógica de uma ou mais operações SQL tratadas como uma **unidade de trabalho indivisível**. Ou todas as operações ocorrem com êxito, ou nenhuma alteração persiste.

### 2.2 As 4 Propriedades ACID em Detalhes

\\\
      A ➔ Atomicidade   (Princípio do "Tudo ou Nada")
      C ➔ Consistência  (Preservação das Regras de Negócio e Constraints)
      I ➔ Isolamento    (Concorrência Segura sem Interferência Mútua)
      D ➔ Durabilidade  (Persistência Garantida mesmo após Queda de Energia)
\\\

* **🅰️ Atomicidade (*Atomicity*):**  
  Se qualquer operação intermediária falhar, o SGBD aciona o \ROLLBACK\ e reverte todas as ações anteriores.  
  *Exemplo:* Em uma transferência, se debitou da Conta A mas falhou ao creditar na Conta B, o débito da Conta A é desfeito imediatamente.
* **🅲 Consistência (*Consistency*):**  
  A transação deve conduzir o banco de um estado válido para outro estado válido, respeitando todas as restrições (PK, FK, CHECK, NOT NULL).  
  *Exemplo:* O saldo final de uma conta não pode violar uma regra de negócio nem criar referências órfãs.
* **🅸 Isolamento (*Isolation*):**  
  Transações simultâneas não devem interferir umas nas outras. O resultado de transações paralelas deve ser idêntico ao de sua execução em fila sequencial.  
  *Exemplo:* O Usuário 2 não pode ler dados parciais ou temporários que o Usuário 1 ainda não confirmou.
* **🅳 Durabilidade (*Durability*):**  
  Uma vez que o comando \COMMIT\ retorna com sucesso, as alterações são gravadas de forma permanente e sobrevivem a desligamentos do servidor.  
  *Mecanismo:* Gravação prévia no **Write-Ahead Log (WAL)** em disco antes da confirmação.

---

### 2.3 Níveis de Isolamento ANSI SQL e Anomalias de Concorrência

| Nível de Isolamento | Leitura Suja (*Dirty Read*) | Leitura Não-Repetível (*Non-Repeatable*) | Leitura Fantasma (*Phantom Read*) | Características |
| :--- | :---: | :---: | :---: | :--- |
| **1. Read Uncommitted** | ⚠️ Ocorre | ⚠️ Ocorre | ⚠️ Ocorre | Mais veloz, porém lê dados não confirmados (sem segurança). |
| **2. Read Committed** *(Padrão)* | ✅ Protegido | ⚠️ Ocorre | ⚠️ Ocorre | **Padrão do PostgreSQL e Oracle.** Excelente equilíbrio geral. |
| **3. Repeatable Read** | ✅ Protegido | ✅ Protegido | ⚠️ Ocorre *(em alguns SGBDs)* | Garante que o mesmo \SELECT\ retorne dados idênticos durante toda a transação. |
| **4. Serializable** | ✅ Protegido | ✅ Protegido | ✅ Protegido | Isolamento máximo (simula execução em fila estrita, com maior custo de lock). |

---

### 2.4 Arquitetura Interna de um SGBD

* ⚙️ **Motor de Execução (*Execution Engine*):** Executa as etapas do plano físico de consulta gerado pelo otimizador.
* 🧠 **Otimizador de Consultas (*Planner/Optimizer*):** Analisa o SQL e escolhe o caminho mais veloz (ex.: varredura sequencial vs. índice B-Tree).
* ⚡ **Gerenciador de Buffer (*Buffer Pool Manager*):** Mantém páginas de dados em memória RAM para evitar leituras lentas de disco.
* 💾 **Gerenciador de Armazenamento (*Storage Manager*):** Aloca e organiza blocos e arquivos de dados fisicamente no HDD/SSD.
* 🔒 **Gerenciador de Concorrência (*Concurrency Manager*):** Controla travas (*Locks*) e versões de linhas (**MVCC - Multi-Version Concurrency Control**) para suportar múltiplos usuários.
* 🛡️ **Gerenciador de Recuperação (*Recovery Manager*):** Garante a durabilidade transacional utilizando o log (WAL) para refazer (\REDO\) ou desfazer (\UNDO\).

---

### 2.5 Arquitetura Cliente-Servidor em 3 Camadas

\\\
[ 1. Apresentação ]          [ 2. Aplicação ]                 [ 3. Dados (SGBD) ]
 (Frontend / Mobile)  ──TCP──▶ (Backend API / Regras)  ──TCP──▶ (PostgreSQL :5432)
\\\

**Fluxo de Execução da Consulta:**
1. A aplicação envia a query via socket TCP (porta padrão \5432\ no PostgreSQL).
2. O servidor autentica a sessão e realiza a análise léxica/sintática (**Parser**).
3. O **Planner/Optimizer** calcula o custo computacional e gera o plano ótimo.
4. O **Execution Engine** busca os dados no **Buffer Pool** (RAM) ou disco.
5. O conjunto de resultados (**Result Set**) é serializado e retornado à aplicação.

---

## SEMANA 3: Linguagem SQL: Introdução aos 5 Subgrupos

A linguagem **SQL (*Structured Query Language*)** é um padrão internacional (ANSI/ISO) declarativo: o desenvolvedor declara **o que** deseja obter, e o SGBD determina **como** obter com máxima eficiência.

### 3.1 Os 5 Subgrupos da Linguagem SQL

| Subgrupo | Significado & Finalidade | Comandos Principais | Exemplo no Dia a Dia |
| :--- | :--- | :--- | :--- |
| **DDL** | **Data Definition Language**<br>Define e modifica a estrutura dos objetos do banco (tabelas, colunas, índices). | \CREATE\, \ALTER\, \DROP\, \TRUNCATE\, \RENAME\ | Construir a estante física da biblioteca e definir suas prateleiras. |
| **DML** | **Data Manipulation Language**<br>Manipula o conteúdo dentro das tabelas (linhas de registros). | \INSERT\, \UPDATE\, \DELETE\, \MERGE\ | Guardar um livro novo na prateleira ou alterar sua etiqueta. |
| **DQL** | **Data Query Language**<br>Focado na consulta e recuperação de dados sem alterá-los. | \SELECT\ (com \WHERE\, \JOIN\, \GROUP BY\, \ORDER BY\) | Consultar o catálogo da biblioteca para ver quais livros existem. |
| **DCL** | **Data Control Language**<br>Gerencia privilégios e permissões de segurança dos usuários. | \GRANT\, \REVOKE\, \DENY\ | Entregar ou recolher a chave da sala reservada da biblioteca. |
| **TCL** | **Transaction Control Language**<br>Controla e confirma blocos de transações no banco. | \BEGIN\, \COMMIT\, \ROLLBACK\, \SAVEPOINT\ | Carimbar o comprovante final ou rasgar a ficha em caso de erro. |

> ⚠️ **Pegadinha Clássica de Prova: \DROP\ vs \TRUNCATE\ vs \DELETE\**
> * **\DELETE FROM tabela WHERE ...\ (\DML\):** Exclui linha a linha, registra todas as operações no log transacional e permite \ROLLBACK\.
> * **\TRUNCATE TABLE tabela\ (\DDL\):** Limpa instantaneamente todas as páginas de dados no disco e reseta a sequência de auto-incremento (ID). Muito mais rápido, mas é comando estrutural DDL.
> * **\DROP TABLE tabela\ (\DDL\):** Apaga a tabela por completo (estrutura, colunas, dados e índices deixam de existir no banco).

---

### 3.2 Exemplos Práticos de Código em Cada Subgrupo (PostgreSQL)

\\\sql
-- 1. Comandos DDL (Criação e Alteração de Estrutura)
CREATE TABLE categorias (
    id_categoria SERIAL PRIMARY KEY,
    nome_categoria VARCHAR(100) NOT NULL UNIQUE
);

ALTER TABLE categorias ADD COLUMN descricao TEXT;

-- 2. Comandos DML e DQL (Manipulação e Consulta de Dados)
INSERT INTO categorias (nome_categoria, descricao)
VALUES ('Ficção Científica', 'Livros de exploração espacial e tecnologia futura');

UPDATE categorias 
SET descricao = 'Ficção científica clássica e contemporânea' 
WHERE id_categoria = 1;

SELECT id_categoria, nome_categoria 
FROM categorias 
ORDER BY nome_categoria ASC;

-- 3. Comandos DCL e TCL (Segurança e Controle Transacional)
GRANT SELECT ON categorias TO usuario_consulta;

BEGIN;
DELETE FROM categorias WHERE id_categoria = 99;
COMMIT;
\\\

---

## SEMANA 4: Manipulação de Dados (DML), Integridade Referencial & Transações

### 4.1 O Esquema da Biblioteca Universitária

\\\
┌────────────────────────┐         ┌────────────────────────┐         ┌──────────────────────────┐
│        autores         │ 1     N │         livros         │ 1     N │   transacoes_emprestimo  │
├────────────────────────┤─────────┤────────────────────────┤─────────┤──────────────────────────┤
│ PK  id_autor           │         │ PK  id_livro           │         │ PK  id_transacao         │
│     nome_autor         │         │ FK  id_autor           │         │ FK  id_livro             │
│     nacionalidade      │         │     titulo             │         │     nome_aluno           │
│     data_nascimento    │         │     ano_publicacao     │         │     data_emprestimo      │
└────────────────────────┘         │     qtd_disponivel     │         │     data_devolucao       │
                                   └────────────────────────┘         └──────────────────────────┘
\\\

#### DDL Completo com Constraints de Chave Primária (PK) e Estrangeira (FK)

\\\sql
-- 1. Tabela autores (Tabela Pai inicial)
CREATE TABLE autores (
    id_autor SERIAL PRIMARY KEY,
    nome_autor VARCHAR(150) NOT NULL,
    nacionalidade VARCHAR(80),
    data_nascimento DATE
);

-- 2. Tabela livros (Filha de autores)
CREATE TABLE livros (
    id_livro SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    id_autor INTEGER NOT NULL,
    ano_publicacao INTEGER,
    quantidade_disponivel INTEGER DEFAULT 0,
    CONSTRAINT livros_id_autor_fkey 
        FOREIGN KEY (id_autor) REFERENCES autores (id_autor)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- 3. Tabela transacoes_emprestimo (Filha de livros)
CREATE TABLE transacoes_emprestimo (
    id_transacao SERIAL PRIMARY KEY,
    id_livro INTEGER NOT NULL,
    nome_aluno VARCHAR(150) NOT NULL,
    data_emprestimo DATE NOT NULL DEFAULT CURRENT_DATE,
    data_devolucao DATE,
    CONSTRAINT transacoes_id_livro_fkey 
        FOREIGN KEY (id_livro) REFERENCES livros (id_livro)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
\\\

---

### 4.2 Integridade Referencial: Chave Primária (PK) e Chave Estrangeira (FK)

* 🔑 **Chave Primária (*PRIMARY KEY*):** Identifica exclusivamente cada registro da tabela. É estritamente **única** e **\NOT NULL\**. O SGBD cria automaticamente um índice B-Tree para buscas instantâneas.
* 🔗 **Chave Estrangeira (*FOREIGN KEY*):** Coluna que referencia a PK de outra tabela, garantindo que não existam registros órfãos (ex.: um livro apontando para um autor inexistente).

#### Ações Referenciais (\ON DELETE\ e \ON UPDATE\)

| Opção | Comportamento ao alterar/excluir o registro Pai | Aplicação Prática |
| :--- | :--- | :--- |
| **\RESTRICT / NO ACTION\** *(Padrão)* | Bloqueia a operação caso existam registros dependentes filhos. | Impede apagar um autor enquanto houver livros cadastrados em seu nome. |
| **\CASCADE\** | Propaga a exclusão ou alteração automaticamente para todos os filhos. | Ao atualizar o ID do autor, atualiza automaticamente na tabela de livros. |
| **\SET NULL\** | Mantém o registro filho, mas preenche o campo da FK com \NULL\. | Quando o vínculo entre as entidades for opcional. |

---

### 4.3 Comandos DML em Detalhes

#### 1. Inserção em Lote e Cláusula \RETURNING\
\\\sql
-- Inserção de múltiplos registros em um único round-trip de rede
INSERT INTO autores (nome_autor, nacionalidade, data_nascimento)
VALUES
    ('Machado de Assis', 'Brasileiro', '1839-06-21'),
    ('Clarice Lispector', 'Brasileira', '1920-12-10'),
    ('Jorge Amado', 'Brasileiro', '1912-08-10');

-- Inserção com RETURNING: captura imediatamente a PK gerada sem precisar de SELECT extra
INSERT INTO livros (titulo, id_autor, ano_publicacao, quantidade_disponivel)
VALUES ('Dom Casmurro', 1, 1899, 5)
RETURNING id_livro, titulo;
\\\

#### 2. Atualização Condicional Segura (\UPDATE\)
\\\sql
UPDATE livros
SET quantidade_disponivel = 7, ano_publicacao = 1900
WHERE id_livro = 1;
\\\
> 🚨 **PERIGO: UPDATE sem WHERE em Produção!**  
> Executar \UPDATE livros SET quantidade_disponivel = 0;\ sem a cláusula \WHERE\ atualizará **todos os registros** da tabela sem pedir confirmação! Em produção, sempre utilize o \WHERE\ filtrando pela Chave Primária.

#### 3. Exclusão e a Ordem Correta com \RESTRICT\
\\\sql
-- Tentativa de exclusão do autor que possui dependentes:
DELETE FROM autores WHERE id_autor = 1;
-- ERRO: update or delete on table "autores" violates foreign key constraint "livros_id_autor_fkey"

-- Ordem correta respeitando a hierarquia de integridade:
-- 1º: Excluir dependentes em transacoes_emprestimo
DELETE FROM transacoes_emprestimo WHERE id_livro = 1;
-- 2º: Excluir o registro em livros
DELETE FROM livros WHERE id_autor = 1;
-- 3º: Excluir o registro pai em autores com sucesso
DELETE FROM autores WHERE id_autor = 1;
\\\

---

### 4.4 Transações na Prática com PostgreSQL: BEGIN, COMMIT, ROLLBACK e SAVEPOINT

#### Fluxo Completo de Transação ACID de Empréstimo
\\\sql
BEGIN;

-- Passo 1: Decrementar a quantidade do livro em estoque
UPDATE livros
SET quantidade_disponivel = quantidade_disponivel - 1
WHERE id_livro = 1 AND quantidade_disponivel > 0;

-- Passo 2: Registrar a movimentação de empréstimo
INSERT INTO transacoes_emprestimo (id_livro, nome_aluno, data_emprestimo, data_devolucao)
VALUES (1, 'Aline Silva', CURRENT_DATE, CURRENT_DATE + INTERVAL '15 days');

-- Passo 3: Confirmar permanentemente
COMMIT;
\\\

#### Controle Parcial com \SAVEPOINT\
\\\sql
BEGIN;

INSERT INTO autores (nome_autor, nacionalidade) 
VALUES ('Carlos Drummond', 'Brasileiro');

-- Cria um ponto intermediário de salvamento
SAVEPOINT autor_inserido;

-- Operação com erro proposital (ID inexistente 9999)
INSERT INTO livros (titulo, id_autor, ano_publicacao) 
VALUES ('Poesia', 9999, 1930);

-- Desfaz apenas o comando defeituoso mantendo o autor gravado!
ROLLBACK TO SAVEPOINT autor_inserido;

-- Inserção correta
INSERT INTO livros (titulo, id_autor, ano_publicacao) 
VALUES ('Alguma Poesia', 1, 1930);

COMMIT;
\\\

---

## SEMANA 5: Seminário Comparativo dos Principais SGBDs Relacionais

| SGBD | Licença | Destaques Arquiteturais | Melhor Cenário de Uso | Linguagem Procedural |
| :--- | :--- | :--- | :--- | :--- |
| 🐘 **PostgreSQL** | Open-Source Livre *(PostgreSQL License)* | SGBD open-source mais avançado, suporte a JSONB/NoSQL híbrido, tipos geométricos (*PostGIS*), conformidade estrita ao padrão ACID. | Aplicações corporativas complexas, fintechs, APIs REST e geolocalização. | **PL/pgSQL** |
| 🐬 **MySQL** | Dual *(GPL / Comercial Oracle)* | O motor mais difundido na Web. Altamente otimizado para operações de leitura rápida (*Read-heavy*), pilha LAMP. | WordPress, e-commerces, portais de conteúdo e plataformas CMS. | **SQL/PSM** |
| 🏢 **Oracle Database** | Proprietária Comercial Enterprise | Padrão da indústria para ambientes bancários e missão crítica. Alta performance, clusters RAC e replicação Data Guard. | Grandes corporações bancárias, telecomunicações e governos. | **PL/SQL** |
| 🪟 **SQL Server** | Proprietária Comercial Microsoft | Integração nativa profunda com Windows Server, ecossistema .NET (C#), nuvem Azure e suíte integrada de BI (*SSIS, SSAS, Power BI*). | Ambientes integrados ao ecossistema Microsoft e ERPs corporativos. | **T-SQL** |
| 🪶 **SQLite** | Domínio Público *(100% Livre)* | **Serverless (Sem Servidor)!** O banco é um arquivo \.db\ único no disco, embutido no processo da aplicação, sem portas de rede. | Aplicativos Mobile (Android/iOS), navegadores (Chrome), IoT e apps desktop. | *Não possui* |
| 🦭 **MariaDB** | 100% Open-Source *(GPL v2)* | Fork independente do MySQL criado pela equipe original para garantir liberdade contínua. 100% compatível com drivers MySQL. | Servidores Linux modernos (Debian/CentOS) e infraestruturas em nuvem abertas. | **SQL/PSM** |

---

## SEMANA 6: Resumo Estratégico, Mapa Mental e Pegadinhas Clássicas

### 6.1 Tabela de Bolso dos 5 Subgrupos SQL

| Subgrupo | Ação no Banco | Comandos Chave | Objeto Alvo |
| :--- | :--- | :--- | :--- |
| **DDL** | Definir Estrutura | \CREATE\, \ALTER\, \DROP\, \TRUNCATE\, \RENAME\ | Tabelas, Colunas, Índices, Esquemas |
| **DML** | Manipular Dados | \INSERT\, \UPDATE\, \DELETE\, \MERGE\ | Linhas / Registros |
| **DQL** | Consultar | \SELECT\ | Visualização / Leitura |
| **DCL** | Controlar Permissões | \GRANT\, \REVOKE\, \DENY\ | Usuários, Perfis, Acessos |
| **TCL** | Controlar Transações | \BEGIN\, \COMMIT\, \ROLLBACK\, \SAVEPOINT\ | Blocos de Operações ACID |

---

### 6.2 As 6 Maiores Pegadinhas de Prova sobre SGBD

1. ⚠️ **\TRUNCATE\ vs \DELETE\:**  
   O \DELETE\ é **DML** (apaga linha a linha e registra no log transacional). O \TRUNCATE\ é **DDL** (desaloca blocos inteiros no disco e reseta o auto-incremento da PK).
2. ⚠️ **Chave Primária e Valores Nulos:**  
   Uma Chave Primária (PK) **NUNCA** aceita valor \NULL\. A restrição \UNIQUE\ aceita nulos, mas a \PRIMARY KEY\ é formalmente a união de \UNIQUE + NOT NULL\.
3. ⚠️ **O papel do \ROLLBACK\:**  
   O comando \ROLLBACK\ **só pode** desfazer operações que estão dentro de uma transação aberta (\BEGIN\) e que **ainda não** receberam o \COMMIT\. Após o commit, a Durabilidade impede a reversão automática.
4. ⚠️ **Ordem de Inserção vs. Ordem de Exclusão:**  
   * **Para Inserir:** Insere-se primeiro a tabela Pai (\utores\) e depois a tabela Filho (\livros\).  
   * **Para Excluir com RESTRICT:** Exclui-se primeiro os registros Filhos (\livros\) e só depois o Pai (\utores\)!
5. ⚠️ **\WHERE\ no \UPDATE\:**  
   Esquecer o \WHERE\ no comando \UPDATE\ **não gera erro de sintaxe**. O SGBD executará com sucesso a alteração em 100% das linhas da tabela!
6. ⚠️ **SQLite não utiliza arquitetura Cliente-Servidor:**  
   O SQLite não roda como um serviço em segundo plano escutando portas TCP de rede. A própria biblioteca do aplicativo lê e escreve no arquivo \.db\ diretamente no disco.

---

## SEMANA 7: Bateria de 15 Questões de Fixação com Gabarito Comentado

#### Questão 01 • Conceitos Fundamentais *(Nível: Básico)*
**Qual das alternativas a seguir expressa a diferença correta entre "Dado" e "Informação"?**  
a) Dados são gerados apenas por relatórios e Informações são números brutos sem formatação.  
b) Dado é um elemento bruto e sem contexto; Informação é o dado processado e dotado de significado.  
c) Não há distinção entre os dois conceitos no estudo de Engenharia de Software.  
d) Dados existem exclusivamente em bancos NoSQL e Informações em bancos relacionais.  
> **Gabarito: B** — O dado é o fato cru isolado (ex.: "38.5"\). A informação é o dado processado com contexto útil (ex.: *"O paciente está com 38.5°C de febre"*).

---

#### Questão 02 • Modelos Históricos *(Nível: Teórico)*
**Qual era a principal limitação arquitetural do Modelo de Banco de Dados Hierárquico (década de 1960)?**  
a) Não aceitava armazenamento de números inteiros.  
b) Estrutura em árvore rígida onde cada registro filho podia ter estritamente um único registro pai, dificultando relações N:N.  
c) Ausência de suporte à linguagem Java.  
d) Exigência mandatória de conexões TCP/IP em nuvem.  
> **Gabarito: B** — A rigidez da árvore no modelo hierárquico impedia múltiplos pais para um mesmo filho, problema resolvido pelo modelo em rede e aprimorado no modelo relacional.

---

#### Questão 03 • Propriedades ACID (Atomicidade) *(Nível: Fundamental)*
**Em uma transferência financeira entre contas, o valor foi debitado da conta de origem, mas antes de creditar na conta de destino o servidor reiniciou. Qual propriedade ACID obriga o SGBD a desfazer o débito (Rollback)?**  
a) Durabilidade.  
b) Atomicidade.  
c) Isolamento.  
d) Flexibilidade.  
> **Gabarito: B** — A Atomicidade segue o princípio do "tudo ou nada": se qualquer etapa intermediária falha, todas as operações anteriores da transação são desfeitas.

---

#### Questão 04 • Propriedades ACID (Durabilidade) *(Nível: Fundamental)*
**Após a execução com êxito de um comando COMMIT, o servidor de banco de dados sofreu uma pane elétrica. Ao reiniciar, o que garante a permanência dos dados gravados?**  
a) A propriedade de Durabilidade, que assegura a persistência dos dados confirmados no log transacional (WAL).  
b) A camada de apresentação do navegador.  
c) O comando DROP TABLE executado em background.  
d) A restrição de integridade UNIQUE.  
> **Gabarito: A** — A Durabilidade garante que, uma vez emitido o \COMMIT\, os dados tornam-se definitivos e sobrevivem a reinicializações e quedas de energia.

---

#### Questão 05 • Classificação de Subgrupos SQL *(Nível: Básico)*
**Assinale a alternativa que relaciona corretamente os comandos \CREATE TABLE\, \INSERT INTO\, \SELECT\, \GRANT\ e \COMMIT\ aos seus respectivos subgrupos:**  
a) DML, DDL, DQL, TCL, DCL.  
b) DDL, DML, DQL, DCL, TCL.  
c) DDL, DQL, DML, TCL, DCL.  
d) DQL, DML, DDL, DCL, TCL.  
> **Gabarito: B** — \CREATE\ é DDL (estrutura), \INSERT\ é DML (manipulação), \SELECT\ é DQL (consulta), \GRANT\ é DCL (permissão) e \COMMIT\ é TCL (transação).

---

#### Questão 06 • Subgrupos SQL (Pegadinha DDL vs DML) *(Nível: Pegadinha)*
**Qual dos seguintes comandos NÃO pertence ao subgrupo DDL (Data Definition Language)?**  
a) ALTER TABLE  
b) TRUNCATE TABLE  
c) UPDATE  
d) DROP TABLE  
> **Gabarito: C** — \UPDATE\ pertence ao subgrupo DML, pois manipula os valores das linhas sem alterar o esquema estrutural da tabela.

---

#### Questão 07 • Chave Primária (PRIMARY KEY) *(Nível: Básico)*
**Em relação às regras que regem uma Chave Primária (PK) em bancos relacionais, é correto afirmar:**  
a) Pode aceitar valores duplicados caso a coluna seja do tipo texto.  
b) Deve conter valores estritamente únicos e nunca aceita valor nulo (NOT NULL).  
c) Uma tabela pode conter até quatro chaves primárias independentes.  
d) É utilizada apenas para fins estéticos no diagrama relacional.  
> **Gabarito: B** — A Chave Primária identifica com exclusividade cada registro da tabela, sendo obrigatoriamente única e \NOT NULL\.

---

#### Questão 08 • Integridade Referencial (FK com RESTRICT) *(Nível: Prático)*
**Ao tentar rodar \DELETE FROM autores WHERE id_autor = 1;\, o PostgreSQL disparou um erro de violação de Foreign Key. Qual é o motivo desse bloqueio?**  
a) O autor de ID 1 não existe no banco.  
b) Existem livros na tabela livros apontando para esse autor e a FK foi configurada com ON DELETE RESTRICT.  
c) O comando DELETE exige que a senha de administrador seja enviada na query.  
d) Faltou utilizar a cláusula GROUP BY no final do comando.  
> **Gabarito: B** — A regra \RESTRICT\ impede a exclusão do registro pai enquanto houver dependentes vinculados a ele, protegendo a integridade referencial.

---

#### Questão 09 • Ações Referenciais (ON DELETE CASCADE) *(Nível: Intermediário)*
**Caso a Foreign Key da tabela \livros\ tivesse sido configurada com \ON DELETE CASCADE\, o que ocorreria ao apagar o autor de ID 1?**  
a) O autor seria removido e todos os livros daquele autor seriam automaticamente excluídos juntos.  
b) Apenas o autor seria excluído, deixando os livros apontando para um autor inexistente.  
c) O SGBD enviaria um email de confirmação ao administrador antes de executar.  
d) O campo id_autor na tabela de livros seria preenchido com zero.  
> **Gabarito: A** — O \CASCADE\ propaga a ação em cascata: excluir o registro pai remove automaticamente todos os registros filhos correspondentes.

---

#### Questão 10 • Sintaxe DML (UPDATE) *(Nível: Prático)*
**Qual comando SQL abaixo altera corretamente a quantidade disponível para 10 do livro cujo \id_livro\ é 3?**  
a) \ALTER livros SET quantidade_disponivel = 10 WHERE id_livro = 3;\  
b) \UPDATE livros SET quantidade_disponivel = 10 WHERE id_livro = 3;\  
c) \MODIFY livros SET quantidade_disponivel = 10;\  
d) \INSERT INTO livros (quantidade_disponivel) VALUES (10);\  
> **Gabarito: B** — A sintaxe padrão do DML é \UPDATE nome_tabela SET coluna = novo_valor WHERE condicao;\.

---

#### Questão 11 • Controle de Transações (SAVEPOINT) *(Nível: Avançado)*
**Qual é o propósito fundamental do comando \SAVEPOINT ponto_a;\ em um bloco transacional SQL?**  
a) Concluir a transação e desconectar o usuário do banco.  
b) Criar um marcador intermediário para permitir o cancelamento parcial de erros com ROLLBACK TO SAVEPOINT sem abortar a transação inteira.  
c) Fazer um backup criptografado em nuvem.  
d) Alterar a senha do superusuário do banco de dados.  
> **Gabarito: B** — O \SAVEPOINT\ cria marcos parciais que permitem desfazer apenas etapas defeituosas, preservando as operações válidas anteriores.

---

#### Questão 12 • Componentes Internos do SGBD *(Nível: Teórico)*
**Qual componente interno do SGBD é responsável por manter páginas de tabelas e índices em memória RAM para otimizar o tempo de acesso?**  
a) Lock Manager (Gerenciador de Bloqueios).  
b) Buffer Manager (Gerenciador de Buffer / Buffer Pool).  
c) Parser Sintático.  
d) Driver de Rede TCP.  
> **Gabarito: B** — O *Buffer Manager* gerencia o cache em memória RAM, minimizando os acessos lentos de I/O em disco.

---

#### Questão 13 • Panorama dos SGBDs (SQLite) *(Nível: Prático)*
**Um engenheiro de software precisa desenvolver um aplicativo mobile offline para Android e iOS. Qual SGBD relacional é a escolha padrão da indústria por ser serverless e embutido?**  
a) Oracle Database RAC.  
b) Microsoft SQL Server Enterprise.  
c) SQLite.  
d) Apache Cassandra.  
> **Gabarito: C** — O SQLite é *serverless*, extremamente leve e roda embutido no próprio processo da aplicação, sendo nativo no Android, iOS e navegadores web.

---

#### Questão 14 • Recursos Avançados do PostgreSQL (RETURNING) *(Nível: Avançado)*
**Qual cláusula SQL do PostgreSQL permite retornar imediatamente o ID gerado automaticamente por um INSERT sem precisar fazer um novo SELECT?**  
a) OUTPUT TO  
b) RETURNING  
c) LAST_INSERT_ID  
d) FETCH GENERATED  
> **Gabarito: B** — A cláusula \RETURNING id_livro;\ devolve os valores recém-gerados na mesma viagem de rede (*round-trip*).

---

#### Questão 15 • Níveis de Isolamento e Concorrência *(Nível: Avançado)*
**O fenômeno no qual uma transação lê dados modificados por outra transação que ainda NÃO efetuou o COMMIT (e que poderá ser cancelada com ROLLBACK) é denominado:**  
a) Leitura Fantasma (*Phantom Read*).  
b) Leitura Suja (*Dirty Read*).  
c) Leitura Não-Repetível (*Non-Repeatable Read*).  
d) Deadlock Serial.  
> **Gabarito: B** — *Leitura Suja (Dirty Read)* ocorre ao ler dados não confirmados (*uncommitted*), sendo prevenida a partir do nível de isolamento *Read Committed*.

