COPY store (name, city, neighbourhood, province)  
    FROM 'C:/Users/Daniel/Documents/Universidad/GitHub/BBDD_advanzadas/advanced_databases_PL2/pel2/Our_Database/GeneratedCSV/store_data.csv' 
    DELIMITER ';' CSV HEADER;

COPY employee (store, dni, first_name, last_name, position, salary) 
    FROM 'C:/Users/Daniel/Documents/Universidad/GitHub/BBDD_advanzadas/advanced_databases_PL2/pel2/Our_Database/GeneratedCSV/employee_data.csv' 
    DELIMITER ';' CSV HEADER;

COPY item FROM 
    'C:/Users/Daniel/Documents/Universidad/GitHub/BBDD_advanzadas/advanced_databases_PL2/pel2/Our_Database/GeneratedCSV/item_data.csv' 
    DELIMITER ';' CSV HEADER;
