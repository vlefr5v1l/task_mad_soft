from fastapi import FastAPI, UploadFile, File, HTTPException
from .utils import upload_file, delete_file

app = FastAPI()

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    filename = file.filename
    try:
        url = upload_file(file.file, filename)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"url": url}

@app.delete("/delete/{filename}")
async def delete_image(filename: str):
    try:
        delete_file(filename)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "File deleted"}
