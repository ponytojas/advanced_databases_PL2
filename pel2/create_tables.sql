DROP TABLE IF EXISTS store CASCADE;
CREATE TABLE store(
	id 					SERIAL      NOT NULL, 
	name 			    TEXT        NOT NULL,
	city				TEXT        NOT NULL,   
	neighbourhood 		TEXT        NOT NULL,
	province			TEXT        NOT NULL,
	CONSTRAINT store_pk PRIMARY KEY (id)
);
ALTER TABLE store OWNER TO ponytojas;


DROP TABLE IF EXISTS item CASCADE;
CREATE TABLE item(
	barcode            TEXT        NOT NULL,
	name               TEXT        NOT NULL,
	type               TEXT        NOT NULL,
	descripction        TEXT 		NOT NULL,
	price              INTEGER     NOT NULL,
	CONSTRAINT item_pk  PRIMARY KEY(barcode)
);
ALTER TABLE item OWNER TO ponytojas;

DROP TABLE IF EXISTS employee CASCADE;
CREATE TABLE employee(
	id 		        	SERIAL 		NOT NULL,
	store 				INTEGER 	NOT NULL,
	dni					TEXT		NOT NULL,
	first_name			TEXT		NOT NULL,
	last_name 			TEXT		NOT NULL,
	position 		   TEXT		   NOT NULL ,
	salary				INTEGER		NOT NULL,
	CONSTRAINT employee_pk 	    PRIMARY KEY (id),
	CONSTRAINT employee_dni		UNIQUE (dni),
	CONSTRAINT shop_fk 			FOREIGN KEY (store)
        REFERENCES store(id) MATCH FULL
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
ALTER TABLE employee OWNER TO ponytojas;