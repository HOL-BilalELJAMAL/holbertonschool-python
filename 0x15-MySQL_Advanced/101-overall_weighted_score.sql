-- Script that creates a stored procedure ComputeOverallWeightedScoreForUsers that computes and store the overall weighted score for all students
DELIMITER |
DROP PROCEDURE IF EXISTS ComputeOverallWeightedScoreForUsers;
CREATE PROCEDURE ComputeOverallWeightedScoreForUsers ()
BEGIN
UPDATE users AS u SET u.overall_score = (
SELECT SUM(c.score * p.weight) / SUM(p.weight)
FROM corrections AS c
LEFT JOIN projects AS p ON c.project_id = p.id
WHERE c.user_id = u.id
);
END;
|
