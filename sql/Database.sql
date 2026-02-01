-- SQL - Criação do Banco de Dados

-- Deleta o schema se já existir
DROP SCHEMA IF EXISTS lab CASCADE;

-- Cria o schema
CREATE SCHEMA lab AUTHORIZATION dsa;

-- Cria as tabelas

CREATE TABLE lab.clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(101),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lab.produtos (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10, 2)
);

CREATE TABLE lab.compras (
    id_compra SERIAL PRIMARY KEY,
    id_cliente INTEGER REFERENCES lab.clientes(id_cliente),
    id_produto INTEGER REFERENCES lab.produtos(id_produto),
    data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
