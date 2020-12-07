import Tkinter as tk
import tkFileDialog as filedialog
import tkMessageBox
import pandas as pd
import fitz 

#df = pd.read_json ('C://info/data.json', )
#export_csv = df.to_csv ('C://info/Newdata.csv', index = None)
#export_excel = df.to_excel('C://info/Newdata.xlsx')


def getJSON ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_json (import_file_path)

def convertToCSV ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None, header=True)


def convertToExcel ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    read_file.to_excel (export_file_path, index = None, header=True)


    
def getPDF ():
    
    import_file_path = filedialog.askopenfilename()
    text = ""

    doc = fitz.open(import_file_path)
    for page in doc:
        text += page.getText()

    if len(text) > 0:
        tkMessageBox.showinfo(message="The PDF contains text", title="PDF TYPE")
    else:
        tkMessageBox.showinfo(message="The PDF is scanned", title="PDF TYPE")