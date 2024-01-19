-- Create a view 'need_meeting' that lists all students that have
-- scored under 80 and no 'last_meeting' or more that 1 month.
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE students.score < 80
	AND (students.last_meeting IS NULL
	OR students.last_meeting > ADDDATE(CURDATE(), INTERVAL - 1 MONTH));
