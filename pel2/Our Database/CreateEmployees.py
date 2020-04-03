#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import random as rd
import time


# In[2]:


def generarDNI(numero):
    letras=['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L','C', 'K', 'E', 'O']
    dni = str(numero)+letras[numero%23]
    return dni


# In[3]:


t = time.time()

men_df = pd.read_csv('./NameAndSurname/hombres.csv')
men_list = men_df['nombre'].to_list()
del men_df

women_df = pd.read_csv('./NameAndSurname/mujeres.csv')
women_list = women_df['nombre'].to_list()
del women_df

names_list = men_list + women_list


rd.shuffle(names_list)


# In[4]:


surname_df = pd.read_csv('./NameAndSurname/apellidos.csv')
surname_df2 = pd.read_csv('./NameAndSurname/apellidos-20.csv')
surname_list = surname_df['apellido'].to_list() + surname_df2['apellido'].to_list()

del surname_df
del surname_df2

rd.shuffle(surname_list)


# In[5]:


puestos = ['Encargado', 'Reponedor', 'Cajero', 'Dependiente']


# In[6]:


random_numbers = rd.sample(range(1, 1000000000), 1000000)
rd.shuffle(random_numbers)


# In[7]:


result_list = []

for index in range(1000000):
    temp = {}
    tempDNI = generarDNI(random_numbers[index])
    temp['DNI'] = tempDNI
    temp['Nombre'] = rd.choice(names_list)
    temp['Apellidos'] = rd.choice(surname_list)+ ' ' + rd.choice(surname_list)
    temp['Puesto'] = rd.choice(puestos)
    temp['Salario'] = rd.randint(1000, 5000)
    result_list.append(temp)
    print(len(result_list))


# In[8]:


df = pd.DataFrame(result_list)
df.to_csv('./Employees.csv', sep=';', index=False)
print("Hemos acabado")
elapsed = time.time() - t
print('Hemos utilizado: ' + str(elapsed))


# In[ ]:




