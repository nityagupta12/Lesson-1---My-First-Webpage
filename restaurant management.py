import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Restaurant Management")
root.geometry("500x500")
#menu and prices
menu = {
    "Pasta" : 250.75,
    "Pizza" : 279.83,
    "Foccacia" : 35.02,
    "Coca Cola" : 5.07,
    "Truffle" : 817.17
}
#Store Variables
variables = {}
quantities = {}
#title
tk.Label(root, text="Restaurant Menu", font=('Arial', 18, 'bold')).pack(pady=10)
#menu UI
menu_frame = tk.Frame(root)
menu_frame.pack()
for item, price in menu.items():
    var = tk.IntVar()
    qty = tk.StringVar(value="0")
    variables[item] = var
    quantities[item] = qty
    
    frame = tk.Frame(menu_frame)
    frame.pack(anchor="w", padx=20)
    
    tk.Checkbutton(frame, text=f"{item} - AED{price}", variable=var).pack(side="left")
    tk.Entry(frame,width=5, textvariable=qty).pack(side="left", padx=10)
#calculate bill
def calculate_total():
    total=0
    order_details = ""
    for item in menu:
        if variables[item].get() == 1:
            try:
                qty = int(quantities[item].get())
                if qty < 0:
                    raise ValueError
                price = menu[item] * qty
                total += price
                order_details += f"{item} x {qty} = AED{price}\n"
            except ValueError:
                messagebox.showerror("Invaild Input", f"Enter a valid quantity for {item}")
                return
    if total == 0:
        messagebox.showinfo("No Selection", "Please select at least one item")
    else:
        messagebox.showinfo("Bill", f"{order_details}\nTotal = AED{total}")
#button
tk.Button(root, text = "Generate Bill", command=calculate_total,bg="black", fg="white",font=('Arial', 12)).pack(pady=20)
root.mainloop()
    
    
            