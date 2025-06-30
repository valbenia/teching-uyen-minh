import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.configure(bg='lightgray')
digit = "1234567890"

# Create a simple calculator GUI
def calculate():
    try:
        num1 = entry_num1.get()
        num2 = entry_num2.get()
        operation = operation_var.get()
        evalOperations = num1 + operation + num2
        result =eval(evalOperations)
        label_result.config(text=f"Result: {result}", fg='black')
    except Exception as e:
        label_result.config(text=f"Error: Invalid input: {e}", fg='red')
        
num1_label = tk.Label(root, text="Number 1:")
num1_label.pack(pady=10)
entry_num1 = tk.Entry(root, width=20)
entry_num1.pack(pady=5)
num2_label = tk.Label(root, text="Number 2:")
num2_label.pack(pady=10)
entry_num2 = tk.Entry(root, width=20)
entry_num2.pack(pady=5)
operation_var = tk.StringVar(value='+')
operation_frame = tk.Frame(root)
operation_frame.pack(pady=10)
for op in ['+', '-', '*', '/']:
    radio_button = tk.Radiobutton(operation_frame, text=op, variable=operation_var, value=op)
    radio_button.pack(side=tk.LEFT, padx=5)
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=20)
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

# Add a button to exit the application
exit_button = tk.Button(root, text="Exit", command=root.quit)  
exit_button.pack(pady=20)
# Start the main loop
root.mainloop()

# invoke the method
# extract method, variable, and class
# try -> except
# RaidioButton
# Checkbutton
# Frame