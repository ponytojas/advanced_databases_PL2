#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Company_database.main import create_company_databases as create_company
from Our_Database.main import create_database as create_store_databse

def main():
    exit = 0
    while(not exit):
        user_input = str
        print('Welcome to the main program, here you can choose this two options:\n')
        print('a) Create company database and add all data')
        print('b) Create the store database with new data')
        print('s) Exit the program')
        user_input = input("Choice: ")
        if(user_input == 'a'):
            create_company()
        elif(user_input == 'b'):
            create_store_databse()
        elif(user_input == 's'):
            exit = 1
        else:
            print('Something went wrong')
            del user_input
    print('See you later, aligator')


if __name__ == "__main__":
   main()