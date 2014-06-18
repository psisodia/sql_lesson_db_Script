import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row
#Student: %s %s
#Github account: %s"""%(row[0], row[1], row[2])

def get_student_grades(github):
    query = """SELECT project_title, grade FROM grades WHERE student_github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row

def make_new_student(first_name,last_name,github):
    query = """INSERT into Students values(?,?,?)"""
    DB.execute(query,(first_name, last_name, github))
    CONN.commit()
    print "Successfully added strudent %s %s" %(first_name, last_name)

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)

    CONN.close()

if __name__ == "__main__":
    main()
