-- Tabela CLIENTES
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(150) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    bairro VARCHAR(100),
    rua VARCHAR(100),
    numero VARCHAR(10),
    complemento VARCHAR(100),
    uf CHAR(2),
    cidade VARCHAR(100),
    cep VARCHAR(10)
);

-- Tabela PRODUTOS
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    categoria VARCHAR(50),
    quantidade INT DEFAULT 0,
    imagem VARCHAR(255)
);
CREATE TABLE carrinho (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_email VARCHAR(100) NOT NULL,
  produto_id INT NOT NULL,
  quantidade INT DEFAULT 1,
  tamanho VARCHAR(10)
);
CREATE TABLE pedidos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_email VARCHAR(100),
  cliente_nome VARCHAR(100),
  produto_nome VARCHAR(100),
  tamanho VARCHAR(10),
  quantidade INT,
  data_pedido DATE,
  endereco_bairro VARCHAR(100),
  endereco_rua VARCHAR(100),
  endereco_numero VARCHAR(10),
  endereco_cidade VARCHAR(100),
  endereco_uf VARCHAR(5),
  forma_pagamento VARCHAR(20),
  status VARCHAR(20)
);
CREATE TABLE solicitacoes_devolucao (
  id INT AUTO_INCREMENT PRIMARY KEY,
  pedido_id INT NOT NULL,
  email VARCHAR(255) NOT NULL,
  data_solicitacao DATE NOT NULL,
  motivo VARCHAR(255),
  descricao TEXT,
  acao VARCHAR(50),
  foto VARCHAR(255)
);
