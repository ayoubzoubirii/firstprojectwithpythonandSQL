import tkinter as tkdash  # for btn and label
import customers
import products
import orders
import orderdetails

root = tkdash.Tk()

def costomers () :
    customers.btn()
def  Products() :
    products.btn()
def  Ordres() :
    orders.btn()
def  Oredresdetails() :
    orderdetails.btn()

button1 = tkdash.Button(
    root,
    text="coustomers",
    command=costomers,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="blue",
)
button2 = tkdash.Button(
    root,
    text="Products",
    command=Products,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="blue",
)

button3 = tkdash.Button(
    root,
    text="Ordres",
    command=Ordres,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="blue",
)
button4 = tkdash.Button(
    root,
    text="oredres Details",
    command=Oredresdetails,
    height=3,
    width=20,
    font=("Helvetica", 20),
    bg="blue",
)

button1.pack()
button2.pack()
button3.pack()
button4.pack()


root.mainloop()