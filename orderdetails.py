import pypyodbc as db  # database
import tkinter as TK_ORDR_DATAILS  # for btn and label
from tkinter import simpledialog as read  # for inputs

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
    root1 = TK_ORDR_DATAILS.Tk()
    OrderID = read.askstring("Input", "OrderID:", parent=root1)
    ProductID = read.askstring("Input", "ProductID:", parent=root1)
    Quantity = read.askstring("Input", "Quantity: ", parent=root1)

    cursor.execute(
        """
        INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
        VALUES (?,?, ?)
         """,
        (OrderID, ProductID, Quantity),
    )

    print("Data inserted")
    conn.commit()
    root1.mainloop()

    conn.close()

####################################################### select_data ##########################################

def select_data():
    root2 = TK_ORDR_DATAILS.Tk()
    cursor.execute("SELECT OrderID, ProductID, Quantity FROM OrderDetails")

    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        for j, column_value in enumerate(row):
            label = TK_ORDR_DATAILS.Label(root2, text=column_value)
            label.grid(row=i, column=j)

        edit_button = TK_ORDR_DATAILS.Button(root2, text="Edit", command=lambda row=row: edit_data(row[0], row[1]))
        edit_button.grid(row=i, column=j + 1)
        delete_button = TK_ORDR_DATAILS.Button(root2, text="Delete", command=lambda row=row: delete_datab(row[0], row[1]))
        delete_button.grid(row=i, column=j + 2)

    root2.mainloop()
    conn.close()

################################################### edit_data(id) ############################################


def edit_data(OrderID, ProductID):
    root3 = TK_ORDR_DATAILS.Tk()
    cursor.execute("SELECT * FROM OrderDetails WHERE OrderID=? AND ProductID=?", (OrderID, ProductID))
    result = cursor.fetchone()

    OrderID = read.askstring(
        "Input", "OrderID:", parent=root3, initialvalue=result[0]
    )
    ProductID = read.askstring(
        "Input", "ProductID:", parent=root3, initialvalue=result[1]
    )
    Quantity = read.askstring(
        "Input", "Quantity: ", parent=root3, initialvalue=result[2]
    )

    cursor.execute(
        """
        UPDATE OrderDetails
        SET OrderID=?, ProductID=?, Quantity=?
        WHERE OrderID=? AND ProductID=?
        """,
        (OrderID, ProductID, Quantity, result[0], result[1]),
    )

    print("Data updated")
    conn.commit()
    root3.destroy()
    select_data()

    conn.close()

######################################################### update_data() ######################################


def update_data():
    root3 = TK_ORDR_DATAILS.Tk()
    OrderID = read.askstring("Input", "OrderID:", parent=root3)
    ProductID = read.askstring("Input", "ProductID:", parent=root3)
    Quantity = read.askstring("Input", "Quantity: ", parent=root3)

    cursor.execute(
        """
        UPDATE OrderDetails
        SET Quantity=?
        WHERE OrderID=? AND ProductID=?
        """,
        (Quantity, OrderID, ProductID),
    )

    print("Data updated")
    conn.commit()
    root3.mainloop()

    conn.close()

######################################################## delete_datab(OrderID, ProductID) ######################################


def delete_datab(OrderID, ProductID):
    root4 = TK_ORDR_DATAILS.Tk()
    cursor.execute(
        """
        DELETE FROM OrderDetails
        WHERE OrderID=? AND ProductID=?
        """,
        (OrderID, ProductID),
    )

    print("Data deleted")
    conn.commit()
    root4.destroy()
    select_data()
    conn.close()


######################################################### delete_data() #####################################


def delete_data():
    root4 = TK_ORDR_DATAILS.Tk()
    OrderID = read.askstring("Input", "OrderID:", parent=root4)
    ProductID = read.askstring("Input", "ProductID:", parent=root4)

    cursor.execute(
        """
        DELETE FROM OrderDetails
        WHERE OrderID=? AND ProductID=?
        """,
        (OrderID, ProductID),
    )

    print("Data deleted")
    conn.commit()
    root4.mainloop()
    select_data()

    conn.close()

#######################################################    CRUD    ################################################

# dashboard for CRUD

def btn():
    root = TK_ORDR_DATAILS.Tk()

    button1 = TK_ORDR_DATAILS.Button(
    root,
    text="Insert data",
    command=insert_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="blue",
)
    button2 = TK_ORDR_DATAILS.Button(
    root,
    text="Read data",
    command=select_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="green",
)
    button3 = TK_ORDR_DATAILS.Button(
    root,
    text="Update data",
    command=update_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="yellow",
)
    button4 = TK_ORDR_DATAILS.Button(
    root,
    text="Delete data",
    command=delete_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="red",
)

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    root.mainloop()
    cursor.close()
    conn.close()

