import Tkinter as tk
import tkFileDialog as filedialog
import tkMessageBox
from api import getJSON, convertToCSV, convertToExcel, getPDF

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 400, bg = 'gray25', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Convertor', bg = 'gray25', fg='white')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


    
browseButton_JSON = tk.Button(text="      Import JSON File     ", command=getJSON, bg='medium aquamarine', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_JSON)



saveAsButton_CSV = tk.Button(text='Convert JSON to CSV', command=convertToCSV, bg='light slate blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_CSV)


saveAsButton_EXCEL = tk.Button(text='Convert JSON to Excel', command=convertToExcel, bg='pink3', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=saveAsButton_EXCEL)


compare_PDF = tk.Button(text='           Verify PDF           ', command=getPDF, bg='light slate blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 280, window=compare_PDF)

root.mainloop()