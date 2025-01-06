SELECT * FROM salaries ORDER BY salary DESC LIMIT 10;

SELECT COUNT(salary) FROM salaries;

SELECT COUNT(DISTINCT salary) FROM salaries;
-- # DISTINCT the list of rows without duplicates

SELECT COUNT(dept_no) FROM employees.dept_emp;

SELECT SUM(salary) FROM salaries;

SELECT MAX(salary) FROM salaries;

SELECT MIN(salary) FROM salaries;

SELECT MAX(emp_no) FROM employees.employees;
SELECT MIN(emp_no) FROM employees.employees;

SELECT AVG(salary) FROM salaries;

SELECT AVG(emp_no) FROM employees.employees;
SELECT ROUND(AVG(emp_no)) FROM employees.employees;

SELECT ROUND(AVG(emp_no), 2) FROM employees.employees;
-- # ROUND(#, decimal_places)

SELECT * FROM departments_dup ORDER BY dept_no;

SELECT dept_no, IFNULL(dept_name, 'Department name not provided') FROM departments_dup;

-- # SELECT dept_no, dept_name,
-- # COALESCE(dept_manager, dept_name, 'N/A') AS dept_manager
-- # FROM departments_dup ORDER BY dept_no ASC;
-- #
-- # SELECT dept_no, dept_name COALESCE('department manager name') AS fake_col
-- # FROM departments_dup;