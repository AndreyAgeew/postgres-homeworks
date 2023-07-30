-- Таблица employees
CREATE TABLE employees
(
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  title VARCHAR(50),
  birth_date DATE,
  notes TEXT
);

-- Таблица customers
CREATE TABLE customers
(
  customer_id VARCHAR(10) PRIMARY KEY,
  company_name VARCHAR(40),
  contact_name VARCHAR(40)
);

-- Таблица orders
CREATE TABLE orders
(
  order_id SERIAL PRIMARY KEY,
  customer_id VARCHAR(10),
  employee_id INT,
  order_date DATE,
  ship_city VARCHAR(30),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);