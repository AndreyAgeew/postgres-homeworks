import csv
import psycopg2


class CustomersDataMixin:
    def upload_customers(self, customers_data_file):
        try:
            with open(customers_data_file, "r") as file:
                reader = csv.reader(file)
                next(reader)
                with self.conn.cursor() as cur:
                    cur.executemany(
                        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                        reader
                    )
        except (FileNotFoundError, psycopg2.Error) as e:
            print(f"Error uploading customers data: {e}")


class EmployeesDataMixin:
    def upload_employees(self, employees_data_file):
        try:
            with open(employees_data_file, "r") as file:
                reader = csv.reader(file)
                next(reader)
                with self.conn.cursor() as cur:
                    cur.executemany(
                        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) "
                        "VALUES (%s, %s, %s, %s, %s, %s)",
                        reader
                    )
        except (FileNotFoundError, psycopg2.Error) as e:
            print(f"Error uploading employees data: {e}")


class OrdersDataMixin:
    def upload_orders(self, order_data_file):
        try:
            with open(order_data_file, "r") as file:
                reader = csv.reader(file)
                next(reader)
                with self.conn.cursor() as cur:
                    cur.executemany(
                        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) "
                        "VALUES (%s, %s, %s, %s, %s)",
                        reader
                    )
        except (FileNotFoundError, psycopg2.Error) as e:
            print(f"Error uploading orders data: {e}")


class DataUploader(CustomersDataMixin, EmployeesDataMixin, OrdersDataMixin):
    def __init__(self, db_params):
        self.db_params = db_params
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.db_params)
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        try:
            if self.conn is not None:
                self.conn.close()
        except psycopg2.Error as e:
            print(f"Error disconnecting from the database: {e}")


