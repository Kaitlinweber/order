import tkinter as tk
from tkinter import ttk, filedialog
#import pandas as pd
# import numpy as np
import process_data

root = tk.Tk()
root.title("Orderbevestiging Tierra Outdoor")

frame = tk.Frame(root)
frame.pack()

#General informatuon frame
general_frame = tk.LabelFrame(frame, borderwidth=0, highlightthickness=0)
general_frame.grid(row=0, column=0, padx=20, pady=20)

#Customer information labels
customer_info_frame = tk.LabelFrame(general_frame, text="Klant informatie")
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
order_info_frame = tk.LabelFrame(general_frame, text="Order informatie")
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
excel_notebook = ttk.Notebook(upload_excel_frame, width=850, height=250)
excel_notebook.grid(row=2, column=0)

tierra_frame = ttk.Frame(excel_notebook, width=850, height=250)
no_label_frame = ttk.Frame(excel_notebook, width=850, height=250)
shop_in_frame = ttk.Frame(excel_notebook, width=850, height=250)

tierra_frame.pack(fill="both", expand=1)
no_label_frame.pack(fill="both", expand=1)
shop_in_frame.pack(fill="both", expand=1)

excel_notebook.add(tierra_frame, text="Tierra Outdoor")
excel_notebook.add(no_label_frame, text="No-Label")
excel_notebook.add(shop_in_frame, text="Shop in Shop")

#Create scrollbar  #TODO: class van scrollbar maken 
scrollbary_tierra = ttk.Scrollbar(tierra_frame)
scrollbary_tierra.pack(side="right", fill="y") 
scrollbarx_tierra = ttk.Scrollbar(tierra_frame, orient="horizontal")
scrollbarx_tierra.pack(side="bottom", fill="x")

scrollbary_no_label = ttk.Scrollbar(no_label_frame)
scrollbary_no_label.pack(side="right", fill="y") 
scrollbarx_no_label = ttk.Scrollbar(no_label_frame, orient="horizontal")
scrollbarx_no_label.pack(side="bottom", fill="x")

scrollbary_shop_in = ttk.Scrollbar(shop_in_frame)
scrollbary_shop_in.pack(side="right", fill="y") 
scrollbarx_shop_in = ttk.Scrollbar(shop_in_frame, orient="horizontal")
scrollbarx_shop_in.pack(side="bottom", fill="x")

#Create treeview
tierra_tree = ttk.Treeview(tierra_frame, yscrollcommand=scrollbary_tierra.set, xscrollcommand=scrollbarx_tierra.set) #TODO: add scroll bar 
no_label_tree = ttk.Treeview(no_label_frame, yscrollcommand=scrollbary_no_label.set, xscrollcommand=scrollbarx_no_label.set)
shop_in_tree = ttk.Treeview(shop_in_frame, yscrollcommand=scrollbary_shop_in.set, xscrollcommand=scrollbarx_shop_in.set)

#Configure scrollbar
scrollbary_tierra.config(command=tierra_tree.yview)
scrollbarx_tierra.config(command=tierra_tree.xview)

scrollbary_no_label.config(command=no_label_tree.yview)
scrollbarx_no_label.config(command=no_label_tree.xview)

scrollbary_shop_in.config(command=shop_in_tree.yview)
scrollbarx_shop_in.config(command=shop_in_tree.xview)

def upload_file():
    excel_file = filedialog.askopenfilename(filetypes=[('xlsx files', '*.xlsx'), ('xls files', '*.xls')]) #Posibility initial directory for opening
    if excel_file:
        try:
            excel_file = r"{}".format(excel_file) 
            df_tierra, df_no_label, df_shop_in = process_data.extract_product(excel_file)
        except ValueError:
            error_label.config(text="File couldn't be openend")
        except FileNotFoundError:
            error_label.config(text="File couldn't be found")
        
    #clear old treeview
    clear_tree(tierra_tree)
    clear_tree(no_label_tree)
    clear_tree(shop_in_tree)

    #set up tree
    set_up_treeview(tierra_tree, df_tierra)
    set_up_treeview(no_label_tree, df_no_label)
    set_up_treeview(shop_in_tree, df_shop_in)


def clear_tree(excel_tree):
    excel_tree.delete(*excel_tree.get_children())
    

def set_up_treeview(excel_tree, df):
    excel_tree["column"] = list(df.columns)
    excel_tree["show"] = "headings"

    for column in excel_tree["column"]:
        excel_tree.heading(column, text=column)
       
    #put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        excel_tree.insert("", "end", values=row)

    #TODO: change color : last row (total)
    excel_tree.pack()

    #set tree style
    style = ttk.Style()
    style.configure("Treeview.Heading", rowheight=50)
    style.configure("Treeview", rowheight=25)
    
    


error_label = tk.Label(root, text='')
error_label.pack(pady=20)

#Function for number
def number():
    try:
        float(general_discount.get())
        test_answer.config(text="")
    except ValueError:
        test_answer.config(text="De korting moet een getal zijn, \n decimaal aangeven met punt")

#Create discount frame 
discount_frame = tk.LabelFrame(frame, text="Korting")
discount_frame.grid(row=4, column=0, padx=20, pady=20)

general_discount_label = tk.Label(discount_frame, text="Algemene korting")
general_discount_label.grid(row=0, column=0)

general_discount = tk.Entry(discount_frame)
general_discount.grid(row=0, column=1)

discount_button = tk.Button(discount_frame, text="Update prijslijst met korting", command=number)
discount_button.grid(row=0, column=2)

test_answer = tk.Label(discount_frame, text='')
test_answer.grid(row=1, column=1)

root.mainloop()
