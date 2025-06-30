# import tkinter as tk

# def button_click():
#     global click_count
#     click_count += 1
#     label.config(text=f"Button clicked {click_count} times!")

# root = tk.Tk()
# root.title("My First GUI")
# root.geometry("400x300")
# root.configure(bg='gray')
# label = tk.Label(root, text="Hello, Tkinter!", bg='#ADEBB3', fg='#000000', font=('Arial', 16))
# label.pack(pady=20, padx=20)

# create a button that counts clicks
# def button_click():
#     global click_count
#     click_count += 1
#     label.config(text=f"Button clicked {click_count} times!")
# click_count = 0
# button = tk.Button(root, text="Click Me!", command=button_click, bg='#FF5733', fg='#FFFFFF', font=('Arial', 12, 'bold'))
# example of button styling with border radius and hover effects
# button.pack(pady=40, padx=20)

# button = tk.Button(root, text="Click Me!", command=button_click, bg='#FF5733', fg='#FFFFFF', font=('Arial', 12, 'bold'))
# button.pack(pady=40, padx=20)
# button.configure(bg='#FF5733', fg='#FFFFFF', font=('Arial', 12, 'bold'))
# button.bind("<Enter>", lambda e: button.configure(bg='#FF8D1A'))
# button.bind("<Leave>", lambda e: button.configure(bg='#FF5733'))
# button.bind("<Button-1>", lambda e: print("Button pressed!"))
# button.bind("<ButtonRelease-1>", lambda e: print("Button released!"))
# button.bind("<Double-Button-1>", lambda e: print("Button double-clicked!"))

# import tkinter as tk 
# def greet_user(): 
#     name = name_entry.get() 
#     greeting_label.config(text=f"Hello, {name}!") 
# root = tk.Tk() 
# tk.Label(root, text="Enter your name:").pack(pady=5) 
# name_entry = tk.Entry(root, width=30) 
# name_entry.pack(pady=5) 
# greet_button = tk.Button(root, text="Greet", command=greet_user) 
# greet_button.pack(pady=5) 
# greeting_label = tk.Label(root, text="") 
# greeting_label.pack(pady=10) 
# root.title("Greeting App")
# root.geometry("300x200")
# root.configure(bg='lightblue')
# root.mainloop()

# import tkinter as tk 
# from tkinter import messagebox, filedialog

# filename = ""  # Initialize filename variable
# def show_info(): 
#     messagebox.showinfo("Info", "This is an info message") 
# def open_file(): 
#     filename = filedialog.askopenfilename() 

# root = tk.Tk() 
# menubar = tk.Menu(root) 
# file_menu = tk.Menu(menubar, tearoff=0) 
# menubar.add_cascade(label="File", menu=file_menu) 
# file_menu.add_command(label="Open", command=open_file) 
# file_menu.add_separator() 
# file_menu.add_command(label="Exit", command=root.quit)
# help_menu = tk.Menu(menubar, tearoff=0) 
# menubar.add_cascade(label="Help", menu=help_menu) 
# help_menu.add_command(label="About", command=show_info) 
# root.mainloop() 

import tkinter as tk 
root = tk.Tk()
root.geometry("1200x800")
root.title("Text Widget Example")
root.configure(bg='lightgray')

text_frame = tk.Frame(root) 
text_frame.pack(expand=1) 
# text_frame.pack_propagate(0)  # Prevent frame from resizing to fit text widget
text_frame.config(height=200, width=400)  # Set fixed size for the frame
text_frame.configure(bg='lightblue')  # Set background color for the frame
label = tk.Label(text_frame, text= "Label Example", padx=10, pady=10, bg='lightgreen', fg='black', font=('Arial', 14))
label.pack(pady=10)  # Add some padding around the label
# text_widget = tk.Text(text_frame, wrap=tk.WORD)
# scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_widget.yview) 
# text_widget.configure(yscrollcommand=scrollbar.set) 
# text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1) 
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y) 
root.mainloop()