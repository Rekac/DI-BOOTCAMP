--HOW TO CREATE TABLE

CREATE TABLE actors(
actor_id SERIAL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
Last_name VARCHAR(100)  NOT NULL,
age DATE,
number_oscars SMALLINT

)

---Count how many actors are in the table

SELECT COUNT(first_name) FROM actors;


----Try to add a new actor with some blank fields
--INSERT DATA INTO THE TABLE

INSERT INTO actors(first_name,last_name,age,number_oscars)
VALUES('Robert','DeNiro',1)
---open an ERROR, since the fields when we created the table actors we defined as NOT NULL,is MANDATORY have an info in the field.To correct the error don't include NOT null