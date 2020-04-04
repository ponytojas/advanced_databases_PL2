#!/usr/bin/env python
# coding: utf-8

import random as rd
import psycopg2
from datetime import datetime as dt
import pandas as pd

def create_stock_tickets_csv(connection):

    cursor = connection.cursor()

    list_tickets= []
    barcode_item = []

    try:
        select_query_store= "select tickets.ticket_number from tickets"
        cursor.execute(select_query_store)
        list_tickets=cursor.fetchall()
        select_query_item= "select item.barcode from item"
        cursor.execute(select_query_item)
        barcode_item=cursor.fetchall()
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    list_to_csv = []

    for ticket in list_tickets:
        index_item = rd.randint(1,10)
        list_barcodes_for_store = []
        for index in range(index_item):
            barcode = rd.choice(barcode_item)
            
            while (barcode in list_barcodes_for_store):
                barcode = rd.choice(barcode_item)
                
            list_barcodes_for_store.append(barcode)
            
            barcode = barcode[0]

            list_to_csv.append(
                {
                'ticket_number' : ticket[0], 
                'Barcode_item' : barcode, 
                'Quantity' : rd.randint(1,10)
                }
                )

    df = pd.DataFrame.from_dict(list_to_csv)
    df.to_csv('./Our_Database/GeneratedCSV/stock_ticket_data.csv', sep=';', index = False, encoding="utf-8")




if __name__ == "__main__":
    password = str
    password = input("Introduce your postgres password: ")
    try:
        print('Trying to connect to DataBase')
        connection = psycopg2.connect(host="localhost",database="pel2", user="postgres", password=password)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    create_stock_tickets_csv(connection)