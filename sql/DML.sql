-- Variables prefixed with : and postfixed with input are values from the Python application.

--  Gets all Members from database with MembershipType 
SELECT member_id, member_first_name, member_last_name, membership_name from Members
    INNER JOIN MembershipTypes on MembershipTypes.membership_type_id = Members.membership_type_id;

--  Gets all Coaches
SELECT coach_id, member_first_name as coach_first_name, member_last_name as coach_last_name 
        from Members
        INNER JOIN Coaches on Coaches.member_id = Members.member_id;

-- All ClassTypes
SELECT class_type_id, class_type_name from ClassTypes;

-- All MembershipTypes
SELECT membership_type_id, membership_name, attendance_limit from MembershipTypes;

-- All ClassEnrollments
SELECT ClassEnrollments.class_enrollment_id, Classes.class_name, Members.member_first_name from ClassEnrollments
        INNER JOIN Members on Members.member_id = ClassEnrollments.member_id
        INNER JOIN Classes on Classes.class_id = ClassEnrollments.class_id
        ORDER BY Classes.class_name, Members.member_first_name;

-- Gets all Classes with ClassType and Coach
SELECT class_id, class_name, class_type_name, member_first_name as coach_name, class_duration_min, class_max_capacity, 
        DATE_FORMAT(class_date_time, '%Y-%m-%d %h:%i %p') AS class_date_time
        FROM Classes
        INNER JOIN Coaches on Coaches.coach_id = Classes.coach_id
        INNER JOIN Members on Members.member_id = Coaches.member_id
        INNER JOIN ClassTypes on ClassTypes.class_type_id = Classes.class_type_id;

-- Adds ClassEnrollment
INSERT INTO ClassEnrollments (class_id, member_id)
        VALUES (:class_id_input, :member_id_input);

-- Updates ClassEnrollment class_id taking in class_id and old_class_id and member_id
UPDATE ClassEnrollments 
        SET class_id = :class_id_input
        WHERE class_id = :old_class_id_input
        AND member_id = :member_id_input;

-- Deletes ClassEnrollment for member_id and class_id
DELETE FROM classEnrollments WHERE 
        class_id = :class_id_input
        AND member_id = :member_id_input;