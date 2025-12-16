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

#set up update function
def update(cur):

def delete(cur):
# set up delete function

def view(cur):
    cur.execute("SELECT * FROM Entries")
    rows = cur.fetchall()

    print("\n--- CONTACT LIST ---")
    for row in rows:
        print(f"ID: {row[0]} | name: {row[1]} | GPA: {row[2]} | GraduationYear: {row[3]} | Age: {row[4]} | Major: {row[5]} | Degree: {row[6]}")
    print("---------------------\n")

if __name__ == "__main__":
    main()