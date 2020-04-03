DROP TABLE IF EXISTS staff CASCADE;
CREATE TABLE staff(
	employee_number 	INTEGER     NOT NULL, 
	employee_firstname 	TEXT        NOT NULL,
	employee_lastname	TEXT        NOT NULL,   
	salary 		        INTEGER     NOT NULL,
	CONSTRAINT staff_pk PRIMARY KEY (employee_number)
);
ALTER TABLE staff OWNER TO daniel;

DROP TABLE IF EXISTS projects CASCADE;
CREATE TABLE projects(
	project_number 	    INTEGER     NOT NULL, 
	projectname_name 	TEXT        NOT NULL,
	location	        TEXT        NOT NULL,   
	cost 		        INTEGER     NOT NULL,
	CONSTRAINT projects_pk PRIMARY KEY (project_number)
);
ALTER TABLE projects OWNER TO daniel;

DROP TABLE IF EXISTS project_employee CASCADE;
CREATE TABLE project_employee(
	employee_number     INTEGER 	NOT NULL,
    project_number 		INTEGER 	NOT NULL,
    hours				INTEGER		NOT NULL,
	CONSTRAINT project_employee_pk  PRIMARY KEY (employee_number, project_number),
	CONSTRAINT employee_number_fk	FOREIGN KEY (employee_number)
        REFERENCES staff(employee_number) MATCH FULL
        ON DELETE RESTRICT
        ON UPDATE CASCADE
	CONSTRAINT projects_number_fk 	FOREIGN KEY (projects_number)
        REFERENCES projects(project_number) MATCH FULL
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
