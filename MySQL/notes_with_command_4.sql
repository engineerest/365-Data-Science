SELECT * FROM departments_dup ORDER BY dept_no;

USE employees;

SELECT * FROM employees.employees WHERE emp_no = 999901;

UPDATE employees.employees
SET first_name = 'Stella',
    last_name = 'Parkinson',
    birth_date = '1990-12-31',
    gender = 'F'
WHERE
    emp_no = 999903;


SELECT * FROM sales.departments_dup ORDER BY dept_no;

COMMIT;

UPDATE sales.departments_dup
SET
    dept_no = 'd011',
    dept_name = 'Quality Control';


ROLLBACK;

COMMIT;

SELECT * FROM employees.departments;

UPDATE employees.departments
SET
    dept_name = 'Data Analysis'
WHERE dept_name = 'Business Analysis';

COMMIT;

SELECT * FROM employees.employees WHERE emp_no = 999903;

DELETE FROM employees.employees WHERE emp_no = 999903;

SELECT * FROM sales.departments_dup ORDER BY dept_no;

DELETE FROM sales.departments_dup;

COMMIT;