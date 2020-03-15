#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import random as rd


# In[2]:


provinces_csv = pd.read_csv('provincias.csv')


# In[3]:


provinces_csv = provinces_csv['name'].to_list()


# In[4]:


dict_stores = []
counter = 1

for index in range (0, 200000):
    store_province = rd.choice(provinces_csv)
    
    store = {'Id_tienda': counter, 'Nombre': 'store_' + str(counter), 'Ciudad' : 'X' , 'Barrio': '1', 'Provincia': store_province}
    dict_stores.append(store)
    counter += 1


# In[ ]:





# In[5]:


df = pd.DataFrame.from_dict(dict_stores)
df.to_csv('./Tienda.csv', sep=';', index = False)


# In[ ]:




