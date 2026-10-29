import mysql.connector

class SwoleSociety:
    def __init__(self):
        self.conn = mysql.connector.connect(
        user='root',
        password='',
        database='swoleSociety'
        )
        self.cursor = self.conn.cursor(dictionary=True)

    # Read Operations all tables in Schema
    def getAllMembers(self):
        #TODO! 
        sql = """
        Select member_first_name from Members where member_id = 1;
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def getAllCoaches(self):
        cursor = self.cursor(dictionary=True)
        sql = """
        TODO
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def getAllClasses(self):
        cursor = self.cursor(dictionary=True)
        sql = """
        TODO
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def getAllClassTypes(self):
        cursor = self.cursor(dictionary=True)
        sql = """
        TODO
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def getAllMembershipTypes(self):
        cursor = self.cursor(dictionary=True)
        sql = """
        TODO
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def getAllClassEnrollments(self):
        cursor = self.cursor(dictionary=True)
        sql = """
        TODO
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    # TODO CUD for ClassEnrollments
    # def addClassEnrollment(self, args):
    #     cursor = self.cursor(dictionary=True)
    #     sql = """
    #     """
    #     cursor.execute(sql, (args))
    #     self.conn.commit()
    #     rowcount = cursor.rowcount
    #     return rowcount

    #  def updateClassEnrollment(self, args):
    #     cursor = self.cursor(dictionary=True)
    #     sql = """
    #     """
    #     cursor.execute(sql, (args))
    #     self.conn.commit()
    #     rowcount = cursor.rowcount
    #     return rowcount

    #  def deleteClassEnrollment(self, enrollmentId):
    #     cursor = self.cursor(dictionary=True)
    #     sql = "DELETE FROM bsg_people WHERE id=%s"
    #     cursor.execute(sql, (enrollmentId))
    #     self.conn.commit()
    #     rowcount = cursor.rowcount
    #     return rowcount

    def close(self):
        self.cursor.close()
        self.conn.close()