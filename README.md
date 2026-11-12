# Swole Society Repo

## Project Details

### Title

Swole Society Membership Database

### Authors
Project Group 8 
Group Members: Gabrielle Abdon, Madalyne Cross

### Description
Swole Society is a Bay Area gym with over 250 members, 6 coaches, and approximately 30 specialty classes per week across HIIT, Olympic Lifting, and Mobility. Currently, class registration is managed with paper sign-up sheets and member records are stored separately, resulting in overbookings, duplicate sign-ups, and limited attendance tracking.

To support growth, Swole Society needs a database-driven system to manage members, coaches, class schedules, and bookings. The new system will track class attendance, prevent overbooking, allow coaches to also participate as members, and support multiple membership tiers with different weekly class limits while maintaining open gym access on a first-come, first-served basis.

## Setup

### Installation/Dependency Requirements
- MySql 8+
- Python 3
- mysql-connector-python
- Data definition language with inserts in DDL.sql must be imported into a local database

### Local Setup
- Clone Repository or download and unzip files

- Open new Mysql session ```mysql -u root -p```

- Create database 
    ```Create database swoleSociety;```
- Use database 
    ```Use swoleSociety;```
- Import the schema and sample data ```source DDL.sql```

### Create Python venv and install requirements, instructions for MacOS 
- From home directory, create python virtual environment 
```python3 -m venv venv```
- Activate venv from home directory
```source venv/bin/activate```
- Install requirements
```pip3 install -r requirements.txt```

### Replace database configurations in test_app.py with your MySql credentials  
    # replace credentials here with your MySql credentials
    conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='swoleSociety'
        )
    cursor = conn.cursor()

### Run the application

- If cloned: From home directory ```python3 src/test_app.py```
- If unzipped run test_app.py ```python3 test_app.py```

## Expected Output
    All ClassTypes: 
    ('class_type_id', 'class_type_name')
    (1, 'HIIT')
    (3, 'Mobility')
    (2, 'Olympic Lifting')
    All MembershipTypes: 
    ('membership_type_id', 'membership_name', 'attendance_limit')
    (1, 'Basic', 2)
    (2, 'Plus', 4)
    (3, 'Unlimited', -1)
    All members in the database with MembershipType: 
    ('member_id', 'member_name', 'membership_name')
    (3, 'Bob Saget', 'Basic')
    (1, 'Michelle Tanner', 'Plus')
    (4, 'Ralph Waldo', 'Basic')
    (2, 'Ted Mosby', 'Unlimited')
    All coaches in the database: 
    ('coach_id', 'coach_name')
    (3, 'Bob Saget')
    (1, 'Michelle Tanner')
    (2, 'Ted Mosby')
    All Classes in the database with ClassType and Coach: 
    ('class_id', 'class_name', 'class_type_name', 'coach_name', 'class_duration_min', 'class_max_capacity', 'class_date_time')
    (1, 'Morning Mobility', 'Mobility', 'Michelle Tanner', 60, 5, '2026-12-01 09:00 AM')
    (2, 'Evening Mobility', 'Mobility', 'Michelle Tanner', 60, 5, '2026-12-01 06:00 PM')
    (3, 'Morning Olympic Lifting', 'Olympic Lifting', 'Ted Mosby', 60, 5, '2026-12-02 09:00 AM')
    All ClassEnrollments: 
    ('class_enrollment_id', 'class_name', 'member_name')
    (2, 'Evening Mobility', 'Bob Saget')
    (1, 'Morning Mobility', 'Ted Mosby')
    (4, 'Morning Olympic Lifting', 'Bob Saget')
    (3, 'Morning Olympic Lifting', 'Michelle Tanner')
    Adding Class Enrollment
    Rows Inserted:  1
    Updated ClassEnrollments: 
    ('class_enrollment_id', 'class_name', 'member_name')
    (2, 'Evening Mobility', 'Bob Saget')
    (6, 'Morning Mobility', 'Ralph Waldo')
    (1, 'Morning Mobility', 'Ted Mosby')
    (4, 'Morning Olympic Lifting', 'Bob Saget')
    (3, 'Morning Olympic Lifting', 'Michelle Tanner')
    Updating Class Enrollment class_id
    Rows Updated:  1
    Updated ClassEnrollments: 
    ('class_enrollment_id', 'class_name', 'member_name')
    (2, 'Evening Mobility', 'Bob Saget')
    (6, 'Evening Mobility', 'Ralph Waldo')
    (1, 'Morning Mobility', 'Ted Mosby')
    (4, 'Morning Olympic Lifting', 'Bob Saget')
    (3, 'Morning Olympic Lifting', 'Michelle Tanner')
    Deleting ClassEnrollment
    Rows Updated:  1
    Updated ClassEnrollments: 
    ('class_enrollment_id', 'class_name', 'member_name')
    (2, 'Evening Mobility', 'Bob Saget')
    (1, 'Morning Mobility', 'Ted Mosby')
    (4, 'Morning Olympic Lifting', 'Bob Saget')
    (3, 'Morning Olympic Lifting', 'Michelle Tanner')


## Acknowledgements and Originality 

#### Citation for the following documents: db_connector.py and test_app.py
Date 11/3/2026
db_connector.py and test_app.py based on CS340 Assignment code for Python CRUD Query App - reworked to fit use case.  
CS340 Fall 2026 Canvas, Python CRUD Query App Assignment. 
https://canvas.oregonstate.edu/courses/2061186/assignments/10623045

#### Citation for use of AI Tools, datetime formatting in function getAllClasses:
Date 11/3/2026 
Prompts used to generate SQL: Make this more user friendly
Microsoft. (November 2026). Microsoft Copilot [large language model]. https://copilot.microsoft.com

#### Citation for use of AI Tools, description:
Date 11/3/2026 
Prompts used to generate description: Take description and make it brief. Output in description.
Microsoft. (November 2026). Microsoft Copilot [large language model]. https://copilot.microsoft.com

#### Citation for use of AI Tools, cursor error:
Date 11/3/2026 
Prompts used to debug cursor error: Why is my cursor working in first example and not second. Unnecessary second object
Microsoft. (November 2026). Microsoft Copilot [large language model]. https://copilot.microsoft.com
 
#### Citation for use of AI Tools, print columns:
Date 11/3/2026 
Prompts used to get command: How can I print columns with python mysql 
Microsoft. (November 2026). Microsoft Copilot [large language model]. https://copilot.microsoft.com


#### All other work is original. 




