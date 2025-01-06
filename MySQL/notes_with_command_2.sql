SELECT * FROM employees.employees WHERE first_name = 'Denis';

select * from employees.employees where first_name = 'Elvis';

SELECT * FROM employees.employees WHERE first_name = 'Denis' AND gender = 'M';

SELECT * FROM employees.employees WHERE first_name = 'Kellie' AND gender = 'F';

SELECT * FROM employees.employees WHERE first_name = 'Denis' OR first_name = 'Elvis';

SELECT * FROM employees.employees WHERE first_name = 'Kellie' OR 'Aruna';

SELECT * FROM employees.employees WHERE last_name = 'Denis' AND (gender = 'M' OR gender = 'F');

SELECT * FROM employees.employees WHERE gender = 'F' AND (first_name = 'Kellie' OR 'Aruna');

SELECT * FROM employees.employees WHERE first_name = 'Cathie' OR 'Mark' OR 'Nathan';

SELECT * FROM employees.employees WHERE first_name IN ('Cathie', 'Mark', 'Nathan');

SELECT * FROM employees.employees WHERE first_name NOT IN ('Cathie', 'Mark', 'Nathan');

SELECT * FROM employees.employees WHERE first_name IN ('Denis', 'Elvis');

SELECT * FROM employees.employees WHERE first_name NOT IN ('John', 'Mark', 'Jacob');


SELECT * FROM employees.employees WHERE first_name LIKE('Mar%');
/*
 % All second part of word
 */

SELECT * FROM employees.employees WHERE first_name LIKE('%ar%');

SELECT * FROM employees.employees WHERE first_name LIKE ('Mar_');
/*
 _ The skipped letter in word
 */

SELECT * FROM employees.employees WHERE first_name NOT LIKE ('mar%');
SELECT * FROM employees.employees WHERE first_name NOT LIKE ('%ar%');

SELECT * FROM employees.employees WHERE first_name LIKE ('Jack');
SELECT * FROM employees.employees WHERE first_name NOT LIKE ('Jack');

SELECT * FROM employees.employees WHERE hire_date NOT BETWEEN '1990-01-01' AND '2000-01-01';
SELECT * FROM employees.employees WHERE hire_date BETWEEN '1990-01-01' AND '2000-01-01';

SELECT * FROM employees.salaries WHERE salary BETWEEN '66,000' AND '70,000';

SELECT * FROM employees.employees WHERE emp_no NOT BETWEEN '10004' AND '10012';
SELECT * FROM employees.departments WHERE dept_name BETWEEN 'd003' AND 'd006';

SELECT * FROM employees.employees WHERE first_name IS NULL;
SELECT * FROM employees.employees WHERE first_name IS NOT NULL;

SELECT * FROM employees.departments WHERE dept_name IS NOT NULL;

SELECT * FROM employees.employees WHERE first_name = 'Mark';
SELECT * FROM employees.employees WHERE first_name != 'Mark';

SELECT * FROM employees.employees WHERE hire_date >= '2000-01-01';
SELECT * FROM employees.employees WHERE hire_date <= '2000-01-01';

SELECT * FROM employees.employees WHERE hire_date <= '1985-02-01';
SELECT * FROM employees.employees WHERE hire_date >= '1985-02-01';

SELECT * FROM employees.employees WHERE gender = 'F' AND hire_date >= '2000-01-01';

SELECT gender FROM employees.employees;

SELECT COUNT(emp_no) FROM employees;

SELECT * FROM employees.employees WHERE first_name IS NULL;

SELECT COUNT(DISTINCT first_name) FROM employees.employees;

SELECT COUNT(salary) FROM employees.salaries;

SELECT COUNT(DISTINCT first_name) FROM employees.employees;

SELECT * FROM employees.employees ORDER BY first_name;

SELECT * FROM employees.employees ORDER BY first_name, last_name ASC;
SELECT * FROM employees.employees ORDER BY first_name, last_name DESC;

SELECT * FROM employees.employees ORDER BY hire_date DESC;

SELECT first_name FROM employees.employees GROUP BY first_name;
SELECT DISTINCT first_name FROM employees.employees;

SELECT first_name, COUNT(first_name)
FROM employees.employees GROUP BY first_name ORDER BY first_name DESC;

SELECT first_name, COUNT(first_name) AS names_count
FROM employees.employees GROUP BY first_name ORDER BY first_name DESC;
/*
 AS Aliases
 */
SELECT * FROM employees.employees HAVING hire_date >= '2000-01-01';

SELECT first_name, COUNT(first_name) as names_count
FROM employees.employees GROUP BY first_name HAVING COUNT(first_name) > 250
ORDER BY first_name;

select first_name, count(first_name) as names_count
from employees.employees where hire_date < '1999-01-01'
group by first_name having count(first_name) < 200
order by first_name desc;

select * from employees.salaries order by salary desc limit 10;
select first_name from employees.employees order by first_name desc limit 5;

select first_name, count(first_name) as names_count from employees.employees
where hire_date > '1999-01-01' group by first_name having count(first_name) < 200
order by first_name desc limit 100;

select emp_no from employees.dept_emp order by emp_no desc limit 100;