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
