import tkinter as tk
from tkinter import filedialog
def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("image files", "*.png *.jpg"), ("All files", "*.*")])
    if file_path:
        # Process the selected file (you can replace this with your own logic)
        print("Selected file", file_path)

root = tk.Tk()
root.title('Import File Example')
# Create an &quot;Import File&quot; button
import_button = tk.Button(root, text='Import File', command=import_file)
import_button.pack(pady=100)
# Run the Tkinter event loop
root.mainloop()
