import psycopg2
import csv
from pathlib import Path

CUSTOMERS_FILE = Path(__file__).parent.joinpath("north_data", "customers_data.csv")
EMPLOYEES_FILE = Path(__file__).parent.joinpath("north_data", "employees_data.csv")
ORDERS_FILE = Path(__file__).parent.joinpath("north_data", "orders_data.csv")

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)
with conn.cursor() as cur:
    with open(CUSTOMERS_FILE, "r") as file:
        all_data = csv.reader(file)
        list_customers = list(all_data)
        del list_customers[0]
        for row in list_customers:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", tuple(row))
    with open(EMPLOYEES_FILE, "r") as file:
        all_data = csv.reader(file)
        list_employees = list(all_data)
        del list_employees[0]
        for row in list_employees:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", tuple(row))
    with open(ORDERS_FILE, "r") as file:
        all_data = csv.reader(file)
        list_orders = list(all_data)
        del list_orders[0]
        for row in list_orders:
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", tuple(row))
    conn.commit()
