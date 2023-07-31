"""Скрипт для заполнения данными таблиц в БД Postgres."""
import database

quary_customers = """INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s);"""

quary_employees = """INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)
                     VALUES (%s, %s, %s, %s, %s, %s);"""

quary_orders = """INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)
                    VALUES (%s, %s, %s, %s, %s);"""

database.instert_to_db("north_data/customers_data.csv", quary_customers)
database.instert_to_db("north_data/employees_data.csv", quary_employees)
database.instert_to_db("north_data/orders_data.csv", quary_orders)
