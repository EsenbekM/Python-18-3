import sqlite3
from sqlite3 import Error


# CRUD (Create, Reed, Update, Delete)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error:
        print(Error)
    return conn


def create_table(conn, sql_to_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_to_create_table)
        return conn
    except Error:
        print(Error)


database = r'group_18_3.db'
conn = create_connection(database)

sql_create_table_students = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (200) NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''


def create_student(conn, student):
    sql = '''INSERT INTO students (fullname, mark, hobby, birth_date, is_married) 
    VALUES (?, ?, ?, ?, ?)'''
    try:
        c = conn.cursor()
        c.execute(sql, student)
        conn.commit()
    except Error:
        print(Error)
    return None

def delete_student(conn, id):
    sql = '''DELETE FROM students WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)

def update_student_mark(conn, student):
    sql = '''UPDATE students SET mark = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, student)
        conn.commit()
    except Error:
        print(Error)

def select_all_students(conn):
    sql = '''SELECT * FROM students'''
    try:
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for i in rows:
            print(i)
    except Error:
        print(Error)

def select_students_by_mark(conn, mark):
    sql = '''SELECT * FROM students WHERE mark >= ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (mark,))
        rows = c.fetchall()

        for i in rows:
            print(i)
    except Error:
        print(Error)

if conn is not None:
    print("Connected Successfully")
    # create_table(conn, sql_create_table_students)
    # delete_student(conn, 10)
    # update_student_mark(conn, (100.0, 5))
    # select_all_students(conn)
    select_students_by_mark(conn, 90.0)

    # create_student(conn, ("Emir Ysak", 98.0, "Sleep", "2005-12-29", True))
    # create_student(conn, ("Kanat Usmanov", 98.0, "Basketball", "2002-11-07", True))
    # create_student(conn, ("Mark Daniels", 77.12, "Football", "1999-01-02", False))
    # create_student(conn, ("Alex Brilliant", 77.12, None, "1989-12-31", True))
    # create_student(conn, ("Diana Julls", 99.3, "Tennis", "2005-01-22", True))
    # create_student(conn, ("Michael Corse", 100.0, "Diving", "2001-09-17", True))
    # create_student(conn, ("Jack Moris", 50.2, "Fishing and cooking", "2001-07-12", True))
    # create_student(conn, ("Viola Manilson", 41.82, None, "1991-03-01", False))
    # create_student(conn, ("Joanna Moris", 100.0, "Painting and arts", "2004-04-13", False))
    # create_student(conn, ("Peter Parker", 32.0, "Travelling and bloging", "2002-11-28", False))
    # create_student(conn, ("Paula Parkerson", 77.09, None, "2001-11-28", True))
    # create_student(conn, ("George Newel", 93.0, "Photography", "1981-01-24", True))
    # create_student(conn, ("Miranda Alistoun", 87.55, "Playing computer games", "1997-12-22", False))
    # create_student(conn, ("Fiona Giordano", 66.12, "Driving fast", "1977-01-15", True))
    conn.close()
