from db_connector import SwoleSociety
import mysql.connector

def main():
    conn = None
    cursor  = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='swoleSociety'
        )

        cursor = conn.cursor()

        q = SwoleSociety(cursor, conn)

        # Start every run from a clean copy of the sample data
        q.resetDatabase()
        print("Database reset to sample data before tests.")

        # Perform READ opertions for all tables

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

        # Add class enrollment
        
        results = q.addClassEnrollment(1, 4)
        print("Adding Class Enrollment")
        # print("Rows Inserted: ", results)

        classEnrollments = q.getAllClassEnrollments()
        print("Updated ClassEnrollments: ")
        print(cursor.column_names)
        for c in classEnrollments:
            print(c)

        # Update class enrollment
        
        results = q.updateClassEnrollment(4, 1, 2) # member_id, old_class_id, new_class_id
        print("Update successful: member 4 moved from class 1 to class 2")

        classEnrollments = q.getAllClassEnrollments()
        print("Updated ClassEnrollments: ")
        print(cursor.column_names)
        for c in classEnrollments:
            print(c)

        # Test the update procedure's error checks
        try:
            q.updateClassEnrollment(4, 2, 99)   # enrollment exists, but class 99 doesn't
        except Exception as e:
            print("Expected error (bad new_class_id):", e)

        try:
            q.updateClassEnrollment(4, 1, 2)    # member 4 is no longer in class 1
        except Exception as e:
            print("Expected error (no matching enrollment):", e)

        # Delete class enrollment
        
        results = q.deleteClassEnrollment(2, 4)
        print("Delete successful: member 4 removed from class 2")

        classEnrollments = q.getAllClassEnrollments()
        print("Updated ClassEnrollments: ")
        print(cursor.column_names)
        for c in classEnrollments:
            print(c)

        # Add extra enrollment to demonstrate reset works

        results = q.addClassEnrollment(3, 4)
        print("Class Enrollments BEFORE reset: ")
        for c in q.getAllClassEnrollments():
            print(c)


        # Reset Database
        
        results = q.resetDatabase()
        print("Database reset. ClassEnrollments should return to the 4 sample rows: ")
        
        classEnrollments = q.getAllClassEnrollments()
        print("All ClassEnrollments: ")
        print(cursor.column_names)
        for c in classEnrollments:
            print(c)

    except Exception as e:
        print("Error: ", e)

    finally: 
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()