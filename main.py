import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd

root = tk.Tk()
root.title("Orderbevestiging Tierra")

frame = tk.Frame(root)
frame.pack()

#Customer information labels
customer_info_frame = tk.LabelFrame(frame, text="Klant informatie")
customer_info_frame.grid(row=0, column=0, padx=20, pady=20)

company_name_label = tk.Label(customer_info_frame, text="Bedrijfsnaam")
company_name_label.grid(row=0, column=0)
address_label = tk.Label(customer_info_frame, text="Adres")
address_label.grid(row=1, column=0)
zip_code_label = tk.Label(customer_info_frame, text="Postcode")
zip_code_label.grid(row=2, column=0)
place_name_label = tk.Label(customer_info_frame, text="Plaatsnaam")
place_name_label.grid(row=3, column=0)
country_label = tk.Label(customer_info_frame, text="Land")
country_label.grid(row=4, column=0)

company_name_entry = tk.Entry(customer_info_frame)
company_name_entry.grid(row=0, column=1)
address_entry = tk.Entry(customer_info_frame)
address_entry.grid(row=1, column=1)
zip_code_entry = tk.Entry(customer_info_frame)
zip_code_entry.grid(row=2, column=1)
place_name_entry = tk.Entry(customer_info_frame)
place_name_entry.grid(row=3, column=1)
country_entry = tk.Entry(customer_info_frame)
country_entry.grid(row=4, column=1)

#Order Information 
order_info_frame = tk.LabelFrame(frame, text="Order informatie")
order_info_frame.grid(row=0, column=1, padx=20, pady=20)

order_number_label = tk.Label(order_info_frame, text="Ordernummer")
order_number_label.grid(row=0, column=0)
container_number_label = tk.Label(order_info_frame, text="Container nummer")
container_number_label.grid(row=1, column=0)
date_delivery_label = tk.Label(order_info_frame, text="Leveringsdatum")
date_delivery_label.grid(row=2, column=0)

order_number_entry = tk.Entry(order_info_frame)
order_number_entry.grid(row=0, column=1)
container_number_entry = tk.Entry(order_info_frame)
container_number_entry.grid(row=1, column=1)
date_delivery_entry = tk.Entry(order_info_frame)
date_delivery_entry.grid(row=2, column=1)


#Upload Excel file information
upload_excel_frame = tk.LabelFrame(frame, text="Prijslijst")
upload_excel_frame.grid(row=3, column=0, padx=20, pady=20)

excel_button=tk.Button(upload_excel_frame, text="Upload Excel bestand", width=20, command=lambda:upload_file())
excel_button.grid(row=0, column=0)

#Create tabs
excel_notebook = ttk.Notebook(upload_excel_frame, width=750, height=250)
excel_notebook.grid(row=2, column=0)

tierra_frame = ttk.Frame(excel_notebook, width=750, height=200)
no_label_frame = ttk.Frame(excel_notebook, width=750, height=200)
shop_in_frame = ttk.Frame(excel_notebook,width=750, height=200)

tierra_frame.pack(fill="both", expand=1)
no_label_frame.pack(fill="both", expand=1)
shop_in_frame.pack(fill="both", expand=1)

excel_notebook.add(tierra_frame, text="Tierra")
excel_notebook.add(no_label_frame, text="No-Label")
excel_notebook.add(shop_in_frame, text="Shop in Shop")

#Create treeview
excel_tree = ttk.Treeview(tierra_frame) #TODO: add scroll bar and create function for this part

def upload_file():
    excel_file = filedialog.askopenfilename(filetypes=[('xlsx files', '*.xlsx'), ('xls files', '*.xls')]) #Posibility initial directory for opening
    if excel_file:
        try:
            excel_file = r"{}".format(excel_file)
            df = pd.read_excel(excel_file) #TODO: add sheetname=None for all the sheets
        except ValueError:
            error_label.config(text="File couldn't be openend")
        except FileNotFoundError:
            error_label.config(text="File couldn't be found")
#     #clear old treeview
#     clear_tree()

#     #set up new treeview
#     excel_tree["column"] = list(df.columns)

# def clear_tree():
#     excel_tree.delete(*excel_tree.get_children())

error_label = tk.Label(root, text='')
error_label.pack(pady=20)


root.mainloop()