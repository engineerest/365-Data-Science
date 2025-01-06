USE employees;

DROP PROCEDURE IF EXISTS select_employees;

DELIMITER $$
CREATE PROCEDURE select_employees()
BEGIN
    SELECT * FROM employees
        LIMIT 1000;
END $$

DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `select_salaries`()
BEGIN
    SELECT * FROM salaries
    LIMIT 1000;
END $$

DELIMITER ;

DELIMITER $$
CREATE PROCEDURE emp_avg_salary(IN p_emp_no INTEGER)
BEGIN
    SELECT e.first_name, e.last_name, avg(s.salary)
    FROM employees e
    JOIN salaries s ON e.emp_no = s.emp_no
    WHERE e.emp_no = p_emp_no;
END $$

DELIMITER ;

DELIMITER $$
CREATE PROCEDURE emp_avg_salary_out(IN p_emp_no INTEGER, OUT p_avg_salary DECIMAL(10,2))
BEGIN
    SELECT avg(s.salary)
    INTO p_avg_salary
    FROM employees e
    JOIN salaries s ON e.emp_no = s.emp_no
    WHERE e.emp_no = p_emp_no;
END $$

DELIMITER ;

DELIMITER $$
CREATE PROCEDURE emp_info(IN p_first_name VARCHAR(25), p_last_name VARCHAR(25), OUT p_emp_no INTEGER)
BEGIN
    SELECT e.emp_no
    INTO p_emp_no
    FROM employees e
    WHERE e.first_name = p_first_name AND
          e.last_name = p_last_name;

END $$
DELIMITER ;


SET @p_avg_salary = 0;
CALL employees.emp_avg_salary_out(11300, @p_avg_salary);
SELECT @p_avg_salary;

SET @v_avg_salary = 0;
CALL employees.emp_avg_salary_out(11300, @v_avg_salary);
SELECT @v_avg_salary;


CALL emp_salary(1130);
CALL emp_avg_salary(11300);



CALL employees.select_employees();

CALL select_employees();

DROP PROCEDURE select_employees;

DELIMITER $$
CREATE FUNCTION f_emp_avg_salary (p_emp_no INTEGER) RETURNS DECIMAL(10, 2)
DETERMINISTIC NO SQL READS SQL DATA
BEGIN

DECLARE v_avg_salary DECIMAL(10,2);

SELECT
    AVG(s.salary)
INTO v_avg_salary
FROM employees e
JOIN salaries s
ON e.emp_no = s.emp_no
WHERE e.emp_no = p_emp_no;

RETURN v_avg_salary;
END $$

DELIMITER ;

SELECT f_emp_avg_salary(11300);

SELECT @v_emp_no = 11300;
SELECT
    emp_no,
    first_name,
    last_name,
    f_emp_avg_salary(@v_emp_no) AS avg_salary
FROM
    employees
WHERE
    emp_no = @v_emp_no;

DELIMITER $$
CREATE FUNCTION emp_no(p_first_name VARCHAR(144), p_last_name VARCHAR(144)) RETURNS DECIMAL(10, 2)
DETERMINISTIC NO SQL READS SQL DATA
BEGIN
DECLARE v_salary DECIMAL(10, 2);

SELECT
    s.salary
INTO
    v_salary
FROM salaries s
JOIN employees e
ON s.emp_no = e.emp_no
WHERE p_first_name = e.first_name
AND p_last_name = e.last_name;

RETURN v_salary;
END $$
DELIMITER ;

SELECT emp_no('Georgi', 'Facello');
SELECT * from employees