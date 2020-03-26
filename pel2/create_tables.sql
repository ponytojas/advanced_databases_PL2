
DROP TABLE IF EXISTS stores CASCADE;
CREATE TABLE stores(
	id 					SERIAL      NOT NULL, 
	name 			    TEXT        NOT NULL,
	city				TEXT        NOT NULL,   
	neighbourhood 		TEXT        NOT NULL,
	province			TEXT        NOT NULL,
	CONSTRAINT store_pk PRIMARY KEY (id)
);
ALTER TABLE stores OWNER TO ponytojas;

