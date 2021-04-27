# CryptoWalletRecorder

This python script, will take your total balance, and update it into a local excel file or google sheet.

Working with a local excel file is simpler.

You will need to install the following python modules:
- pip3 install openpyxl
- pip3 install python-binance

If you want to use the Google Sheet option:need to install also:
- pip3 install gspread

Once you download the file, you will need to get Binance API (I suggest you create a new set of API keys, and restric it to read only, and limit the IP.

On the first run of the script, the default .ini file will be created. 
On the first run of the script, if excel is selected, an empty file will be created.


base_currency - enter the base currency you use.
exchange - currently only binance is supported
output_medium - select google or excel


Following options :
[EXCHANGE]
exchange = binance
base_currency = USDT
api_key = ENTER_YOUR_API_KEY_HERE
api_secret = ENTER_YOUR_SECRET_HERE

[OUTPUT]
output_medium = [google,excel]

[GOOGLE_SHEET]
service_account_file_path = D:\My Downloads\client_secret.json
file_name = spreadsheet1

[EXCEL_SHEET]
file_name = Wallet_Value.xlsx
