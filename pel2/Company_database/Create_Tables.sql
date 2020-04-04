DROP TABLE IF EXISTS staff CASCADE;
CREATE TABLE staff(
	employee_number 	NUMERIC     NOT NULL, 
	employee_firstname 	TEXT        NOT NULL,
	employee_lastname	TEXT        NOT NULL,   
	salary 		        NUMERIC     NOT NULL,
	CONSTRAINT staff_pk PRIMARY KEY (employee_number)
);

DROP TABLE IF EXISTS projects CASCADE;
CREATE TABLE projects(
	project_number 	    NUMERIC     NOT NULL, 
	projectname_name 	TEXT        NOT NULL,
	location	        TEXT        NOT NULL,   
	cost 		        NUMERIC     NOT NULL,
	CONSTRAINT projects_pk PRIMARY KEY (project_number)
);

DROP TABLE IF EXISTS project_employee CASCADE;
CREATE TABLE project_employee(
	employee_number     NUMERIC 	NOT NULL,
    project_number 		NUMERIC 	NOT NULL,
    hours				NUMERIC		NOT NULL,
	CONSTRAINT project_employee_pk  PRIMARY KEY (employee_number, project_number),
	CONSTRAINT employee_number_fk	FOREIGN KEY (employee_number)
        REFERENCES staff(employee_number) MATCH FULL
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
	CONSTRAINT projects_number_fk 	FOREIGN KEY (project_number)
        REFERENCES projects(project_number) MATCH FULL
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

COPY staff FROM '/Users/ponytojas/Downloads/table_data/staff_data.csv' WITH (FORMAT csv);
COPY projects FROM '/Users/ponytojas/Downloads/table_data/projects_data.csv' WITH (FORMAT csv);
COPY project_employee FROM '/Users/ponytojas/Downloads/table_data/project_employee_data.csv' WITH (FORMAT csv);


