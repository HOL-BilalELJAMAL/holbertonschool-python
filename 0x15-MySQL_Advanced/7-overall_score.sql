-- Script that creates a stored procedure ComputeOverallScoreForUser that computes and store the overall score for a student
DELIMITER |
DROP PROCEDURE IF EXISTS ComputeOverallScoreForUser;
CREATE PROCEDURE ComputeOverallScoreForUser (IN user_id int)
BEGIN
UPDATE users AS u SET u.overall_score = (
SELECT SUM(c.score)/COUNT(c.score) FROM corrections AS c WHERE c.user_id = user_id
) WHERE u.id = user_id;
END;
|
