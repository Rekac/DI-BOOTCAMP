--- CREATE TABLE items

CREATE TABLE items(
item_id SERIAL,
item VARCHAR(100) NOT NULL,
price_item  NUMERIC(50,0) NOT NULL);


--- CREATE TABLE customers

CREATE TABLE customers(
customer_id SERIAL,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(100) NOT NULL);

--INSERT VALUES ON TABLE ITEMS 

INSERT INTO items(item,price_item)
VALUES('Small Desk',100),
('Large Desk',300),
('Fan',80);

--INSERT VALUES ON TABLE COSTUMERS

INSERT INTO costumers(first_name,last_name)
VALUES('Greg','Jones'),
('Sandra','Jones'),
('Scott','Scott'),
('Trevor','Green'),
('Melanie','Johnson');



---SELECT ALL items

SELECT * FROM items;


--SELECT ALL ITEMS ABOVE PRICE 80

SELECT * FROM items WHERE price_item>80;

--SELECT ALL ITEMS BELOW PRICE 300

SELECT * FROM items WHERE price_item<=300;

---All customers whose last name is ‘Smith’ 

SELECT * FROM costumers WHERE last_name='Smith';

--All customers whose last name is ‘Jones’

SELECT * FROM costumers WHERE last_name='Jones';

---All customers whose firstname is not ‘Scott’

SELECT * FROM costumers WHERE first_name<>'Scott';