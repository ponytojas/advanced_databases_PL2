COPY stock_ticket
    FROM './pel2/Our_Database/GeneratedCSV/stock_ticket_data.csv' 
    DELIMITER ';' CSV HEADER;
