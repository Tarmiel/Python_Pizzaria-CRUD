    create database erp;
     
    create table cadastros(
    nome varchar(50) not null,
    senha varchar(20) not null,
    nivel int not null
     
    );
     
    insert into cadastros values ('admin', 'admin', 2);
     
    create table produtos(
    id int auto_increment not null primary key,
    nome varchar(100) not null,
    ingredientes varchar(1000),
    grupo varchar(100),
    preco float
     
    );
     
    create table pedidos(
    id int not null primary key auto_increment,
    nome varchar(100) not null,
    ingredientes varchar(1000),
    grupo varchar(100),
    localEntrega varchar(500),
    observacoes varchar(1000),
    dataPedido varchar(20) not null,
    vendedor varchar(30) not null
     
    );
    insert into produtos(nome,ingredientes,grupo,preco) values ('coca','','bebidas',6);
    insert into produtos(nome,ingredientes,grupo,preco) values ('pizza de mussarela','mussarela','pizzas',34.9);
    insert into produtos(nome,ingredientes,grupo,preco) values ('pizza de portuguesa','mussarela','pizzas',34.9);
    insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes,dataPedido,vendedor) values ('pizza de mussarela', 'mussarela', 'pizzas', '', 'sem cebola','01-2020','admin');
    insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes,dataPedido,vendedor) values ('coca', '', 'bebidas', '', '','01-2020','admin');

     
    create table estatisticaVendido(
    id int not null primary key auto_increment,
    nome varchar(100) not null,
    grupo varchar(100),
    preco float,
    vendedor varchar(30) not null
    );
     
    insert into estatisticaVendido(nome, grupo, preco,vendedor) values ('pizza de mussarela', 'pizzas', 34.90,'admin');
     
    insert into estatisticaVendido(nome, grupo, preco,vendedor) values ('coca', 'bebidas', 6,'admin');
     
    insert into estatisticaVendido(nome, grupo, preco,vendedor) values ('pizza de portuguesa', 'pizzas', 34.90,'admin');
     
    insert into estatisticaVendido(nome, grupo, preco,vendedor) values ('suco de laranja', 'pizzas', 7,'admin');
