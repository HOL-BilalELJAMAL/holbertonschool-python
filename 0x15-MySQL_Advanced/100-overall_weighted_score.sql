-- Script that creates a stored procedure ComputeOverallWeightedScoreForUser that computes and store the overall weighted score for a student
DELIMITER |
DROP PROCEDURE IF EXISTS ComputeOverallWeightedScoreForUser;
CREATE PROCEDURE ComputeOverallWeightedScoreForUser (IN user_id int)
BEGIN
UPDATE users AS u SET u.overall_score = (
SELECT SUM(c.score * p.weight) / SUM(p.weight)
FROM corrections AS c
LEFT JOIN projects AS p ON c.project_id = p.id
WHERE c.user_id = user_id
) WHERE u.id = user_id;
END;
|
