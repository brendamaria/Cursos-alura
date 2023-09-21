-- inserir dados 
INSERT INTO PRODUTOS VALUES ('1040107', 'Light - 350ml - Melancia', 'Lata', '350ml', 'Melancia', 4.56);

--inserir dados multiplos
INSERT INTO PRODUTOS VALUES 
('1037797', 'Clean 2 Litros Laranja', 'PET', '2 Litros', 'Laranja', 16.01),
('1000889', 'Sabor da Montanha 700 ml Uva', 'Garrafa', '700 ml', 'Uva', 6.31),
('1004327', 'Videira do Campo - 1,5 Litros Melancia', 'PET', '1,5 Litros', 'Melancia', 19.51),
('1088126', 'Linha Citrus 1 Litro Limão', 'PET', '1 Litro', 'Limão', 7.00);


INSERT INTO CLIENTES VALUES
('00384393431','João da Silva', 'Rua Projetada A', 'Numero 233', 'Copacabana', 'RJ', '20000000', '1965-03-21', 57, 'M', 200000, 3000.30, 1),
('00384393555', 'Maria Clara', 'Rua Projetada A', 'Numero 233', 'Copacabane', 'RJ', '20000000', '1975-03-21', 47, 'F', 200000, 3000.30, 0);


--Desafio: incluindo vendedores
INSERT INTO VENDEDORES VALUES
('00236', 'Cláudia Morais', 0.08),
('00237', 'Macela Ferreira', 0.09),
('00238', 'Márcio Almeida', 0.08);


--INSERIR FORA DE ORDEM
INSERT INTO PRODUTOS (CODIGO_PRODUTO, NOME_PRODUTO, EMBALAGEM, TAMANHO, PRECO_LISTA, SABOR) VALUES
('5449310', 'Frescor do Verão - 350 ml - Limão', 'Lata', '350 ml', 2.45, 'Limão'),
('1078680', 'Frescor do Verão - 350 ml - Manga', 'Lata', '350 ml', 3.18, 'Manga');