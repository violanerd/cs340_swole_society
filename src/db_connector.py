class SwoleSociety:
    def __init__(self, cursor, connection=None):
        self.cursor = cursor
        self.connection = connection

    def _commit(self):
        """Commit if a connection object was provided."""
        if self.connection is not None:
            self.connection.commit()


    # Read Operations all tables in Schema
    def getAllMembers(self):
        """
        Gets all Members from database with MembershipType 
        """
        sql = """
        SELECT member_id, CONCAT(member_first_name, ' ', member_last_name) AS member_name, membership_name from Members
        INNER JOIN MembershipTypes on MembershipTypes.membership_type_id = Members.membership_type_id
        ORDER BY member_last_name, member_first_name
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def getAllCoaches(self):
        """
        Gets all Coaches
        """
        sql = """
        SELECT coach_id, CONCAT(member_first_name, ' ', member_last_name) AS coach_name
        from Members
        INNER JOIN Coaches on Coaches.member_id = Members.member_id
        ORDER BY member_last_name, member_first_name
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def getAllClasses(self):
        """
        Gets all Classes with ClassType and Coach
        """
        sql = """
        SELECT class_id, class_name, class_type_name, CONCAT(member_first_name, ' ', member_last_name) AS coach_name, class_duration_min, class_max_capacity, 
        DATE_FORMAT(class_date_time, '%Y-%m-%d %h:%i %p') AS class_date_time
        FROM Classes
        INNER JOIN Coaches on Coaches.coach_id = Classes.coach_id
        INNER JOIN Members on Members.member_id = Coaches.member_id
        INNER JOIN ClassTypes on ClassTypes.class_type_id = Classes.class_type_id
        ORDER BY Classes.class_date_time
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def getAllClassTypes(self):
        """
        All ClassTypes
        """
        sql = """
        SELECT class_type_id, class_type_name from ClassTypes
        ORDER BY class_type_name
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def getAllMembershipTypes(self):
        """
        All MembershipTypes
        """
        sql = """
        SELECT membership_type_id, membership_name, attendance_limit from MembershipTypes
        ORDER BY membership_name
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def getAllClassEnrollments(self):
        """
        All ClassEnrollments
        """
        sql = """
        SELECT ClassEnrollments.class_enrollment_id, Classes.class_name, CONCAT(member_first_name, ' ', member_last_name) AS member_name from ClassEnrollments
        INNER JOIN Members on Members.member_id = ClassEnrollments.member_id
        INNER JOIN Classes on Classes.class_id = ClassEnrollments.class_id
        ORDER BY Classes.class_name, member_last_name, member_first_name
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

 
    def addClassEnrollment(self, class_id, member_id):
        """
        Add ClassEnrollment
        """
        sql = """
        INSERT INTO ClassEnrollments (class_id, member_id)
        VALUES (%s, %s)
        """
        self.cursor.execute(sql, (class_id, member_id))
        self._commit()
        rowcount = self.cursor.rowcount
        return rowcount

    def updateClassEnrollment(self, class_id, old_class_id, member_id):
        """
        Update ClassEnrollment with new class_id
        """
        sql = """
        UPDATE ClassEnrollments 
        SET class_id = %s
        WHERE class_id = %s
        AND member_id = %s
        """
        self.cursor.execute(sql, (class_id, old_class_id, member_id))
        self._commit()
        rowcount = self.cursor.rowcount
        return rowcount

    def deleteClassEnrollment(self, class_id, member_id):
        """
        Delete ClassEnrollment by member and class id
        """
        sql = """
        DELETE FROM ClassEnrollments WHERE 
        class_id=%s
        AND member_id = %s
        """
        self.cursor.execute(sql, (class_id, member_id))
        self._commit()
        rowcount = self.cursor.rowcount
        return rowcount

