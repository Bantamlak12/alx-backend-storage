-- Creates a stored procedure that computes and store the average
-- weighted score for all student.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users U,
	(SELECT u.id, SUM(score * weight) / SUM(weight)
		AS average_weighted_score
		FROM users u
		JOIN corrections c ON u.id = c.user_id
		JOIN projects p ON p.id = c.project_id
		GROUP BY u.id)
	AS subquery

	SET U.average_score = subquery.average_weighted_score
	WHERE U.id = subquery.id;
END
$$
DELIMITER ;
