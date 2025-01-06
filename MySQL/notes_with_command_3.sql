select * from employees.employees
order by emp_no desc limit 10;

insert into employees.employees
(
    emp_no,
    birth_date,
    first_name,
    last_name,
    gender,
    hire_date
) values
(
    999901,
    '1986-04-21',
    'John',
    'Smith',
    'M',
    '2011-01-01'
);

create table departments_dup
(
    dept_no char(4) not null,
    dept_name varchar(40) not null
);

insert into sales.departments_dup
(
 dept_no,
 dept_name
)
select * from sales.departments_dup;