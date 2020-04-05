COPY stock_item 
    FROM 'C:/Users/Daniel/Documents/Universidad/GitHub/BBDD_advanzadas/advanced_databases_PL2/pel2/Our_Database/GeneratedCSV/stock_item_data.csv' 
    DELIMITER ';' CSV HEADER;

COPY tickets (total_price, ticket_date, employee_id)  
    FROM 'C:/Users/Daniel/Documents/Universidad/GitHub/BBDD_advanzadas/advanced_databases_PL2/pel2/Our_Database/GeneratedCSV/ticket_data.csv' 
    DELIMITER ';' CSV HEADER;
