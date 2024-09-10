import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

#defining file names
def extract_data(file_path):
    folder_name = os.path.basename(os.path.dirname(file_path))
    file_name = os.path.basename(file_path)

#reading .sp file

    with open(file_path, 'r') as file:
            lines = file.readlines()

#extracting specific data from specific line
    for line in lines:
        if line.startswith('410.000000'):
            data_410 = float(line.split()[-1])
        elif line.startswith('450.000000'):
            data_450 = float(line.split()[-1])

    return folder_name, file_name, data_410, data_450

#processing an entire folder
def process_folder(folder_path):
    data = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.sp'):
                file_path = os.path.join(root, file)
                folder_name, file_name, data_410, data_450 = extract_data(file_path)
                data.append({
                    'folder name': folder_name,
                    'file name': file_name,
                    '410': data_410,
                    '450': data_450
                })

    df = pd.DataFrame(data)
    return df

#saving dataframe to excel
def save_to_excel(dataframe, output_path):
    dataframe.to_excel(output_path, index=False)
    messagebox.showinfo("Success", f"Data successfully saved to {output_path}")

#folder selection for GUI
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        df = process_folder(folder_selected)
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if save_path:
            save_to_excel(df, save_path)


#Creating GUI window
root = tk.Tk()
root.title("Data Extractor")

select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

root.mainloop()
