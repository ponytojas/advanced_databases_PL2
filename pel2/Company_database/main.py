#!/usr/bin/python3
# -*- coding: utf-8 -*-
import psycopg2
import time

def create_company_databases():
    print('Starting to create the company database')
    file = open("./Company_database/Create_Tables.sql","r")
    print('Reading the SQL file')
    sql = s = " ".join(file.readlines())
    print('Creating SQL query')
        password = str
    password = input("Introduce your postgres password")
    try:
        print('Trying to connect to DataBase')
        connection = psycopg2.connect(host="localhost",database="pel2", user="postgres", password=password)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    cursor = connection.cursor()
    print('Starting the query, this will take a time')
    start_time = time.time()
    cursor.execute(sql)    
    connection.commit()
    print("--- %s seconds --- To execute the query" % (time.time() - start_time))
    print("All correct, let's close connection")
    connection.close()
    print('Comming back to main program')

if __name__ == '__main__':
    create_company_databases()