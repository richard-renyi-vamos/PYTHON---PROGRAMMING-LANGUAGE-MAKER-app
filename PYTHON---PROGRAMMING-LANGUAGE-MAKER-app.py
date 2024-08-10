import tkinter as tk
from tkinter import messagebox, scrolledtext

# Function to create a new function
def define_function():
    function_name = function_name_entry.get()
    parameters = parameters_entry.get()
    function_code = function_code_text.get("1.0", tk.END)

    if not function_name:
        messagebox.showerror("Error", "Function name is required!")
        return

    try:
        # Dynamically define the function
        exec(f"def {function_name}({parameters}):\n{function_code}", globals())
        messagebox.showinfo("Success", f"Function '{function_name}' defined successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error in function definition:\n{e}")

# Function to show help instructions
def show_help():
    help_text = (
        "Welcome to the Programming Language Maker!\n\n"
        "1. Define Function:\n"
        "- Enter the function name, parameters, and the code inside the function.\n"
        "- Click 'Define Function' to create the function.\n\n"
        "2. Help:\n"
        "- This option provides instructions on how to use the app.\n\n"
        "Note: Be careful with your syntax, as any errors in the code will result in an error message."
    )
    messagebox.showinfo("HELP", help_text)

# Create the main application window
app = tk.Tk()
app.title("Programming Language Maker")

# Function definition frame
frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

# Function name
tk.Label(frame, text="Function Name:").grid(row=0, column=0, sticky="e")
function_name_entry = tk.Entry(frame, width=30)
function_name_entry.grid(row=0, column=1)

# Parameters
tk.Label(frame, text="Parameters:").grid(row=1, column=0, sticky="e")
parameters_entry = tk.Entry(frame, width=30)
parameters_entry.grid(row=1, column=1)

# Function code
tk.Label(frame, text="Function Code:").grid(row=2, column=0, sticky="ne")
function_code_text = scrolledtext.ScrolledText(frame, width=40, height=10)
function_code_text.grid(row=2, column=1, padx=5, pady=5)

# Define function button
define_function_button = tk.Button(frame, text="Define Function", command=define_function)
define_function_button.grid(row=3, columnspan=2, pady=10)

# Menu bar
menu_bar = tk.Menu(app)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="HELP", command=show_help)
menu_bar.add_cascade(label="Help", menu=help_menu)

app.config(menu=menu_bar)

# Run the application
app.mainloop()
