from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Папка для сохранения масок
os.makedirs("masks", exist_ok=True)

@app.post("/save-mask")
async def save_mask(mask: UploadFile = File(...)):
    file_path = f"masks/{mask.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(mask.file, f)
    return {"status": "ok", "file": file_path}

@app.get("/masks/{filename}")
def get_mask(filename: str):
    file_path = f"masks/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}
