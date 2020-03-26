#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import random as rd
from uuid import uuid4 as uuid


# In[2]:


provinces_csv = pd.read_csv('provincias.csv')


# In[3]:


provinces = provinces_csv['name'].to_list()
del provinces_csv


# In[4]:


cities_provinces= dict()
contador_ciudades = 0
cities_dict = dict()
contador_barrios = 0


for province in provinces:
    cities_provinces[province]= []
    index_random = rd.randint(80, 680)
    contador_ciudades += index_random
    
    for index in range(index_random):
        city = 'city_' + str(uuid().hex)
        cities_provinces[province].append(city)
        cities_dict[city] = []
        
        index_barrios = rd.randint(5, 15)
        contador_barrios += index_barrios
        for index_2 in range (index_barrios):
            barrio = 'neighborhood_' + str(uuid().hex)
            cities_dict[city].append(barrio)

print(contador_ciudades)
print(contador_barrios)


# In[5]:


stores = []
for index in range (200000):
    stores.append('store_' + str(index + 1))


# In[6]:


list_for_csv = []
for store in stores:
    temp_province = rd.choice(provinces)
    temp_city = rd.choice(cities_provinces[temp_province])
    temp_neighborhood = rd.choice(cities_dict[temp_city])
    
    list_for_csv.append(
        {
            'Nombre': store, 
            'Ciudad': temp_city, 
            'Barrio': temp_neighborhood, 
            'Provincia': temp_province
        }
    )


# In[7]:


df = pd.DataFrame.from_dict(list_for_csv)
df.to_csv('./Tienda.csv', sep=';', index = False, encoding="utf-8")


# In[ ]:


# Insertar mediante transaccion en la base de datos #


# In[ ]:





# In[ ]:





# In[ ]:




