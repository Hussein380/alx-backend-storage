-- Creates a stored procedure AddBonus that adds a new
-- correction for a student.
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    DECLARE project_count INT DEFAULT 0;
    DECLARE project_id INT DEFAULT 0;

    -- Check if the project already exists
    SELECT COUNT(id)
        INTO project_count
        FROM projects
        WHERE name = project_name;
    
    -- If the project does not exist, create it
    IF project_count = 0 THEN
        INSERT INTO projects(name)
            VALUES(project_name);
    END IF;
    
    -- Retrieve the project ID
    SELECT id
        INTO project_id
        FROM projects
        WHERE name = project_name;
    
    -- Insert the correction record
    INSERT INTO corrections(user_id, project_id, score)
        VALUES (user_id, project_id, score);
END $$
DELIMITER ;
