from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from . import models, schemas, crud, dependencies
from .database import engine, SessionLocal
from .s3 import upload_file
import uvicorn


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/memes", response_model=schemas.MemeList)
def read_memes(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    memes = crud.get_memes(db, skip=skip, limit=limit)
    print('URL get memes')
    return {"memes": memes}

@app.get("/memes/{meme_id}", response_model=schemas.Meme)
def read_meme(meme_id: int, db: Session = Depends(dependencies.get_db)):
    meme = crud.get_meme(db, meme_id=meme_id)
    if meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return meme


@app.post("/memes", response_model=schemas.Meme)
async def create_meme(text: str = Form(...), image: UploadFile = File(...), db: Session = Depends(dependencies.get_db)):
    try:
        image_url = upload_file(image.file, image.filename)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    meme = schemas.MemeCreate(text=text, image_url=image_url)
    return crud.create_meme(db=db, meme=meme)

@app.put("/memes/{meme_id}", response_model=schemas.Meme)
def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(dependencies.get_db)):
    return crud.update_meme(db=db, meme_id=meme_id, meme=meme)

@app.delete("/memes/{meme_id}", response_model=schemas.Meme)
def delete_meme(meme_id: int, db: Session = Depends(dependencies.get_db)):
    return crud.delete_meme(db=db, meme_id=meme_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
