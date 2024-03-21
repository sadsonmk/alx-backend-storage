-- create a SQL script that creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER //
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - 1
	WHERE item_id = orders.id;
END;
//
DELIMITER ;

