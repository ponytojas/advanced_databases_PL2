DROP TABLE IF EXISTS store CASCADE;
CREATE TABLE store(
	id 					SERIAL      NOT NULL, 
	name 			    TEXT        NOT NULL,
	city				TEXT        NOT NULL,   
	neighbourhood 		TEXT        NOT NULL,
	province			TEXT        NOT NULL,
	CONSTRAINT store_pk PRIMARY KEY (id)
);

DROP TABLE IF EXISTS item CASCADE;
CREATE TABLE item(
	barcode            TEXT        NOT NULL,
	name               TEXT        NOT NULL,
	type               TEXT        NOT NULL,
	descripction       TEXT 		NOT NULL,
	price              INTEGER     NOT NULL,
	CONSTRAINT item_pk  PRIMARY KEY(barcode)
);

DROP TABLE IF EXISTS employee CASCADE;
CREATE TABLE employee(
	id 		        	SERIAL 		NOT NULL,
	store 				INTEGER 	NOT NULL,
	dni					TEXT		NOT NULL,
	first_name			TEXT		NOT NULL,
	last_name 			TEXT		NOT NULL,
	position 		   	TEXT		   NOT NULL ,
	salary				INTEGER		NOT NULL,
	CONSTRAINT employee_pk 	    PRIMARY KEY (id),
	CONSTRAINT employee_dni		UNIQUE (dni),
	CONSTRAINT shop_fk 			FOREIGN KEY (store)
        REFERENCES store(id) MATCH FULL
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS stock_item CASCADE;
CREATE TABLE stock_item(
	store           INTEGER 	NOT NULL,
	barcode         TEXT    	NOT NULL,
	quantity        INTEGER 	NOT NULL,
	CONSTRAINT store_item_pk   PRIMARY KEY (store, barcode),
	CONSTRAINT store_fk    FOREIGN KEY (store)
        REFERENCES store(id) MATCH FULL 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
	CONSTRAINT barcode_fk  FOREIGN KEY (barcode)
        REFERENCES item(barcode) MATCH FULL
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS tickets CASCADE;
CREATE TABLE tickets(
	ticket_number 	SERIAL		NOT NULL,
	total_price     INTEGER     NOT NULL,
    ticket_date    	DATE        NOT NULL,
	employee_id     INTEGER     NOT NULL,
	CONSTRAINT ticket_pk  PRIMARY KEY(ticket_number),
	CONSTRAINT employee_fk FOREIGN KEY(employee_id) 
        REFERENCES employee(id) MATCH FULL 
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS stock_ticket CASCADE;
CREATE TABLE stock_ticket(
	ticket_number      	INTEGER 	NOT NULL,
    item_barcode        TEXT    	NOT NULL,
    quantity            INTEGER 	NOT NULL,
    CONSTRAINT inv_items_pk    PRIMARY KEY (ticket_number, item_barcode),
    CONSTRAINT tickets_fk     FOREIGN KEY (ticket_number) 
        REFERENCES tickets(ticket_number) MATCH FULL
        ON DELETE CASCADE
        ON UPDATE CASCADE,
		CONSTRAINT items_fk        FOREIGN KEY (item_barcode)
        REFERENCES item(barcode) MATCH FULL
        ON DELETE CASCADE
        ON UPDATE CASCADE
);