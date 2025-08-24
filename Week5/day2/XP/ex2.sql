--CREATE TABLE Students

CREATE TABLE Students(
id SERIAL,
last_name VARCHAR(100)  NOT NULL,
first_name VARCHAR(50) NOT NULL,
birth_date DATE NOT NULL

);

--INSERT DATA INTO THE TABLE

INSERT INTO Students(first_name,last_name,birth_date)
VALUES('Renata','Kac','03/02/1984')
VALUES('Marc','Benichou','02/11/1998'),
('Yoan','Cohen','03/12/2010'),
('Lea','Benichou','27/07/1987'),
('Amelia','Dux','07/04/1996'),
('David','Grez','14/06/2003'),
('Omer','Simpson','03/10/1980');


--INSERT MY DATA INTO THE TABLE

INSERT INTO Students(first_name,last_name,birth_date)
VALUES('Renata','Kac','03/02/1984');


--Fetch all data from table --

SELECT * FROM Students;

--Fetch all of the students first_names and last_names

SELECT 
first_name,
last_name
FROM Students;

--Fetch the student which id is equal to 2


SELECT 
first_name,
last_name
FROM Students WHERE id=2;


--Fetch the student whose last_name is Benichou AND first_name is Marc

SELECT 
first_name,
last_name
FROM Students WHERE last_name='Benichou' AND first_name='Marc';

--Fetch the students whose last_names are Benichou OR first_names are Mar

SELECT 
first_name,
last_name
FROM Students WHERE last_name='Benichou' OR first_name='Marc';

--Fetch the students whose first_names contain the letter a

SELECT 
first_name,
last_name
FROM Students WHERE first_name LIKE '%a%';


--Fetch the students whose first_names starts with the letter a

SELECT 
first_name,
last_name
FROM Students WHERE first_name LIKE 'a%';

--Fetch the students whose first_names ends with the letter a

SELECT 
first_name,
last_name
FROM Students WHERE first_name LIKE '%a';


--Fetch the students whose second to last letter of their first_names are a 

SELECT 
first_name,
last_name
FROM Students WHERE first_name LIKE '_a%';


--Fetch the students whose id’s are equal to 1 AND 3

SELECT 
first_name,
last_name
FROM Students WHERE id IN(1,3);

---Fetch the students whose birth_dates are equal to or come after 1/01/2000

SELECT * FROM Students WHERE birth_date>'1/01/2000';