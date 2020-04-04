#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import random as rd


# In[2]:


counter = 1
item_name =[]

for index in range(0, 1000000):
    item_name.append('item_' + str(counter))
    counter += 1


# In[3]:


counter = 1
item_type = []

for index in range(0, 300):
    item_type.append('type_' + str(counter))
    counter += 1


# In[4]:


dict_items = []
barcode_counter = 0

for item in item_name:
    barcode_counter += 1
    barcode = str(barcode_counter).zfill(7)  
    type_item = rd.choice(item_type)
    price = rd.randint(50, 1000)
    description = "Nombre: " + str(item) + "   Tipo: " + str(type_item) +"   Precio: " + str(price)
    
    item = {'Codigo de barras': barcode, 'Nombre': item, 'Tipo': type_item, 'Descripcion': description, 'Precio': price}
    dict_items.append(item)


# In[7]:


dict_items


# In[13]:


df = pd.DataFrame.from_dict(dict_items, index=False)


# In[14]:


df.to_csv('./Productos.csv', sep=';', index = False)


# In[ ]:




