import gspread

from configparser import ConfigParser

file = 'CryptoWalletRecorderConfig.ini'
config = ConfigParser()
config.read(file)


from google.oauth2.service_account import Credentials
#import pandas as pd
scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file(config['GOOGLE_SHEET']['service_account_file_path'], scopes=scope)
gclient = gspread.authorize(creds)
google_sh = gclient.open(config['GOOGLE_SHEET']['file_name'])
sheet1 = google_sh.get_worksheet(0)
