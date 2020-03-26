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

