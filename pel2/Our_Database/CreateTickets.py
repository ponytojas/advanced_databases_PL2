#!/usr/bin/env python3
# coding: utf-8

import random as rd
import psycopg2
from datetime import datetime as dt

def create_tickets_csv(connection):

    cursor = connection.cursor()
    list_employees= []

    try:
        select_query_store= "select employee.id from employee;"
        cursor.execute(select_query_store)
        list_employees=cursor.fetchall()
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    start_date = dt(2019, 1, 1).toordinal()
    end_date = dt(2019,12,31).toordinal()

    list_of_days = [rd.randint(start_date, end_date) for iter in range(5000000)]
    rd.shuffle(list_of_days)

    list_to_csv = []

    for index in range(5000000):

        random_day = dt.fromordinal(list_of_days.pop())
        random_day = random_day.strftime('%Y-%m-%d')

        id_employee= rd.choice(list_employees)

        list_to_csv.append(
        {        
        'Barcode_item' : rd.randint(100,10000), 
        'Date' : random_day,
        'Employee_id' : id_employee[0], 
        }
        )

    df = pd.DataFrame.from_dict(list_to_csv)
    df.to_csv('./Our_Database/GeneratedCSV/ticket_data.csv', sep=';', index = False, encoding="utf-8")

if __name__ == "__main__":
    password = str
    password = input("Introduce your postgres password: ")
    try:
        print('Trying to connect to DataBase')
        connection = psycopg2.connect(host="localhost",database="pel2", user="postgres", password=password)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    create_tickets_csv(connection)