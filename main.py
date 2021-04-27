#https://www.codeforests.com/2020/11/22/gspread-read-write-google-sheet/

import json
import datetime
currDate = datetime.datetime.now().date()

from configparser import ConfigParser
config = ConfigParser()

import os
# verify config file exists. if not create it
file = 'CryptoWalletRecorderConfig.ini'

if os.path.isfile('./' + file) == False:
    # create initial Config file
    print('config file is missing - creating')
    config.add_section('EXCHANGE')
    config.set('EXCHANGE', 'exchange', 'binance')
    config.set('EXCHANGE', 'base_currency', 'USDT')
    config.set('EXCHANGE', 'api_key', '')
    config.set('EXCHANGE', 'api_secret', '')
    config.add_section('OUTPUT')
    config.set('OUTPUT', 'output_medium', 'excel')
    config.add_section('GOOGLE_SHEET')
    config.set('GOOGLE_SHEET', 'service_account_file_path', 'D:\My Downloads\client_secret.json')
    config.set('GOOGLE_SHEET', 'file_name', 'spreadsheet1')
    config.add_section('EXCEL_SHEET')
    config.set('EXCEL_SHEET', 'file_name', 'Wallet_Value.xlsx')

    with open(file, 'w') as configFile:
        config.write(configFile)
    # TODO: need user input for missing values.

config.read(file)

# First run - check if CryptoWalletRecorderConfig.ini file exists

BASE_CURRENCY = config['EXCHANGE']['base_currency']
API_KEY = config['EXCHANGE']['api_key']
API_SECRET = config['EXCHANGE']['api_secret']

from binance.client import Client
client = Client(API_KEY, API_SECRET)
clientData = client.get_account()

wallet_value = 0
#get all account current assets
currentAssets = clientData['balances']

#get latest trade prices
lastTradePrices = client.get_all_tickers()

for currentAsset in currentAssets:
    if float(currentAsset['free']) > 0:
        if currentAsset['asset'] == BASE_CURRENCY:
            wallet_value += float(currentAsset['free'])
        for lastTradePrice in lastTradePrices:
            if lastTradePrice['symbol'] == currentAsset['asset']+BASE_CURRENCY:
                wallet_value += (float(currentAsset['free'])*float(lastTradePrice['price']))

### output Section
### output to Google Sheet
if config['OUTPUT']['output_medium'] == 'google':
    from output_google_sheet import sheet1
    newRow = len(sheet1.col_values(1))+1
    sheet1.update_cell(newRow,1, str(datetime.datetime.now()))
    sheet1.update_cell(newRow,2, str(wallet_value))
    sheet1.update_cell(newRow,3, BASE_CURRENCY)

### output to Local excel
elif config['OUTPUT']['output_medium'] == 'excel':
    import openpyxl

    loc = (config['EXCEL_SHEET']['file_name'])
    # To open Workbook
    wb = openpyxl.load_workbook(filename=loc)
    ws = wb.active

    ws.append([str(datetime.datetime.now()), str(wallet_value), BASE_CURRENCY])
    wb.save(filename=loc)

