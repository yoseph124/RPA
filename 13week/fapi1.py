from fastapi import FastAPI
from fastapi import Form
from fastapi import File, UploadFile
import shutil
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO

import qrcode.constants

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id,"name":name,"age":age}

@app.post("/user")
async def read_user_form(name: str = Form(...), studentcode: str = Form(...), major: str = Form(...)):
    print(f"Received data: Name={name}, Student Code={studentcode}, Major={major}")
    return {"msg": f"{major} {name}님 ({studentcode})반갑습니다."}

@app.post("/plus")
async def read_plus(num1: int = Form(...), num2: int = Form(...),num3: int = Form(...), num4: int = Form(...)):
    result = num1+num2
    result2 = num3+num4
    return {"result": f"{num1} + {num2} = {result} | {num3} + {num4} = {result2}"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    save_path = Path("static/uploads") / file.filename
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "location": str(save_path)}

@app.get("/files/{filename}")
async def get_file(filename: str):
    file_path = Path("static/uploads") / filename
    if file_path.is_file():
        return FileResponse(path=file_path, filename=filename) 
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.post("/qrcode/")
async def generate_qr(data: str = Form(...)):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    #바이너리 데이터로 변환
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr=img_byte_arr.getvalue()
    
    return StreamingResponse(BytesIO(img_byte_arr),media_type="image/png")

def loginDB(userId, userPassword):
    import sqlite3
    
    conn = sqlite3.connect('education.db')
    cursor = conn.cursor()
    
    query = 'SELECT * FROM user WHERE userId = ? AND userPassword = ?'
    cursor.execute(query, (userId, userPassword))
    result=cursor.fetchone()
    conn.close()
    
    if result:
        print("Login successful!")
        print("User Info : ", result) #쿼리 결과 출력
        return True
    
    else:
        print("Login failed. Invalid username or password.")
        return False
    
@app.post("/login")
def login_form(userid: str = Form(...),userpassword: str = Form(...)):
    result = loginDB (userid, userpassword)
    
    if result == True:
        return {"msg":f"{userid}님 반갑습니다"}
    
    else:
        return{"msg":f"로그인에 실패했습니다"}




from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static",html=True), name="static")

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1',port=8000,log_level="info")
    
