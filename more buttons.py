import tkinter as tk
from tkinter import messagebox

def info_box():
    messagebox.showinfo("Information", "Coding is really useful.")
    
def warning_box():
    messagebox.showwarning("Warning", "This is a warning message!")
    
def error_box():
    messagebox.showerror("Error", "An error has occured!")
    
def question_box():
    response = messagebox.askyesno("Question", "Do you like coding?")
    print("Response:", response)
    
def ok_cancel_box():
    response = messagebox.askokcancel("Confirm", "Do you want to proceed?")
    print("Response:", response)
    
def yes_no_box():
    response = messagebox.askyesno("Confirm", "Do you want to save changes?")
    
def retry_cancel_box():
    response = messagebox.askretrycancel("Retry", "Operation failed. Retry?")
    print("Response:", response)
    
root = tk.Tk()

root.title("Message Box Examples")

root.geometry("300x400")

# Buttons for each message box

tk.Button(root, text="Show Info", command=info_box).pack(pady=5)

tk.Button(root, text="Show Warning", command=warning_box).pack(pady=5)

tk.Button(root, text="Show Error", command=error_box).pack(pady=5)

tk.Button(root, text="Ask Question", command=question_box).pack(pady=5)

tk.Button(root, text="Ask Ok Cancel", command=ok_cancel_box).pack(pady=5)

tk.Button(root, text="Ask Yes No", command=yes_no_box).pack(pady=5)

tk.Button(root, text="Ask Retry Cancel", command=retry_cancel_box).pack(pady=5)

root.mainloop()