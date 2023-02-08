CREATE DATABASE IF NOT EXISTS solution;
USE solution;

CREATE TABLE IF NOT EXISTS products (
    id INT(11) AUTO_INCREMENT,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    PRIMARY KEY (id)
);

INSERT INTO products VALUE(0, 'Capacete para galinha', 45);
INSERT INTO products VALUE(0, 'Papel higiênico com estampa de dólar', 20);
INSERT INTO products VALUE(0, 'Chaveiro de bacon', 15);
INSERT INTO products VALUE(0, 'Chifres de carneiro', 70);
INSERT INTO products VALUE(0, 'Bolsa de silicone para amassar pão', 30);
INSERT INTO products VALUE(0, 'Xícara de café comestível', 25)