-- ====================================================================
-- PROJETO DE BANCO DE DADOS: BIBLIOTECA UNIVERSITÁRIA
-- SGBD: PostgreSQL
-- Disciplina: Sistemas Gerenciadores de Banco de Dados (Engenharia de Software)
-- ====================================================================

-- 1. CRIAÇÃO DO BANCO DE DADOS
-- CREATE DATABASE biblioteca_universitaria;
-- \c biblioteca_universitaria;

-- ====================================================================
-- 2. DDL - DEFINIÇÃO DE ESTRUTURA (TABELAS E CONSTRAINTS)
-- ====================================================================

-- Tabela 1: Categorias (Classificação temática)
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria SERIAL PRIMARY KEY,
    nome_categoria VARCHAR(100) NOT NULL UNIQUE,
    descricao TEXT
);

-- Tabela 2: Autores (Tabela Pai)
CREATE TABLE IF NOT EXISTS autores (
    id_autor SERIAL PRIMARY KEY,
    nome_autor VARCHAR(150) NOT NULL,
    nacionalidade VARCHAR(80),
    data_nascimento DATE
);

-- Tabela 3: Livros (Tabela Filha de Autores)
CREATE TABLE IF NOT EXISTS livros (
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

-- Tabela 4: Transações de Empréstimo (Tabela Filha de Livros)
CREATE TABLE IF NOT EXISTS transacoes_emprestimo (
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

-- ====================================================================
-- 3. DML - INSERÇÃO DE DADOS (POPULAÇÃO INICIAL)
-- ====================================================================

-- Inserção de categorias
INSERT INTO categorias (nome_categoria, descricao)
VALUES 
    ('Ficção Científica', 'Livros de exploração espacial e tecnologia futura'),
    ('Literatura Brasileira', 'Grandes clássicos e romances nacionais'),
    ('Engenharia e Computação', 'Livros acadêmicos e técnicos de tecnologia');

-- Inserção em lote de autores (alta eficiência)
INSERT INTO autores (nome_autor, nacionalidade, data_nascimento)
VALUES
    ('Machado de Assis', 'Brasileiro', '1839-06-21'),
    ('Clarice Lispector', 'Brasileira', '1920-12-10'),
    ('Jorge Amado', 'Brasileiro', '1912-08-10');

-- Inserção com RETURNING para capturar imediatamente a PK gerada
INSERT INTO livros (titulo, id_autor, ano_publicacao, quantidade_disponivel)
VALUES ('Dom Casmurro', 1, 1899, 5)
RETURNING id_livro, titulo;

INSERT INTO livros (titulo, id_autor, ano_publicacao, quantidade_disponivel)
VALUES 
    ('A Hora da Estrela', 2, 1977, 3),
    ('Capitães da Areia', 3, 1937, 4);

-- ====================================================================
-- 4. DML - ATUALIZAÇÕES E EXCLUSÕES SEGURAS
-- ====================================================================

-- Atualização condicional segura com WHERE
UPDATE livros
SET quantidade_disponivel = 7, ano_publicacao = 1900
WHERE id_livro = 1;

-- Ordem correta de exclusão respeitando o ON DELETE RESTRICT:
-- 1º) Excluir registros dependentes em transacoes_emprestimo
-- 2º) Excluir livros
-- 3º) Excluir autor

-- ====================================================================
-- 5. TCL - TRANSAÇÕES ACID E CONTROLE DE FLUXO
-- ====================================================================

-- Transação de Empréstimo Atômica (Tudo ou Nada)
BEGIN;

-- Passo 1: Decrementar a quantidade do livro no estoque
UPDATE livros
SET quantidade_disponivel = quantidade_disponivel - 1
WHERE id_livro = 1 AND quantidade_disponivel > 0;

-- Passo 2: Registrar a movimentação de empréstimo para a aluna
INSERT INTO transacoes_emprestimo (id_livro, nome_aluno, data_emprestimo, data_devolucao)
VALUES (1, 'Aline Silva', CURRENT_DATE, CURRENT_DATE + INTERVAL '15 days');

-- Passo 3: Confirmar permanentemente (salvo no Write-Ahead Log)
COMMIT;

-- Transação com SAVEPOINT (Recuperação parcial de erros)
BEGIN;

INSERT INTO autores (nome_autor, nacionalidade) 
VALUES ('Carlos Drummond', 'Brasileiro');

-- Ponto de recuperação
SAVEPOINT autor_inserido;

-- Simulação de tentativa com erro (ID inexistente: 9999)
-- INSERT INTO livros (titulo, id_autor, ano_publicacao) VALUES ('Poesia', 9999, 1930);

-- Caso ocorra falha:
-- ROLLBACK TO SAVEPOINT autor_inserido;

-- Inserção com ID correto (id_autor = 1):
INSERT INTO livros (titulo, id_autor, ano_publicacao, quantidade_disponivel) 
VALUES ('Alguma Poesia', 1, 1930, 2);

COMMIT;

-- ====================================================================
-- 6. DQL - CONSULTAS
-- ====================================================================

-- Listagem de livros e seus respectivos autores
SELECT 
    l.id_livro,
    l.titulo,
    a.nome_autor,
    l.ano_publicacao,
    l.quantidade_disponivel
FROM livros l
INNER JOIN autores a ON l.id_autor = a.id_autor
ORDER BY l.titulo ASC;
