-- Variables prefixed with : and postfixed with input are values from the Python application.


-- CreateClassEnrollment PL/SQL
-- Adds ClassEnrollment
DROP PROCEDURE IF EXISTS sp_create_class_enrollment;

DELIMITER //
CREATE PROCEDURE sp_create_class_enrollment(
        IN p_class_id int,
        IN p_member_id int,
        OUT p_class_enrollment_id int
)
BEGIN
        INSERT INTO ClassEnrollments (class_id, member_id)
        VALUES (p_class_id, p_member_id);

        SELECT LAST_INSERT_ID() INTO p_class_enrollment_id;
END //
DELIMITER ;

-- UpdateClassEnrollment PL/SQL
-- Updates ClassEnrollment class_id taking in class_id and old_class_id and member_id
DROP PROCEDURE IF EXISTS sp_update_class_enrollment;

DELIMITER //
CREATE PROCEDURE sp_update_class_enrollment(
        IN p_member_id int,
        IN p_old_class_id int,
        IN p_new_class_id int
)
BEGIN
        UPDATE ClassEnrollments 
        SET class_id = p_new_class_id
        WHERE class_id = p_old_class_id
                AND member_id = p_member_id;
END //
DELIMITER ;

-- DeleteClassEnrollment PL/SQL
-- Deletes ClassEnrollment for member_id and class_id
DROP PROCEDURE IF EXISTS sp_delete_class_enrollment;

DELIMITER //
CREATE PROCEDURE sp_delete_class_enrollment(
        IN p_class_id int,
        IN p_member_id int
)
BEGIN
        DECLARE v_rows_deleted INT DEFAULT 0;
        DECLARE error_message VARCHAR(255);

        DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN  
                ROLLBACK;
                RESIGNAL;
        END;

        START TRANSACTION;
                DELETE FROM ClassEnrollments 
                WHERE 
                        class_id = p_class_id
                        AND member_id = p_member_id;

                SET v_rows_deleted = ROW_COUNT();

                IF v_rows_deleted = 0 THEN
                        SET error_message = CONCAT('No matching record found in ClassEnrollments for 
                                member_id ' , p_member_id, ' in class_id ', p_class_id);

                        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
                END IF;
        COMMIT;
END //
DELIMITER ;