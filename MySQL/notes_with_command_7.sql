SELECT dm.dept_no, dm.emp_no, s.salary FROM dept_manager dm JOIN salaries s ON dm.emp_no = s.emp_no;

# SELECT s.salary FROM dept_manager dm JOIN salaries s ON dm.emp_no = s.emp_no
#
# UPDATE (SELECT s.salary FROM dept_manager dm JOIN salaries s ON dm.emp_no = s.emp_no)
# SET salary = salary + salary * 0.15;

UPDATE salaries s JOIN dept_manager dm ON dm.emp_no = s.emp_no
SET s.salary = s.salary + s.salary * 0.15;


SELECT dm.dept_no, dm.emp_no, s.salary
FROM dept_manager dm JOIN salaries s ON dm.emp_no = s.emp_no;

SELECT * FROM dept_manager;
SELECT * FROM departments;

SELECT dm.dept_no, d.dept_name
FROM dept_manager dm
         JOIN departments d on dm.dept_no = d.dept_no;
SELECT d.dept_name, e.*
FROM departments d
         JOIN employees e on d.dept_no = e.emp_no;


-- Course

SELECT * FROM dept_manager;

SELECT e.first_name, e.last_name FROM employees e
WHERE e.emp_no IN (SELECT dm.emp_no FROM dept_manager dm);

SELECT dm.emp_no FROM dept_manager dm;

SELECT e.first_name, e.last_name FROM employees e
WHERE EXISTS(SELECT * FROM dept_manager dm WHERE dm.emp_no = e.emp_no);

SELECT e.first_name, e.last_name FROM employees e
WHERE EXISTS(SELECT * FROM dept_manager dm
WHERE dm.emp_no = e.emp_no ORDER BY emp_no);

INSERT INTO titles(emp_no, title, from_date, to_date)
SELECT de.emp_no, 'Assistant Engineer', NOW(), NOW()
FROM departments d
JOIN dept_emp de ON d.dept_no = de.dept_no
WHERE dept_name = 'Development'
LIMIT 50;

SELECT e.first_name, e.last_name
FROM employees e
WHERE NOT EXISTS(SELECT *
             FROM titles t
             WHERE title = 'Assistant Engineer'
               AND e.emp_no = t.emp_no);

SELECT * FROM employees;

SELECT e.first_name, e.last_name
FROM employees e
WHERE e.emp_no NOT IN (SELECT t.emp_no
                   FROM titles t
                   WHERE title = 'Assistant Engineer');

SELECT emp_no FROM dept_manager WHERE emp_no = 110022;

SELECT A.*
FROM
(SELECT e.emp_no as employee_ID,
       MIN(de.dept_no) as department_code,
    (SELECT emp_no
     FROM dept_manager
     WHERE emp_no = 110022) AS manager_ID
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
WHERE e.emp_no <= 10020
GROUP BY e.emp_no
ORDER BY e.emp_no) AS A
UNION
SELECT B.*
FROM
(SELECT e.emp_no as employee_ID,
       MIN(de.dept_no) as department_code,
    (SELECT emp_no
     FROM dept_manager
     WHERE emp_no = 110039) AS manager_ID
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
WHERE e.emp_no <= 10020
GROUP BY e.emp_no
ORDER BY e.emp_no) AS B;

SELECT *
FROM dept_emp;

SELECT emp_no, from_date, to_date, COUNT(emp_no) AS Num
FROM dept_emp
GROUP BY emp_no
HAVING Num > 1;

CREATE OR REPLACE VIEW v_dept_emp_latest_date AS
SELECT
    emp_no, MAX(from_date) as from_date, MAX(to_date) as to_date
FROM
    dept_emp
GROUP BY emp_no;
SELECT
    emp_no, MAX(from_date) as from_date, MAX(to_date) as to_date
FROM
    dept_emp
GROUP BY emp_no;

SELECT * FROM employees.v_dept_emp_latest_date;