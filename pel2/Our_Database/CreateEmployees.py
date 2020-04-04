#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import random as rd
import time

def generarDNI(numero):
    letras=['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L','C', 'K', 'E', 'O']
    dni = str(numero)+letras[numero%23]
    return dni

def create_employee_csv():

    men_df = pd.read_csv('./Our_Database/NameAndSurname/hombres.csv')
    men_list = men_df['nombre'].to_list()
    del men_df

    women_df = pd.read_csv('./Our_Database/NameAndSurname/mujeres.csv')
    women_list = women_df['nombre'].to_list()
    del women_df

    names_list = men_list + women_list

    rd.shuffle(names_list)

    surname_df = pd.read_csv('./Our_Database/NameAndSurname/apellidos.csv')
    surname_df2 = pd.read_csv('./Our_Database/NameAndSurname/apellidos-20.csv')
    surname_list = surname_df['apellido'].to_list() + surname_df2['apellido'].to_list()

    del surname_df
    del surname_df2

    rd.shuffle(surname_list)

    puestos = ['Encargado', 'Reponedor', 'Cajero', 'Dependiente']

    random_numbers = rd.sample(range(1, 1000000000), 1000000)
    rd.shuffle(random_numbers)

    result_list = []

    for index in range(1000000):
        temp = {}
        temp['Tienda'] = int(rd.randint(1,200000))
        tempDNI = generarDNI(random_numbers[index])
        temp['DNI'] = tempDNI
        temp['Nombre'] = rd.choice(names_list)
        temp['Apellidos'] = rd.choice(surname_list)+ ' ' + rd.choice(surname_list)
        temp['Puesto'] = rd.choice(puestos)
        temp['Salario'] = int(rd.randint(1000, 5000))
        result_list.append(temp)

    df = pd.DataFrame(result_list)
    df.to_csv('./Our_Database/GeneratedCSV/employee_data.csv', sep=';', index=False)

if __name__ == "__main__" :
    create_employee_csv()

