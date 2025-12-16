import sqlite3

def main():
    database_name = "student.db"
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()

    while True:
        choose = input("Would you like to 1 create, 2 update, 3 delete, 4 read, 5 to view all data, or 6 to exit.")
        if choose == '1':
            create(cur)
            conn.commit()
        elif choose == '2':
            read(cur)
            conn.commit()
        elif choose == '3':
            update(cur)
            conn.commit()
        elif choose == '4':
            delete(cur)
            conn.commit()
        elif choose == '5':
            view(cur)
            conn.commit()
        else:
            conn.close()
            exit()

def create(cur):
    ID = input("Enter student ID: ")
    name = input("Enter name: ")
    GPA = input("Enter GPA: ")
    GraduationYear = input("Enter your Graduation Year: ")
    Age = input("Enter your Age: ")
    Major = input("Enter your Major: ")
    Degree = input("Enter your in progress Degree: ")


    cur.execute("INSERT INTO Entries (ID, name, GPA, GraduationYear, Age, Major, Degree) VALUES (?, ?)", (ID, name, GPA, GraduationYear, Age, Major, Degree))

def read(cur):
    reading = input("What field do you want to read?")
    row = cur.fetchone()
    if row:
        ID = row[0]
        name = row[1]
        GPA = row[2]
        GraduationYear = row[3]
        Age = row[4]
        Major = row[5]
        Degree = row[6]
        return ID, name, GPA, GraduationYear, Age, Major, Degree
    else:
        return None

def update(cur):
    id_val = input("Enter student ID to update: ") 
    # Use consistent naming (id vs ID) based on your table creation
    cur.execute("SELECT id FROM entries WHERE id=?", (id_val,))
    if cur.fetchone():
        # Inputting data
        name = input("Enter new name: ")
        gpa = input("Enter new GPA: ")
        grad_year = input("Enter new Graduation Year: ")
        age = input("Enter new Age: ")
        major = input("Enter new Major: ")
        degree = input("Enter new Degree: ")

        cur.execute(
            "UPDATE entries SET name=?, gpa=?, graduationyear=?, age=?, major=?, degree=? WHERE id=?",
            (name, gpa, grad_year, age, major, degree, id_val)
        )
        print("Record updated successfully.")
    else:
        print(f"Error: Student ID {id_val} not found.")

def delete(cur):
    id_val = input("Enter student ID to delete: ")
    # Check existence first for better error reporting
    cur.execute("SELECT id FROM entries WHERE id=?", (id_val,))
    if cur.fetchone():
        cur.execute("DELETE FROM entries WHERE id=?", (id_val,))
        print("Record deleted successfully.")
    else:
        print(f"Error: Student ID {id_val} not found.")

def read(cur):
    id_val = input("Enter student ID to read: ")
    cur.execute("SELECT * FROM entries WHERE id=?", (id_val,))
    row = cur.fetchone()
    if row:
        print(row)
    else:
        print(f"Error: Student ID {id_val} not found.")

def view(cur):
    cur.execute("SELECT * FROM entries")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No entries found in the database.")
