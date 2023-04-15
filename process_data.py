import pandas as pd


def extract_product(excel_file):
    '''Extracts excel sheets and returns selected products '''
    order_list = pd.read_excel(excel_file, sheet_name=None)
    tierra = order_list['Tierra Outdoor'] 
    tierra = tierra[tierra.filter(regex='^(?!Unnamed)').columns] #removes unnamed columns from tierra price list
    tierra_total = tierra.iloc[-1]
  
    tierra = tierra.drop(tierra.columns[[1, 4, 5, 7]], axis=1) #removes unwanted columns
    tierra = tierra.dropna(subset=tierra.columns[4])
    tierra.loc[-1] = tierra_total
    tierra.fillna('', inplace=True) 
    no_label = order_list['No-Label']
    new_header = no_label.iloc[0] #create new header
    no_label = no_label[1:] #take the data less the header row
    no_label.columns = new_header #set the header row as the df header
    no_label = no_label.drop(no_label.columns[[1, 4, 5]], axis=1)
    no_label = no_label.dropna(subset=no_label.columns[4])

    shop_in = order_list['Shop in Shop']
    shop_in = shop_in.drop(shop_in.columns[[1, 4]], axis=1)
    shop_in = shop_in.dropna(subset=shop_in.columns[4])

    return tierra, no_label, shop_in

