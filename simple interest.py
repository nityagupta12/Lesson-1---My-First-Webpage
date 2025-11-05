import tkinter as tk
from tkinter import messagebox

# Function to calculate Simple and Compound Interest
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        # Calculations
        simple_interest = (principal * rate * time) / 100
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        # Display results
        simple_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        compound_label.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create main window
window = tk.Tk()
window.title("Interest Calculator App")
window.geometry("400x350")
window.config(bg="#ccf9ff")

# Title label
title = tk.Label(window, text="💰 Interest Calculator", font=("Arial", 18, "bold"), bg="#069cb0", fg="#00796b")
title.pack(pady=15)

# Input fields
tk.Label(window, text="Principal Amount:", bg="#01626e", font=("Arial", 12)).pack()
principal_entry = tk.Entry(window, width=25)
principal_entry.pack(pady=5)

tk.Label(window, text="Rate of Interest (%):", bg="#01626e", font=("Arial", 12)).pack()
rate_entry = tk.Entry(window, width=25)
rate_entry.pack(pady=5)

tk.Label(window, text="Time Period (years):", bg="#01626e", font=("Arial", 12)).pack()
time_entry = tk.Entry(window, width=25)
time_entry.pack(pady=5)

# Calculate button
calc_button = tk.Button(window, text="Calculate", command=calculate_interest, bg="#00796b", fg="white", font=("Arial", 12, "bold"))
calc_button.pack(pady=15)

# Output labels
simple_label = tk.Label(window, text="Simple Interest: ", bg="#01626e", font=("Arial", 12, "bold"))
simple_label.pack()

compound_label = tk.Label(window, text="Compound Interest: ", bg="#01626e", font=("Arial", 12, "bold"))
compound_label.pack()

# Run the GUI loop
window.mainloop()
