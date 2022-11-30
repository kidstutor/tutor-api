from fastapi import FastAPI
import pandas as pd
# from db.dbutils import Database as db
from app.entity.student import Student as Student
from app.entity.env import Env as Env
from app.entity.dbconn import DBConn
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# DBConn()

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
    try:
        students = Student().GetStudents()
        return {"data": students}
    except Exception as err:
        return {"exception": err}

@app.get("/students/cache")
async def reset_cache() -> dict:
    try:
        ret = Student().ResetCache()
        return {"data": ret}
    except Exception as err:
        return {"exception": err}

@app.get("/students/{id}")
async def get_student(id : int) -> dict:
    try:
        student = Student().GetStudent(id)
        return {"data": student}
    except Exception as err:
        return {"exception": err}


# @app.get("/env")
# async def get_env() -> dict:
#     e = Env()
#     data = e.get_env()
#     return {"data" : data}

# def main():
    # scopes = ['https://www.googleapis.com/auth/spreadsheets',
    #         'https://www.googleapis.com/auth/drive']

    # #access the json key you downloaded earlier           
    # # credentials = ServiceAccountCredentials.from_json_keyfile_name("tutorkids.json", scopes) 

    # keyfile_dict = {"type": "service_account",
    #                 "project_id": os.getenv("GOOGLE_PROJECT_ID"),
    #                 "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
    #                 "private_key": os.getenv("GOOGLE_PRIVATE_KEY"),
    #                 "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
    #                 "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    #                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #                 "token_uri": "https://oauth2.googleapis.com/token",
    #                 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #                 "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
    #                }

    # credentials = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, 
    #                                                                scopes=scopes)

    # # authenticate the JSON key with gspread
    # file = gspread.authorize(credentials) 

    # #open sheet
    # sheet = file.open("students")
    # # sheet = sheet.sheet1

    # sheet = sheet.worksheet('Sheet1')

    # print("all records")
    # print('************')
    # df = pd.DataFrame(sheet.get_all_records())
    # print(df)
    # print("***************************************************************************")



    # all_cells = sheet.range('A1:C6')
    # print("All cells")
    # print("*********")
    # print(all_cells)
    # print("***************************************************************************")
    
    # print("Cell Values in a for loop")
    # print("**************************")
    # for cell in all_cells:
    #     print(cell.value)
    # print("***************************************************************************")

    # print("A2 value")
    # print("********")
    # A2 = sheet.acell('A2').value
    # print(A2)
    # print("***************************************************************************")

    # print("Coordinates")
    # print("***********")
    # coord = sheet.cell(1, 3).value
    # print(coord)
    # print("***************************************************************************")

    # print("First Row")
    # print("**********")
    # row = sheet.row_values(1) 
    # print(row)
    # print("***************************************************************************")
    
    # print("Second Column")
    # print("*************")
    # col = sheet.col_values(2)
    # print(col)
    # print("***************************************************************************")
    
    # # sheet.update_acell('C2', 'Blue')
    # # sheet.update_cell(2, 3, 'Blue') #updates row 2 on column 3\n

    # # sheet.update('A2:B3', [["Not Ford", "Not Lancia"], ["Nothing", "Not"]])

    # # sheet.format('A1:C1', {'textFormat': {'bold': True}})


# if __name__ == '__main__':
#     main()