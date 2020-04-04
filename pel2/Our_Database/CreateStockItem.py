#!/usr/bin/env python
# coding: utf-8

import random as rd
import pandas as pd
import psycopg2

def create_stock_item_csv(connection):

    cursor = connection.cursor()

    list_stores= []
    barcode_item = []

    try:
        select_query_store= "select store.id from store"
        cursor.execute(select_query_store)
        list_stores=cursor.fetchall()
        select_query_item= "select item.barcode from item"
        cursor.execute(select_query_item)
        barcode_item=cursor.fetchall()
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    list_for_csv = []

    for store in list_stores:
        index_item = rd.randint(90,110)
        list_barcodes_for_store = []
        for index in range(index_item):
            barcode = rd.choice(barcode_item)
            
            while (barcode in list_barcodes_for_store):
                barcode = rd.choice(barcode_item)
                
            list_barcodes_for_store.append(barcode)
            
            barcode = barcode[0]
            list_for_csv.append(
                {
                "Store_id" = store[0], 
                "Barcode_item" = barcode, 
                "Quantity" = rd.randint(10,200)
                }
                )

    df = pd.DataFrame.from_dict(list_for_csv)
    df.to_csv('./Our_Database/GeneratedCSV/stock_item_data.csv', sep=';', index = False, encoding="utf-8")

if __name__ == "__main__":
    password = str
    password = input("Introduce your postgres password")
    try:
        print('Trying to connect to DataBase')
        connection = psycopg2.connect(host="localhost",database="pel2", user="postgres", password=password)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    create_stock_item_csv(connection)
