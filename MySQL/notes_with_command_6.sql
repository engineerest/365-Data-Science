
CREATE TABLE IF NOT EXISTS dept_manager_dup
(
    emp_no VARCHAR(10),
    dept_no VARCHAR(10),
    from_date DATE,
    to_date DATE
);

INSERT INTO dept_manager_dup
VALUES ('110228', 'd003', '1992-03-21', '9999-01-01');

INSERT INTO departments_dup
VALUES ('D009', 'Customer Service');

SELECT * FROM dept_manager_dup;

SELECT ed.dept_no, ed.dept_name FROM employees.departments ed
INNER JOIN sales.departments d on ed.dept_name = d.dept_name
ORDER BY ed.dept_no;

SELECT m.dept_no, m.emp_no, d.dept_name
FROM dept_manager m JOIN departments_dup d
ON m.dept_no = d.dept_name ORDER BY dept_no;

# SELECT sd.dept_no, sd.dept_name
# FROM sales.departments sd
# INNER JOIN
# employees.departments ed ON sd.dept_no = ed.dept_no;


DELETE FROM dept_manager_dup
WHERE emp_no = '110228';

DELETE FROM departments_dup
WHERE dept_no = 'd009';

INSERT INTO dept_manager_dup
VALUES ('110228', 'd003', '1992-03-21', '9999-01-01');

INSERT INTO departments_dup
VALUES ('D009', 'Customer Service');

# SELECT m.dept_no, m.emp_no, d.dept_name
# FROM dept_manager_dup m LEFT JOIN
# departments_dup d ON m.dept_no = d.dept_no
# GROUP BY m.emp_no ORDER BY m.dept_no;

SELECT d.dept_no, m.emp_no, d.dept_name FROM
departments_dup d LEFT JOIN dept_manager_dup m
ON m.dept_no = d.dept_no ORDER BY d.dept_no;


SELECT d.dept_no, m.emp_no, d.dept_name FROM
dept_manager_dup m RIGHT JOIN departments_dup d
ON m.dept_no = d.dept_no ORDER BY dept_no;

-- JOIN
SELECT m.dept_no, m.emp_no, d.dept_name FROM
dept_manager_dup m INNER JOIN departments_dup d
ON m.dept_no = d.dept_no ORDER BY m.dept_no;

-- WHERE
SELECT m.dept_no, m.emp_no, d.dept_name FROM
dept_manager_dup m, departments_dup d WHERE
m.dept_no = d.dept_no ORDER BY m.dept_no;

SELECT e.emp_no, e.first_name, e.last_name, s.salary
FROM employees e JOIN salaries s ON e.emp_no = s.emp_no
WHERE s.salary > 145000;



SELECT dm.*, d.* FROM dept_manager dm
CROSS JOIN departments_dup d ORDER BY
dm.emp_no, d.dept_no;

SELECT dm.*, d.* FROM
dept_manager dm, departments d
ORDER BY dm.emp_no, d.dept_no;

SELECT dm.*, d.* FROM dept_manager dm
JOIN departments d ORDER BY dm.emp_no,
d.dept_no;

SELECT dm.*, d.* FROM departments d
CROSS JOIN dept_manager dm WHERE
d.dept_no <> dm.dept_no ORDER BY
dm.emp_no, d.dept_no;


-- SELECT e.emp_no, e.gender, AVG(s.salary) AS average_salary
-- FROM employees e JOIN salaries s ON e.emp_no = s.emp_no
-- GROUP BY gender;

SELECT
    e.first_name,
    e.last_name,
    e.hire_date,
    m.from_date,
    d.dept_name
FROM
    employees e JOIN dept_manager m
    ON e.emp_no = m.emp_no JOIN
    departments d ON m.dept_no = d.dept_no;

SELECT
    d.dept_name, AVG(salary)
FROM
    departments d
    JOIN dept_manager m ON d.dept_no = M.dept_no
    JOIN salaries s ON m.emp_no = s.emp_no
    GROUP BY dept_name
    ORDER BY AVG(salary) DESC;


insert into departments(DEPT_NO, DEPT_NAME)
valuES (1, 'Customer Service'),
       (2, 'Development'),
       (3, 'Finance'),
       (4, 'Human Resources'),
       (5, 'Marketing'),
       (6, 'Production');

SELECT de.dept_no, d.dept_name, COUNT(de.dept_no)
FROM dept_emp de
JOIN departments d ON d.dept_no = de.dept_no
GROUP BY de.dept_no;

INSERT INTO salaries (emp_no, salary, from_date, to_date)
SELECT e.emp_no, 5000, '2024-01-01', '2024-11-25'
FROM employees e LIMIT 1000 OFFSET 2500;

SELECT d.dept_name, SUM(s.salary)
FROM departments d
JOIN dept_emp de on d.dept_no = de.dept_no
JOIN salaries s ON s.emp_no = de.emp_no
GROUP BY d.dept_name
ORDER BY d.dept_name;

DROP TABLE IF EXISTS employees_dup;
CREATE TABLE IF NOT EXISTS employees_dup (
    emp_no int(11),
    birth_data date,
    first_name varchar(14),
    last_name varchar(16),
    gender enum('M', 'F'),
    hire_date date
);

INSERT INTO employees_dup
SELECT e.* FROM employees e LIMIT 20;

SELECT * FROM employees_dup;

SELECT
    e.emp_no,
    e.first_name,
    e.last_name,
    NULL AS dept_no,
    NULL AS from_date
FROM
    employees_dup e
WHERE
    e.emp_no = 10001
UNION ALL SELECT
    NULL AS emp_no,
    NULL AS first_name,
    NULL AS last_name,
    m.dept_no,
    m.from_date
FROM
    dept_manager m;


INSERT INTO dept_manager (emp_no, dept_no, from_date, to_date)
SELECT
    (SELECT e.emp_no FROM employees e JOIN dept_emp de ON de.emp_no = e.emp_no WHERE de.dept_no = d.dept_no LIMIT 1) as emp_no,
    d.dept_no,
    '2024-01-01',
    '2024-11-29'
FROM departments d;


SELECT * FROM employees JOIN employees.dept_emp de on employees.emp_no = de.emp_no
WHERE dept_no = 1;

SELECT * FROM dept_manager;
UPDATE salaries SET salary = salary + 500 WHERE emp_no IN (SELECT emp_no FROM dept_manager);
    JOIN dept_manager dm ON s.emp_no = dm.emp_no;
SELECT * FROM salaries WHERE emp_no NOT IN (SELECT emp_no FROM employees);

SELECT * FROM dept_manager dm WHERE dm.dept_no IN (SELECT d.dept_no FROM departments d);

SELECT de.dept_no, COUNT(de.dept_no), AVG(s.salary)
FROM salaries s
JOIN dept_emp de ON de.emp_no = s.emp_no
GROUP BY de.dept_no;

INSERT INTO salaries(emp_no, salary, from_date, to_date)
SELECT emp_no, 1500, DATE_ADD(NOW(), interval -6 MONTH), DATE_ADD(NOW(), interval 2 DAY)
FROM employees
WHERE emp_no IN (SELECT emp_no FROM dept_emp WHERE dept_no = 2);

SELECT * FROM dept_manager;
