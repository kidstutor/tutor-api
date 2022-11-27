import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os
import pandas as pd

class Database:
    _conn = None
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            # Database.acquire_connection()
            scopes = ['https://www.googleapis.com/auth/spreadsheets',
                  'https://www.googleapis.com/auth/drive']

            keyfile_dict = {"type": "service_account",
                            "project_id": os.getenv("GOOGLE_PROJECT_ID"),
                            "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
                            "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace("\\\\", "\\"),
                            "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
                            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                            "token_uri": "https://oauth2.googleapis.com/token",
                            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                            "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
                        }

            credentials = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, 
                                                                       scopes=scopes)

            cls._conn = gspread.authorize(credentials) 
        return cls._instance

    # @staticmethod
    # def acquire_connection(self):
    #     scopes = ['https://www.googleapis.com/auth/spreadsheets',
    #               'https://www.googleapis.com/auth/drive']

    #     keyfile_dict = {"type": "service_account",
    #                     "project_id": os.getenv("GOOGLE_PROJECT_ID"),
    #                     "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
    #                     "private_key": os.getenv("GOOGLE_PRIVATE_KEY"),
    #                     "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
    #                     "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    #                     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #                     "token_uri": "https://oauth2.googleapis.com/token",
    #                     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #                     "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
    #                 }

    #     credentials = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, 
    #                                                                    scopes=scopes)

    #     self._conn = gspread.authorize(credentials) 
    #     print(self._conn)
    
    @classmethod
    def ReadData(cls, spread_sheet_name: str, sheet_name: str = 'Sheet1', filters: dict = {}) -> pd.DataFrame:
        spreadsheet = cls._conn.open(spread_sheet_name)
        worksheet = spreadsheet.worksheet(sheet_name)
        return pd.DataFrame(worksheet.get_all_records())


