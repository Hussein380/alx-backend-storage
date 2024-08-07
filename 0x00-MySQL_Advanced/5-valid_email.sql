-- Drop any existing trigger named 'validate_email' to avoid conflicts
DROP TRIGGER IF EXISTS validate_email;

-- Change the delimiter to $$ to allow using semicolons within the trigger body
DELIMITER $$

-- Create a new trigger named 'validate_email'
CREATE TRIGGER validate_email
-- Specify that the trigger should fire before an update operation on the 'users' table
BEFORE UPDATE ON users
-- Indicate that the trigger should execute for each row affected by the update
FOR EACH ROW
BEGIN
    -- Check if the email address is being changed
    IF OLD.email != NEW.email THEN
        -- If the email has changed, set 'valid_email' to 0
        SET NEW.valid_email = 0;
    ELSE
        -- If the email has not changed, retain the current value of 'valid_email'
        -- Note: This line is technically redundant and does not alter the value
        SET NEW.valid_email = NEW.valid_email;
    END IF;
END $$

-- Restore the delimiter back to the default semicolon
DELIMITER ;
