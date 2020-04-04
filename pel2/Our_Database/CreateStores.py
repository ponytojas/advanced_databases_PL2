#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import random as rd
from uuid import uuid4 as uuid

def create_store_csv():

    provinces_csv = pd.read_csv('./Our_Database/provincias.csv')

    provinces = provinces_csv['name'].to_list()
    del provinces_csv

    cities_provinces= dict()
    contador_ciudades = 0
    cities_dict = dict()
    contador_barrios = 0


    for province in provinces:
        cities_provinces[province]= []
        index_random = rd.randint(80, 680)
        
        for index in range(index_random):
            city = 'city_' + str(uuid().hex)
            cities_provinces[province].append(city)
            cities_dict[city] = []
            
            index_barrios = rd.randint(5, 15)

            for _ in range(index_barrios):
                barrio = 'neighborhood_' + str(uuid().hex)
                cities_dict[city].append(barrio)

    stores = []
    for index in range (200000):
        stores.append('store_' + str(index + 1))

    list_to_csv = []
    for store in stores:
        temp_province = rd.choice(provinces)
        temp_city = rd.choice(cities_provinces[temp_province])
        temp_neighborhood = rd.choice(cities_dict[temp_city])
        
        list_to_csv.append(
            {
                'Nombre': store, 
                'Ciudad': temp_city, 
                'Barrio': temp_neighborhood, 
                'Provincia': temp_province
            }
        )

    df = pd.DataFrame.from_dict(list_to_csv)
    df.to_csv('./Our_Database/GeneratedCSV/store_data.csv', sep=';', index = False, encoding="utf-8")

if __name__ == "__main__":
    create_store_csv()

