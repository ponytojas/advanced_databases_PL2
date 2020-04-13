COPY stock_item 
    FROM './pel2/Our_Database/GeneratedCSV/stock_item_data.csv' 
    DELIMITER ';' CSV HEADER;

COPY tickets (total_price, ticket_date, employee_id)  
    FROM './pel2/Our_Database/GeneratedCSV/ticket_data.csv' 
    DELIMITER ';' CSV HEADER;
