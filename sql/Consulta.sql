-- SQL - Consulta para obter o total de compra por cliente

SELECT 
    c.nome,
    COUNT(p.id_compra) AS total_compras,
    SUM(pr.preco) AS total_gasto
FROM 
    lab.clientes c
JOIN 
    lab.compras p ON c.id_cliente = p.id_cliente
JOIN 
    lab.produtos pr ON p.id_produto = pr.id_produto
GROUP BY 
    c.nome;