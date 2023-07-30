"""Скрипт для заполнения данными таблиц в БД Postgres."""
import configparser

from data_uploader import DataUploader
from config import DATABASE_PASSWORD

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('database.ini')

    db_params = {
        "host": config.get('postgresql', 'host'),
        "database": config.get('postgresql', 'database'),
        "user": config.get('postgresql', 'user'),
        "password": DATABASE_PASSWORD
    }

    # Путь к файлам с данными
    customers_data_file = "north_data/customers_data.csv"
    employees_data_file = "north_data/employees_data.csv"
    orders_data_file = "north_data/orders_data.csv"

    # Создание экземпляра класса и загрузка данных
    uploader = DataUploader(db_params)
    uploader.connect()
    uploader.upload_customers(customers_data_file)
    uploader.upload_employees(employees_data_file)
    uploader.upload_orders(orders_data_file)
    uploader.conn.commit()
    uploader.disconnect()
