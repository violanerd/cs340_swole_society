from db_connector import SwoleSociety

def main():
    try:
        db = SwoleSociety()

        members = db.getAllMembers()
        print(members, "TEST")
    except:
        db.close()
    finally: 
        if db is not None:
            db.close()

if __name__ == "__main__":
    main()