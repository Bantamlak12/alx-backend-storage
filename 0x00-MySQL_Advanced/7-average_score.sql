-- A stored procedure that computes and store the average score for student.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE a_score FLOAT;

	SELECT AVG(score)
	INTO a_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	UPDATE users
	SET average_score = a_score
	WHERE id = user_id;
END
$$
DELIMITER ;
