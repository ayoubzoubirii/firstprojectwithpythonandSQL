import pypyodbc as db  # database
import tkinter as TK_ORDR  # for btn and label
from tkinter import simpledialog as read  # for inputs

#################################################### DATABASE CONNECTION #################################################

# db info
DRIVER_NAME = "SQL SERVER"
SERVER_NAME = "AZ"
DATABASE_NAME = "storefv"

# connection to db sql server by ssms
conn = db.connect(f" DRIVER={{{DRIVER_NAME}}}; SERVER={SERVER_NAME}; DATABASE={DATABASE_NAME};   ")
cursor = conn.cursor()


############################################################ insert_order ##################################
def insert_order():
    root1 = TK_ORDR.Tk()
    OrderID = read.askstring("Input", "OrderID:", parent=root1)
    CustomerID = read.askstring("Input", "CustomerID:", parent=root1)
    OrderDate = read.askstring("Input", "OrderDate:", parent=root1)
    ShipppedDate = read.askstring("Input", "ShipppedDate:", parent=root1)

    cursor.execute(
        """
        INSERT INTO Orders (OrderID, CustomerID, OrderDate, ShipppedDate)
        VALUES (?, ?, ?, ?)
         """,
        (OrderID, CustomerID, OrderDate, ShipppedDate),
    )

    print("Order inserted")
    conn.commit()
    root1.mainloop()

    conn.close()

####################################################### select_orders ##########################################

def select_orders():
    root2 = TK_ORDR.Tk()
    cursor.execute("SELECT OrderID, CustomerID, OrderDate, ShipppedDate FROM Orders")

    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        for j, column_value in enumerate(row):
            label = TK_ORDR.Label(root2, text=column_value)
            label.grid(row=i, column=j)

        edit_button = TK_ORDR.Button(root2, text="Edit", command=lambda row=row: edit_order(row[0]))
        edit_button.grid(row=i, column=j + 1)
        delete_button = TK_ORDR.Button(root2, text="Delete", command=lambda row=row: delete_order(row[0]))
        delete_button.grid(row=i, column=j + 2)

    root2.mainloop()
    conn.close()

################################################### edit_order(id) ############################################


def edit_order(id):
    root3 = TK_ORDR.Tk()
    cursor.execute("SELECT OrderID, CustomerID, OrderDate, ShipppedDate FROM Orders WHERE OrderID=?", (id,))
    result = cursor.fetchone()

    OrderID = read.askstring(
        "Input", "OrderID:", parent=root3, initialvalue=result[0]
    )
    CustomerID = read.askstring(
        "Input", "CustomerID:", parent=root3, initialvalue=result[1]
    )
    OrderDate = read.askstring("Input", "OrderDate: ", parent=root3, initialvalue=result[2])
    ShipppedDate = read.askstring("Input", "ShipppedDate: ", parent=root3, initialvalue=result[3])

    cursor.execute(
        """
        UPDATE Orders
        SET OrderID=?, CustomerID=?, OrderDate=?, ShipppedDate=?
        WHERE OrderID=?
        """,
        (OrderID, CustomerID, OrderDate, ShipppedDate, id),
    )

    print("Order updated")
    conn.commit()
    root3.destroy()
    select_orders()

    conn.close()

######################################################### update_order() ######################################


def update_order():
    root3 = TK_ORDR.Tk()
    OrderID = read.askstring("Input", "OrderID:", parent=root3)
    CustomerID = read.askstring("Input", "CustomerID:", parent=root3)
    OrderDate = read.askstring("Input", "OrderDate:", parent=root3)
    ShipppedDate = read.askstring ( "Input", "ShipppedDate: ", parent=root3)

    cursor.execute(
        """
        UPDATE Orders
        SET CustomerID=?, OrderDate=?, ShipppedDate=?
        WHERE OrderID=?
        """,
        (CustomerID, OrderDate, ShipppedDate, OrderID),
    )

    print("Order updated")
    conn.commit()
    root3.mainloop()

    conn.close()

######################################################## delete_order(id) ######################################


def delete_order(id):
    root4 = TK_ORDR.Tk()
    cursor.execute(
        """
        DELETE FROM Orders
        WHERE OrderID=?
        """,
        (id,),
    )

    print("Order deleted")
    conn.commit()
    root4.destroy()
    select_orders()

    conn.close()

######################################################### delete_order() #####################################


def delete_order():
    root4 = TK_ORDR.Tk()
    OrderID = read.askstring("Input", "OrderID:", parent=root4)

    cursor.execute(
        """
        DELETE FROM Orders
        WHERE OrderID=?
        """,
        (OrderID,),
    )

    print("Order deleted")
    conn.commit()
    root4.mainloop()
    select_orders()

    conn.close()

#######################################################    CRUD    ################################################

# dashbord for crud

def btn():
    root = TK_ORDR.Tk()

    button1 = TK_ORDR.Button(
    root,
    text="Insert Order",
    command=insert_order,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="blue",
)
    button2 = TK_ORDR.Button(
    root,
    text="Read Orders",
    command=select_orders,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="green",
)
    button3 = TK_ORDR.Button(
    root,
    text="Update Order",
    command=update_order,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="yellow",
)
    button4 = TK_ORDR.Button(
    root,
    text="Delete Order",
    command=delete_order,
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


