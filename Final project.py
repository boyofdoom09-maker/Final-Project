import sqlite3
#this allows the program to make the db
#ALL DEBUGGED! WE'RE DONE!
def create_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Entries (
            ID TEXT PRIMARY KEY,
            name TEXT,
            GPA REAL,
            GraduationYear INTEGER,
            Age INTEGER,
            Major TEXT,
            Degree TEXT
        )
    """)

def main():
    database_name = "student.db"
    conn = sqlite3.connect(database_name)

    cur = conn.cursor()
    create_table(cur)

    while True:
        choose = input("Would you like to 1 create, 2 read, 3 update, 4 delete, 5 to view all data, or 6 to exit?")
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
    Degree = input("Enter your Degree: ")


    cur.execute("INSERT INTO Entries (ID, name, GPA, GraduationYear, Age, Major, Degree) VALUES (?, ?, ?, ?, ?, ?, ?)", (ID, name, GPA, GraduationYear, Age, Major, Degree))

def update(cur):
    ID_val = input("Enter student ID to update: ")
    # Use consistent naming (ID) based on your table creation
    #use ID, that's what I was doing
    cur.execute("SELECT ID FROM Entries WHERE ID=?", (ID_val,))
    if cur.fetchone():
        # Inputting data
        Name = input("Enter new name: ")
        gpa = input("Enter new GPA: ")
        grad_year = input("Enter new Graduation Year: ")
        age = input("Enter new Age: ")
        major = input("Enter new Major: ")
        degree = input("Enter new Degree: ")

        cur.execute(
            "UPDATE Entries SET name=?, GPA=?, GraduationYear=?, Age=?, Major=?, Degree=? WHERE ID=?",
            (Name, gpa, grad_year, age, major, degree, ID_val)
        )
        print("Record updated successfully.")
    else:
        print(f"Error: Student ID {ID_val} not found.")

def delete(cur):
    ID_val = input("Enter student ID to delete: ")
    # Check existence first for better error reporting
    cur.execute("SELECT ID FROM Entries WHERE ID=?", (ID_val,))
    if cur.fetchone():
        cur.execute("DELETE FROM Entries WHERE ID=?", (ID_val,))
        print("Record deleted successfully.")
    else:
        print(f"Error: Student ID {ID_val} not found.")

def read(cur):
    ID_val = input("Enter student ID to read: ")
    cur.execute("SELECT * FROM Entries WHERE ID=?", (ID_val,))
    row = cur.fetchone()
    if row:
        print(row)
    else:
        print(f"Error: Student ID {ID_val} not found.")

def view(cur):
    cur.execute("SELECT * FROM Entries")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No entries found in the database.")

if __name__ == "__main__":
    main()