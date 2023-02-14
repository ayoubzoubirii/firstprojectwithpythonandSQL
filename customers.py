import pypyodbc as db  # database
import tkinter as TkCUSTOMERS  # for btn and label
from tkinter import simpledialog as read  # for inputs

#################################################### DATABASE CONNECTION #################################################

# db info
DRIVER_NAME = "SQL SERVER"
SERVER_NAME = "AZ"
DATABASE_NAME = "storefv"
# connection to db sql server by ssms
conn = db.connect(
    f" DRIVER={{{DRIVER_NAME}}}; SERVER={SERVER_NAME}; DATABASE={DATABASE_NAME};   "
)
cursor = conn.cursor()


############################################################ insert_data ##################################
def insert_data():
    root1 = TkCUSTOMERS.Tk()
    # CustomerID = input("CustomerID: ")
    # FirstName = input("FirstName: ")
    # LastName = input("LastName: ")
    # Address = input("Address: ")
    # City = input("City: ")
    # Mobile = input("Mobile: ")
    # Email = input("Email: ")

    CustomerID = read.askstring("Input", "CustomerID:", parent=root1)
    FirstName = read.askstring("Input", "FirstName:", parent=root1)
    LastName = read.askstring("Input", "LastName: ", parent=root1)
    Address = read.askstring("Input", "Address: ", parent=root1)
    City = read.askstring("Input", "City: ", parent=root1)
    Mobile = read.askstring("Input", "Mobile: ", parent=root1)
    Email = read.askstring("Input", "Email: ", parent=root1)

    cursor.execute(
        """
        INSERT INTO Customers (CustomerID,FirstName, LastName, Address, City, Mobile, Email)
        VALUES (?,?, ?, ?, ?, ?, ?)
         """,
        (CustomerID, FirstName, LastName, Address, City, Mobile, Email),
    )

    print("Data inserted")
    conn.commit()
    root1.mainloop()
    conn.close()


####################################################### select_data ##########################################

def select_data():
    root2 = TkCUSTOMERS.Tk()
    cursor.execute("SELECT * FROM customers")

    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        for j, column_value in enumerate(row):
            label = TkCUSTOMERS.Label(root2, text=column_value)
            label.grid(row=i, column=j)

        edit_button = TkCUSTOMERS.Button(root2, text="Edit", command=lambda row=row: edit_data(row[0]))
        edit_button.grid(row=i, column=j + 1)
        delete_button = TkCUSTOMERS.Button(root2, text="Delete", command=lambda row=row: delete_datab(row[0]))
        delete_button.grid(row=i, column=j + 2)

    root2.mainloop()
    conn.close()

################################################### edit_data(id) ############################################


def edit_data(id):
    root3 = TkCUSTOMERS.Tk()
    cursor.execute("SELECT * FROM customers WHERE CustomerID=?", (id,))
    result = cursor.fetchone()

    CustomerID = read.askstring(
        "Input", "CustomerID:", parent=root3, initialvalue=result[0]
    )
    FirstName = read.askstring(
        "Input", "FirstName:", parent=root3, initialvalue=result[1]
    )
    LastName = read.askstring(
        "Input", "LastName: ", parent=root3, initialvalue=result[2]
    )
    Address = read.askstring("Input", "Address: ", parent=root3, initialvalue=result[3])
    City = read.askstring("Input", "City: ", parent=root3, initialvalue=result[4])
    Mobile = read.askstring("Input", "Mobile: ", parent=root3, initialvalue=result[5])
    Email = read.askstring("Input", "Email: ", parent=root3, initialvalue=result[6])

    cursor.execute(
        """
        UPDATE Customers
        SET CustomerID=?, FirstName=?, LastName=?, Address=?, City=?, Mobile=?, Email=?
        WHERE CustomerID=?
        """,
        (CustomerID, FirstName, LastName, Address, City, Mobile, Email, id),
    )

    print("Data updated")
    conn.commit()
    root3.destroy()
    select_data()
    conn.close()


######################################################### update_data() ######################################


def update_data():
    root3 = TkCUSTOMERS.Tk()
    CustomerID = read.askstring("Input", "CustomerID:", parent=root3)
    FirstName = read.askstring("Input", "FirstName:", parent=root3)
    LastName = read.askstring("Input", "LastName: ", parent=root3)
    Address = read.askstring("Input", "Address: ", parent=root3)
    City = read.askstring("Input", "City: ", parent=root3)
    Mobile = read.askstring("Input", "Mobile: ", parent=root3)
    Email = read.askstring("Input", "Email: ", parent=root3)

    cursor.execute(
        """
        UPDATE Customers
        SET FirstName=?, LastName=?, Address=?, City=?, Mobile=?, Email=?
        WHERE CustomerID=?
        """,
        (FirstName, LastName, Address, City, Mobile, Email, CustomerID),
    )

    print("Data updated")
    conn.commit()
    root3.mainloop()
    conn.close()


######################################################## delete_datab(id) ######################################


def delete_datab(id):
    root4 = TkCUSTOMERS.Tk()
    cursor.execute(
        """
        DELETE FROM Customers
        WHERE CustomerID=?
        """,
        (id,),
    )

    print("Data deleted")
    conn.commit()
    root4.destroy()
    select_data()
    conn.close()


######################################################### delete_data() #####################################


def delete_data():
    root4 = TkCUSTOMERS.Tk()
    CustomerID = read.askstring("Input", "CustomerID:", parent=root4)

    cursor.execute(
        """
        DELETE FROM Customers
        WHERE CustomerID=?
        """,
        (CustomerID,),
    )

    print("Data deleted")
    conn.commit()
    root4.mainloop()
    select_data()
    conn.close()

#######################################################    CRUD    ################################################

# dashbord for crud

def btn():
    root = TkCUSTOMERS.Tk()

    button1 = TkCUSTOMERS.Button(
    root,
    text="Insert data",
    command=insert_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="blue",
)
    button2 = TkCUSTOMERS.Button(
    root,
    text="read data",
    command=select_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="green",
)
    button3 = TkCUSTOMERS.Button(
    root,
    text="Update data",
    command=update_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="yellow",
)
    button4 = TkCUSTOMERS.Button(
    root,
    text="Delete data",
    command=delete_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="red",
)



    button2.pack()
    button1.pack()
    button3.pack()
    button4.pack()
    root.mainloop()
    cursor.close()
    conn.close()
    
##################################################### conn.close() ################################################



