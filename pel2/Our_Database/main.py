#!/usr/bin/env python3
# coding: utf-8

import psycopg2
import time

from Our_Database.CreateEmployees.py import create_employee_csv as create_employees
from Our_Database.CreateItems.py import create_item_csv as create_items
from Our_Database.CreateStores.py import create_store_csv as create_stores
from Our_Database.CreateStockItem.py import create_stock_item_csv as create_stock_items
from Our_Database.CreateTickets.py import create_ticket_csv as create_tickets
from Our_Database.CreateStockTicket.py import create__stock_tickets_csv as create__stock_ticket

def create_database():
    start_total_time = time.time()
    
    password = str
    password = input("Introduce your postgres password")
    try:
        print('Trying to connect to DataBase')
        connection = psycopg2.connect(host="localhost",database="pel2", user="postgres", password=password)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    create_tables(connection)
    create_employees_items_and_stores(connection)
    print("--- %s seconds --- To create the database from employees, items and stores" % (time.time() - start_time))
    create_stock_and_tickets(connection)
    create_stock_tickets(connection)
    print("--- %s seconds --- Total time to create the database" % (time.time() - start_total_time))

def create_tables(connection):
    print('Starting to create the tables of the store database')

    file = open("./Our_Database/create_tables.sql","r")
    print('Reading the SQL file')
    sql = s = " ".join(file.readlines())
    print('Creating SQL query')

    cursor = connection.cursor()
    cursor.execute(sql)    
    connection.commit()

    print("All correct, let's continue")

def create_employees_items_and_stores(connection):
    print("Starting to create the data from employees, items and stores")

    create_employees()
    create_items()
    create_stores()

    print("Starting to insert the data created")

    file = open("./Our_Database/1st_copy.sql","r")
    print('Reading the SQL file')
    sql = s = " ".join(file.readlines())
    print('Creating SQL query')

    cursor = connection.cursor()
    cursor.execute(sql)    
    connection.commit()

    print("All correct, let's continue")

def create_stock_tickets_and_stocktickets(connection):
    print("Starting to create the data from stock of items and tickets")

    create_stock_items(connection)
    create_tickets(connection)

    print("Starting to insert the data created")
    file = open("./Our_Database/2nd_copy.sql","r")
    print('Reading the SQL file')
    sql = s = " ".join(file.readlines())
    print('Creating SQL query')

    cursor = connection.cursor()
    cursor.execute(sql)    
    connection.commit()

    print("All correct, let's continue")

def create_stock_tickets(connection):
    print("Starting to create the data from stock of tickets")

    create__stock_ticket(connection)

    print("Starting to insert the data created")
    file = open("./Our_Database/3rd_copy.sql","r")
    print('Reading the SQL file')
    sql = s = " ".join(file.readlines())
    print('Creating SQL query')

    cursor = connection.cursor()
    cursor.execute(sql)    
    connection.commit()

    print("All database created")


if __name__ == "__main__":
    create_database()
