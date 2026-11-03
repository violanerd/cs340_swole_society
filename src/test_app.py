from db_connector import SwoleSociety
import mysql.connector

def main():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='swoleSociety'
        )
        cursor = conn.cursor()

        q = SwoleSociety(cursor, conn)

        classes = q.getAllClassTypes()
        print("All ClassTypes: ")
        print(cursor.column_names)
        for c in classes:
            print(c)
        
        classes = q.getAllMembershipTypes()
        print("All MembershipTypes: ")
        print(cursor.column_names)
        for c in classes:
            print(c)
        
        members = q.getAllMembers()
        print("All members in the database with MembershipType: ")
        print(cursor.column_names)
        for m in members:
            print(m)

        coaches = q.getAllCoaches()
        print("All coaches in the database: ")
        print(cursor.column_names)
        for c in coaches:
            print(c)
        
        classes = q.getAllClasses()
        print("All Classes in the database with ClassType and Coach: ")
        print(cursor.column_names)
        for c in classes:
            print(c)
        
        classEnrollments = q.getAllClassEnrollments()
        print("All ClassEnrollments: ")
        print(cursor.column_names)
        for c in classEnrollments:
            print(c)
        
        results = q.addClassEnrollment(1, 4)
        print("Adding Class Enrollment")
        print("Rows Inserted: ", results)

        classEnrollments = q.getAllClassEnrollments()
        print("Updated ClassEnrollments: ")
        print(cursor.column_names)
        for c in classEnrollments:
            print(c)
        
        results = q.updateClassEnrollment(2, 1, 4)
        print("Updating Class Enrollment class_id")
        print("Rows Updated: ", results)

        classEnrollments = q.getAllClassEnrollments()
        print("Updated ClassEnrollments: ")
        print(cursor.column_names)
        for c in classEnrollments:
            print(c)
        
        results = q.deleteClassEnrollment(2, 4)
        print("Deleting ClassEnrollment")
        print("Rows Updated: ", results)

        classEnrollments = q.getAllClassEnrollments()
        print("Updated ClassEnrollments: ")
        print(cursor.column_names)
        for c in classEnrollments:
            print(c)


    except Exception as e:
        print(e)
        cursor.close()
        conn.close()

    finally: 
        if cursor is not None:
            cursor.close()
            conn.close()
if __name__ == "__main__":
    main()