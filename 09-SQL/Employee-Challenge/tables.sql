drop table employees;

CREATE TABLE employees(
    emp_no int not null primary key,
    emp_title_id varchar(10) null,
    birth_date date null,
    first_name varchar(50),
    last_name varchar(50),
    sex varchar(2) null,
    hire_date DATE null,
    last_updated timestamp null default current_timestamp
);

drop table "titles";

CREATE TABLE "titles" (
    "title_id" varchar(7)   NOT NULL,
    "title" varchar(50)   NOT NULL
);

drop table "departments";

CREATE TABLE "departments" (
    "dept_no" varchar(10)   NOT NULL,
    "dept_name" varchar(50)   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

drop table "dept_emp";

CREATE TABLE "dept_emp" (
    "dept_emp_id" SERIAL not null primary key,
    "emp_no" int null references employees("emp_no"),
    "dept_no" varchar(10) null references departments("dept_no"),
    "last_updated" timestamp null default current_timestamp
);

drop table "dept_manager";

CREATE TABLE "dept_manager" (
    "dept_manager_id" SERIAL not null primary key,
    "dept_no" varchar(10) null references departments("dept_no"),
    "emp_no" int null references employees("emp_no"),
    "last_updated" timestamp null default current_timestamp
);

drop table "salaries";

CREATE TABLE "salaries" (
    "salary_id" serial NOT NULL primary key,
    "emp_no" int null references employees("emp_no"),
    "salary" int null,
    "last_updated" timestamp null default current_timestamp
);
