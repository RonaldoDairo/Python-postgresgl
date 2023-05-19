CREATE TABLE students(id Serial, name text, address text, age int);

INSERT INTO students(name, address, age) VALUES
    ('John', 'New York', 35);
INSERT INTO students(name, address, age) VALUES
    ('Mary', 'London', 45);

select * from students;