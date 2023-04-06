import argparse
import pathlib
import pandas as pd

def extract_sheets(file_path):
    ''' Extracts the different excel sheets (Tierra, No-label, Shop in Shop) 
        from the price list and removes unnamed columns '''
    for excel_file in file_path:
        order_list = pd.read_excel(excel_file, sheet_name=None)
        
        tierra = order_list['Tierra Outdoor'] 
        tierra = tierra[tierra.filter(regex='^(?!Unnamed)').columns] #removes unnamed columns from tierra price list
        nolabel = order_list['No-Label']
        shop_in = order_list['Shop in Shop']
    return tierra, nolabel, shop_in

def tierra_product():
    pass

def no_label_product():
    pass

def shop_in_product():
    pass

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-i', '--input', type=pathlib.Path, 
                        default=[], nargs='+', help='Filepath to price list excel file ')
    argument_parser.add_argument('-o', '--output', type=pathlib.Path, 
                        default=[], nargs='+', help='Filepath to output directory')
    args = argument_parser.parse_args()
    xlsx_sheets = extract_sheets(file_path=args.input)
    print(xlsx_sheets)
 