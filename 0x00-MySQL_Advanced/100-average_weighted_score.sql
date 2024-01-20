-- Creates a stored procedure that computes and store the average
-- weighted score for a student.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE average_weighted_score FLOAT;

	SELECT SUM(score * weight) / SUM(weight)
	INTO average_weighted_score
	FROM users AS u
	JOIN corrections AS c
	ON u.id = c.user_id
	JOIN projects AS p
	ON p.id = c.project_id
	WHERE u.id = user_id;

	UPDATE users
	SET average_score = average_weighted_score
	WHERE id = user_id;
END
$$
DELIMITER ;
