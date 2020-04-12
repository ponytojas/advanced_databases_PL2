CREATE INDEX employee_store ON employee USING hash (store);
CREATE INDEX stock_store ON stock_item USING hash (store);
CREATE INDEX employee_ticket ON tickets USING hash (employee_id);
CREATE INDEX ticket_number ON items_ticket USING hash (ticket_number);

VACUUM FULL store;
VACUUM FULL employee;
VACUUM FULL stock_item;
VACUUM FULL tickets;
VACUUM FULL items_ticket;

ALTER TABLE employee
DROP CONSTRAINT shop_fk,
ADD CONSTRAINT shop_fk FOREIGN KEY (store)
REFERENCES public.store (id) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE employee
DROP CONSTRAINT shop_fk,
ADD CONSTRAINT shop_fk FOREIGN KEY (store) REFERENCES public.store (id) 
ON UPDATE CASCADE ON DELETE CASCADE;

DELETE FROM store where store.id in (SELECT id FROM store TABLESAMPLE BERNOULLI(50));



