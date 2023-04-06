import tkinter as tk

window = tk.Tk()
window.title("Orderbevestiging Tierra")

frame = tk.Frame(window)
frame.pack()

#Customer information labels
customer_info_frame = tk.LabelFrame(frame, text="Klant informatie")
customer_info_frame.grid(row=0, column=0)

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


#Customer information entries
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

#Order Information labels 
order_info_frame = tk.LabelFrame(frame, text="Order informatie")
order_info_frame.grid(row=0, column=1)

order_number_label = tk.Label(order_info_frame, text="Ordernummer")
order_number_label.grid(row=0, column=0)
container_number_label = tk.Label(order_info_frame, text="Container nummer")
container_number_label.grid(row=1, column=0)
date_delivery_label = tk.Label(order_info_frame, text="Leveringsdatum")
date_delivery_label.grid(row=2, column=0)

#Order information entries
order_number_entry = tk.Entry(order_info_frame)
order_number_entry.grid(row=0, column=1)
container_number_entry = tk.Entry(order_info_frame)
container_number_entry.grid(row=1, column=1)
date_delivery_entry = tk.Entry(order_info_frame)
date_delivery_entry.grid(row=2, column=1)


window.mainloop()