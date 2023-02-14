import pypyodbc as db  # database
import tkinter as TK_PRODUCTS  # for btn and label
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
    root1 = TK_PRODUCTS.Tk()
    
    ProductID = read.askstring("Input", "ProductID:", parent=root1)
    Name = read.askstring("Input", "Name:", parent=root1)
    Color = read.askstring("Input", "Color: ", parent=root1)
    Price = read.askstring("Input", "Price: ", parent=root1)

    cursor.execute(
        """
        INSERT INTO Products (ProductID,Name, Color, Price)
        VALUES (?,?, ?, ?)
         """,
        (ProductID, Name, Color, Price),
    )

    print("Data inserted")
    conn.commit()
    root1.mainloop()
    conn.close()


####################################################### select_data ##########################################

def select_data():
    root2 = TK_PRODUCTS.Tk()
    cursor.execute("SELECT * FROM Products")

    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        for j, column_value in enumerate(row):
            label = TK_PRODUCTS.Label(root2, text=column_value)
            label.grid(row=i, column=j)

        edit_button = TK_PRODUCTS.Button(root2, text="Edit", command=lambda row=row: edit_data(row[0]))
        edit_button.grid(row=i, column=j + 1)
        delete_button = TK_PRODUCTS.Button(root2, text="Delete", command=lambda row=row: delete_datab(row[0]))
        delete_button.grid(row=i, column=j + 2)

    root2.mainloop()
    conn.close()

################################################### edit_data(id) ############################################


def edit_data(id):
    root3 = TK_PRODUCTS.Tk()
    cursor.execute("SELECT * FROM Products WHERE ProductID=?", (id,))
    result = cursor.fetchone()

    ProductID = read.askstring(
        "Input", "ProductID:", parent=root3, initialvalue=result[0]
    )
    Name = read.askstring(
        "Input", "Name:", parent=root3, initialvalue=result[1]
    )
    Color = read.askstring(
        "Input", "Color: ", parent=root3, initialvalue=result[2]
    )
    
    Price = read.askstring("Input", "Price: ", parent=root3, initialvalue=result[3])

    cursor.execute(
        """
        UPDATE Products
        SET ProductID=?, Name=?, Color=?, Price=?
        WHERE ProductID=?
        """,
        (ProductID, Name, Color, Price, id),
    )

    print("Data updated")
    conn.commit()
    root3.destroy()
    select_data()

    conn.close()

######################################################### update_data() ######################################


def update_data():
    root3 = TK_PRODUCTS.Tk()
    ProductID = read.askstring("Input", "ProductID:", parent=root3)
    Name = read.askstring("Input", "Name:", parent=root3)
    Color = read.askstring("Input", "Color: ", parent=root3)
    Price = read.askstring("Input", "Price: ", parent=root3)

    cursor.execute(
        """
        UPDATE Products
        SET Name=?, Color=?, Price=?
        WHERE ProductID=?
        """,
        (Name, Color, Price, ProductID),
    )

    print("Data updated")
    conn.commit()
    root3.mainloop()

    conn.close()

######################################################## delete_datab(id) ######################################


def delete_datab(id):
    root4 = TK_PRODUCTS.Tk()
    cursor.execute(
        """
        DELETE FROM Products
        WHERE ProductID=?
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
    root4 = TK_PRODUCTS.Tk()
    ProductID = read.askstring("Input", "ProductID:", parent=root4)

    cursor.execute(
        """
        DELETE FROM Products
        WHERE ProductID=?
        """,
        (ProductID,),
    )

    print("Data deleted")
    conn.commit()
    root4.mainloop()
    select_data()

    conn.close()

#######################################################    CRUD    ################################################

# dashbord for crud

def btn():
    root = TK_PRODUCTS.Tk()

    button1 = TK_PRODUCTS.Button(
    root,
    text="Insert data",
    command=insert_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="blue",
)
    button2 = TK_PRODUCTS.Button(
    root,
    text="read data",
    command=select_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="green",
)
    button3 = TK_PRODUCTS.Button(
    root,
    text="Update data",
    command=update_data,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="yellow",
)
    button4 = TK_PRODUCTS.Button(
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



