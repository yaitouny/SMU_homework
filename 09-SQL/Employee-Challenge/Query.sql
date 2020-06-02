-- Listing details about employees and joining salaries table
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
from 
	employees as e
inner join 
	salaries as s on
e.emp_no = s.emp_no;

-- List first name, last name, and hire date for employees who were hired in 1986.
select 
	first_name, 
	last_name, 
	hire_date
from employees
where hire_date between '1986-01-01' and '1986-12-31';

-- List the manager of each department with the following information: department number, department name, 
-- the manager's employee number, last name, first name.
select 
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e.last_name,
	e.first_name
from departments d
join dept_manager dm on d.dept_no = dm.dept_no
join employees e on e.emp_no = dm.emp_no
join titles t on t.title_id = e.emp_title_id
where t.title = 'Manager';

-- List the department of each employee with the following information: employee number, last name, first name, and department name.
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from employees e 
join dept_emp de on e.emp_no = de.emp_no
join departments d on d.dept_no = de.dept_no;

-- List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select 
	first_name, 
	last_name,
	sex
from employees
where first_name = 'Hercules'
and last_name LIKE 'B%';

-- List all employees in the Sales department, including their employee number, last name, first name, and department name.
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from employees e 
join dept_emp de on e.emp_no = de.emp_no
join departments d on d.dept_no = de.dept_no
where d.dept_name = 'Sales';

-- List all employees in the Sales and Development departments, including their employee number, last name, first name, and 
-- department name.
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from employees e 
join dept_emp de on e.emp_no = de.emp_no
join departments d on d.dept_no = de.dept_no
where d.dept_name ='Development'
or d.dept_name ='Sales';

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name, count(last_name) as "Name count"
from employees
group by last_name
order by last_name desc;


