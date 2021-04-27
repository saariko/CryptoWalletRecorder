# Writing to an excel
import openpyxl
from configparser import ConfigParser

file = 'CryptoWalletRecorderConfig.ini'
config = ConfigParser()
config.read(file)

# Give the location of the file
loc = (config['EXCEL_SHEET']['file_name'])

try:
    wb = openpyxl.load_workbook(filename = loc)
except FileNotFoundError:
    # File does not exist - first run - create default file
    # Workbook is created
    wb = openpyxl.Workbook()
    # add_sheet is used to create sheet.
    ws1 = wb.active
    ws1.title = 'Sheet 1'
    ws1['A1'] = 'Date'
    ws1['B1'] = 'Wallet Value'
    ws1['C1'] = 'Base Currency'

    #    wb.save(config['EXCEL_SHEET']['file_name']+'.xls')
    wb.save(filename=loc)

else:
    print('No exception occurred')


