CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(25) NOT NULL,
	last_name varchar(35) NOT NULL,
	titlte varchar(50) NOT NULL,
	birth_date date,
    notes text
);

CREATE TABLE customers
(
    customer_id varchar(50) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
	contact_name varchar(70) NOT NULL
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
	customer_id varchar(50) REFERENCES customers(customer_id) NOT NULL,
    employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(50)
);
