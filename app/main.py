from fastapi import FastAPI
import pandas as pd
# from db.dbutils import Database as db
from app.entity.student import Student as Student
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

@app.get("/")
def read_root():
    return {"Welcome": "Root"}

@app.get("/groups")
async def get_groups() -> dict:
    # groups = meta.GetGroups()
    groups = ['a', 'b', 'c']
    return {"data" : groups}

@app.get("/students")
async def get_students() -> dict:
    s = Student()
    students = s.GetStudents()
    return {"data": students}

def main():
    scopes = ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']

    #access the json key you downloaded earlier           
    # credentials = ServiceAccountCredentials.from_json_keyfile_name("tutorkids.json", scopes) 

    # keyfile_dict = {"type": "service_account",
    #                 "project_id": os.getenv("GOOGLE_PROJECT_ID", "tutorkids"),
    #                 "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID", "4a64c8e30160bb364e5fad158706f26f595e8941"),
    #                 "private_key": os.getenv("GOOGLE_PRIVATE_KEY", "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQD0JqXuMLxaqaFN\n+UEaza8FLdnziQJ8fkWAVYvX4co8bzO5tWemyBhsXPKVOJt+neR1eQRfvYPpSgxr\nrr86+Ll4jgeKb16+jTTkKbUADUAIUjIWvvJtlhGkYeJLANfvi8+/+rcs4Mlpgofe\nTrNXWHS9g3oueSOYAAf0pCfRFfjnmr+lLs5GAznzfl5Bfh+ufy8CN3a6yY3SspUd\nsPk3MDkWq5YCn8yacj0cDwSbD28GUMDPRC1kvqqRClPUcezO/ehhEdyK97fGIXtU\nYns9scQ+wtCExXlUkKypCDNHuS4eoX9Ba7gbaT+9ipxh2pqLtopq+TffZCXkv6ms\nojaBveJjAgMBAAECggEAHokA4q/ktsAVZP+iBVypIZAw/JTroy9VuO26Djd2iCVu\nRjEqdAD9kPv0+PW5+NV9f7WxdtnoeBJjSEp0L0dxRuMYjVdNda6KaWjP8uA1XHUP\nP6oE/vCwZys41qGV4CdPxdZw92NrvU7ueD7GjkuJWjRp4QsUiQuj8xReyHcjiK+i\n8AvN42fTrRpv/BCBZJtIQu9VLxUp8h6XngZRH8SZkHUglFNiCGK3Mi5JtJ28TEXt\nTaUxBzxEv8Rf+CYB+F3vnLFnJ75WD/ArQQ10xzlyjTAU2TbXbyb3SozlV+t8iSn1\nAqAyvA4d5qXGhb95V2f3boM+/EL2MBEVOhX4+a3LeQKBgQD/zVG5WPLV+v8wpZjU\nKovb70FaH9E5gBauilWjHtnsraY8evMM2wroqXioZe9EpBLYvHUdy1dSRdTY7Hvz\nr0tcvBC42/QKxnL9wxY/24clj24SAHu5+08wSw8BgP/4Ih84OKdTV3Ms64Q0lOEj\nwP5mIvK+KTYVHGN6VeK/7ezLWwKBgQD0VwVDzMs1C6eTOZcy1oZPdbt35s7h7G33\nJBeCcWv6tA1EHw/C9M3VYUjsAavfbLaifAROuRyC8O0vLmw/isw8MyUH2cG702be\nGfNVPRYHX4bnLDSdIh4JzfPzXPlxTva9Q3p4RzDO6XWyyj3gdNHB+gQGEmGF86fu\nVonlnv1bmQKBgQDSoXIFuKRcZgzzNageK9p2AxBA8aoKOtpyZh4V7zVqmaIkcujn\nUQYuhj2ADE90qdWK+cNGAUWpzS5yYGfARDs95O2wCg1tQfM12QndExq5Zt0vnY5D\nmheeoG9+wYYD/7TNSnkdOwjvmA6IbX7lPek8mNJgmvaZc4LGHSpU98jfuQKBgQDs\nHnvz/SASbuTNnUXD1xOMDhXP1LfwE25g+fvODpVufDilr+6nU7LllVHG4Aabro7/\njiELgk9PKkvK4G2zKgob0sDiSUiynaQ21ZUUtidnkKTpGQrvHl0w1Fn+v8Y9/TTr\nyR28xe8gxPL8h/wrwDhD37ursm+T5tZNuEsiHvZvYQKBgQC2s0PwsnW5SWvqEDZ+\noGZW9oibL8vLkRvm8ZRHeeKWVNNAwo02VM/3FFS7mfyIUmwiZ7u1F6kJERyphv85\naZvsIFg5GjYG513BwDbxf5kdQoCnfy+8eJABty4jQN1i5qpGYuj6ivgLiM+9WZRD\nZ/BT1tO8h4HCMXjp7HKbj24mxQ==\n-----END PRIVATE KEY-----\n"),
    #                 # "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQD0JqXuMLxaqaFN\n+UEaza8FLdnziQJ8fkWAVYvX4co8bzO5tWemyBhsXPKVOJt+neR1eQRfvYPpSgxr\nrr86+Ll4jgeKb16+jTTkKbUADUAIUjIWvvJtlhGkYeJLANfvi8+/+rcs4Mlpgofe\nTrNXWHS9g3oueSOYAAf0pCfRFfjnmr+lLs5GAznzfl5Bfh+ufy8CN3a6yY3SspUd\nsPk3MDkWq5YCn8yacj0cDwSbD28GUMDPRC1kvqqRClPUcezO/ehhEdyK97fGIXtU\nYns9scQ+wtCExXlUkKypCDNHuS4eoX9Ba7gbaT+9ipxh2pqLtopq+TffZCXkv6ms\nojaBveJjAgMBAAECggEAHokA4q/ktsAVZP+iBVypIZAw/JTroy9VuO26Djd2iCVu\nRjEqdAD9kPv0+PW5+NV9f7WxdtnoeBJjSEp0L0dxRuMYjVdNda6KaWjP8uA1XHUP\nP6oE/vCwZys41qGV4CdPxdZw92NrvU7ueD7GjkuJWjRp4QsUiQuj8xReyHcjiK+i\n8AvN42fTrRpv/BCBZJtIQu9VLxUp8h6XngZRH8SZkHUglFNiCGK3Mi5JtJ28TEXt\nTaUxBzxEv8Rf+CYB+F3vnLFnJ75WD/ArQQ10xzlyjTAU2TbXbyb3SozlV+t8iSn1\nAqAyvA4d5qXGhb95V2f3boM+/EL2MBEVOhX4+a3LeQKBgQD/zVG5WPLV+v8wpZjU\nKovb70FaH9E5gBauilWjHtnsraY8evMM2wroqXioZe9EpBLYvHUdy1dSRdTY7Hvz\nr0tcvBC42/QKxnL9wxY/24clj24SAHu5+08wSw8BgP/4Ih84OKdTV3Ms64Q0lOEj\nwP5mIvK+KTYVHGN6VeK/7ezLWwKBgQD0VwVDzMs1C6eTOZcy1oZPdbt35s7h7G33\nJBeCcWv6tA1EHw/C9M3VYUjsAavfbLaifAROuRyC8O0vLmw/isw8MyUH2cG702be\nGfNVPRYHX4bnLDSdIh4JzfPzXPlxTva9Q3p4RzDO6XWyyj3gdNHB+gQGEmGF86fu\nVonlnv1bmQKBgQDSoXIFuKRcZgzzNageK9p2AxBA8aoKOtpyZh4V7zVqmaIkcujn\nUQYuhj2ADE90qdWK+cNGAUWpzS5yYGfARDs95O2wCg1tQfM12QndExq5Zt0vnY5D\nmheeoG9+wYYD/7TNSnkdOwjvmA6IbX7lPek8mNJgmvaZc4LGHSpU98jfuQKBgQDs\nHnvz/SASbuTNnUXD1xOMDhXP1LfwE25g+fvODpVufDilr+6nU7LllVHG4Aabro7/\njiELgk9PKkvK4G2zKgob0sDiSUiynaQ21ZUUtidnkKTpGQrvHl0w1Fn+v8Y9/TTr\nyR28xe8gxPL8h/wrwDhD37ursm+T5tZNuEsiHvZvYQKBgQC2s0PwsnW5SWvqEDZ+\noGZW9oibL8vLkRvm8ZRHeeKWVNNAwo02VM/3FFS7mfyIUmwiZ7u1F6kJERyphv85\naZvsIFg5GjYG513BwDbxf5kdQoCnfy+8eJABty4jQN1i5qpGYuj6ivgLiM+9WZRD\nZ/BT1tO8h4HCMXjp7HKbj24mxQ==\n-----END PRIVATE KEY-----\n",
    #                 "client_email": os.getenv("GOOGLE_CLIENT_EMAIL", "svctutor@tutorkids.iam.gserviceaccount.com"),
    #                 "client_id": os.getenv("GOOGLE_CLIENT_ID", "109753320455854966616"),
    #                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #                 "token_uri": "https://oauth2.googleapis.com/token",
    #                 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #                 "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL", "https://www.googleapis.com/robot/v1/metadata/x509/svctutor%40tutorkids.iam.gserviceaccount.com")
    #                }

    keyfile_dict = {"type": "service_account",
                    "project_id": os.getenv("GOOGLE_PROJECT_ID"),
                    "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
                    "private_key": os.getenv("GOOGLE_PRIVATE_KEY"),
                    "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
                    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                    "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
                   }

    credentials = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, 
                                                                   scopes=scopes)

    # authenticate the JSON key with gspread
    file = gspread.authorize(credentials) 

    #open sheet
    sheet = file.open("students")
    # sheet = sheet.sheet1

    sheet = sheet.worksheet('Sheet1')

    print("all records")
    print('************')
    df = pd.DataFrame(sheet.get_all_records())
    print(df)
    print("***************************************************************************")



    all_cells = sheet.range('A1:C6')
    print("All cells")
    print("*********")
    print(all_cells)
    print("***************************************************************************")
    
    print("Cell Values in a for loop")
    print("**************************")
    for cell in all_cells:
        print(cell.value)
    print("***************************************************************************")

    print("A2 value")
    print("********")
    A2 = sheet.acell('A2').value
    print(A2)
    print("***************************************************************************")

    print("Coordinates")
    print("***********")
    coord = sheet.cell(1, 3).value
    print(coord)
    print("***************************************************************************")

    print("First Row")
    print("**********")
    row = sheet.row_values(1) 
    print(row)
    print("***************************************************************************")
    
    print("Second Column")
    print("*************")
    col = sheet.col_values(2)
    print(col)
    print("***************************************************************************")
    
    # sheet.update_acell('C2', 'Blue')
    # sheet.update_cell(2, 3, 'Blue') #updates row 2 on column 3\n

    # sheet.update('A2:B3', [["Not Ford", "Not Lancia"], ["Nothing", "Not"]])

    # sheet.format('A1:C1', {'textFormat': {'bold': True}})


if __name__ == '__main__':
    main()