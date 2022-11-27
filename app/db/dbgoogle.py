import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os
import pandas as pd

class GoogleSheet:
    _conn = None
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(__class__, cls).__new__(cls)
            scopes = ['https://www.googleapis.com/auth/spreadsheets',
                  'https://www.googleapis.com/auth/drive']

            keyfile_dict = {"type": "service_account",
                            "project_id": os.getenv("GOOGLE_PROJECT_ID"),
                            "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
                            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQD0JqXuMLxaqaFN\n+UEaza8FLdnziQJ8fkWAVYvX4co8bzO5tWemyBhsXPKVOJt+neR1eQRfvYPpSgxr\nrr86+Ll4jgeKb16+jTTkKbUADUAIUjIWvvJtlhGkYeJLANfvi8+/+rcs4Mlpgofe\nTrNXWHS9g3oueSOYAAf0pCfRFfjnmr+lLs5GAznzfl5Bfh+ufy8CN3a6yY3SspUd\nsPk3MDkWq5YCn8yacj0cDwSbD28GUMDPRC1kvqqRClPUcezO/ehhEdyK97fGIXtU\nYns9scQ+wtCExXlUkKypCDNHuS4eoX9Ba7gbaT+9ipxh2pqLtopq+TffZCXkv6ms\nojaBveJjAgMBAAECggEAHokA4q/ktsAVZP+iBVypIZAw/JTroy9VuO26Djd2iCVu\nRjEqdAD9kPv0+PW5+NV9f7WxdtnoeBJjSEp0L0dxRuMYjVdNda6KaWjP8uA1XHUP\nP6oE/vCwZys41qGV4CdPxdZw92NrvU7ueD7GjkuJWjRp4QsUiQuj8xReyHcjiK+i\n8AvN42fTrRpv/BCBZJtIQu9VLxUp8h6XngZRH8SZkHUglFNiCGK3Mi5JtJ28TEXt\nTaUxBzxEv8Rf+CYB+F3vnLFnJ75WD/ArQQ10xzlyjTAU2TbXbyb3SozlV+t8iSn1\nAqAyvA4d5qXGhb95V2f3boM+/EL2MBEVOhX4+a3LeQKBgQD/zVG5WPLV+v8wpZjU\nKovb70FaH9E5gBauilWjHtnsraY8evMM2wroqXioZe9EpBLYvHUdy1dSRdTY7Hvz\nr0tcvBC42/QKxnL9wxY/24clj24SAHu5+08wSw8BgP/4Ih84OKdTV3Ms64Q0lOEj\nwP5mIvK+KTYVHGN6VeK/7ezLWwKBgQD0VwVDzMs1C6eTOZcy1oZPdbt35s7h7G33\nJBeCcWv6tA1EHw/C9M3VYUjsAavfbLaifAROuRyC8O0vLmw/isw8MyUH2cG702be\nGfNVPRYHX4bnLDSdIh4JzfPzXPlxTva9Q3p4RzDO6XWyyj3gdNHB+gQGEmGF86fu\nVonlnv1bmQKBgQDSoXIFuKRcZgzzNageK9p2AxBA8aoKOtpyZh4V7zVqmaIkcujn\nUQYuhj2ADE90qdWK+cNGAUWpzS5yYGfARDs95O2wCg1tQfM12QndExq5Zt0vnY5D\nmheeoG9+wYYD/7TNSnkdOwjvmA6IbX7lPek8mNJgmvaZc4LGHSpU98jfuQKBgQDs\nHnvz/SASbuTNnUXD1xOMDhXP1LfwE25g+fvODpVufDilr+6nU7LllVHG4Aabro7/\njiELgk9PKkvK4G2zKgob0sDiSUiynaQ21ZUUtidnkKTpGQrvHl0w1Fn+v8Y9/TTr\nyR28xe8gxPL8h/wrwDhD37ursm+T5tZNuEsiHvZvYQKBgQC2s0PwsnW5SWvqEDZ+\noGZW9oibL8vLkRvm8ZRHeeKWVNNAwo02VM/3FFS7mfyIUmwiZ7u1F6kJERyphv85\naZvsIFg5GjYG513BwDbxf5kdQoCnfy+8eJABty4jQN1i5qpGYuj6ivgLiM+9WZRD\nZ/BT1tO8h4HCMXjp7HKbj24mxQ==\n-----END PRIVATE KEY-----\n",
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
    
    @classmethod
    def ReadData(cls, spread_sheet_name: str, sheet_name: str = 'Sheet1', filters: dict = {}) -> pd.DataFrame:
        spreadsheet = cls._conn.open(spread_sheet_name)
        worksheet = spreadsheet.worksheet(sheet_name)
        df = pd.DataFrame(worksheet.get_all_records())
        for key in filters:
            if key in df.columns:
                df = df[df[key] == filters[key]]
        return df


