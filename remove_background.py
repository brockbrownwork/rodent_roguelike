from rembg import remove
from tkinter import Tk, filedialog
import os

def remove_background(input_path):
    output_path = input_path.rsplit('.', 1)[0] + '_no_background.' + input_path.rsplit('.', 1)[1]

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input_data = i.read()
            output = remove(input_data)
            o.write(output)
    print(f"Background removed. Output saved as: {output_path}")

def select_file():
    root = Tk()
    root.withdraw()  # to hide the main window
    current_directory = os.getcwd()
    file_path = filedialog.askopenfilename(initialdir=current_directory)
    if file_path:
        remove_background(file_path)
    else:
        print("No file selected.")

select_file()
