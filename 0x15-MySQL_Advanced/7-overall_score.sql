-- Script that creates a stored procedure ComputeOverallScoreForUser that computes and store the overall score for a student
DELIMITER |
CREATE PROCEDURE IF EXISTS ComputeOverallScoreForUser (IN user_id int);
BEGIN
UPDATE users AS u set u.overall_score = (
SELECT FLOOR(SUM(c.score)/COUNT(c.score)) FROM corrections AS c where c.user_id = user_id
) WHERE u.id = user_id;
END;
|
