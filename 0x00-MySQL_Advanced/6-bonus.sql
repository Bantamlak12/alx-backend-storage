-- creates a stored procedure `AddBonus` that
-- adds a new correction for a student.
DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score FLOAT
)
BEGIN
	DECLARE project_id INT;

	-- Create the name if no `projects.name` found
	IF (SELECT name FROM projects WHERE name = project_name) IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;

	-- Add correction
	SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
	INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, project_id, score);
END
$$
DELIMITER ;
