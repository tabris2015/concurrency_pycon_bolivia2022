from fastapi import FastAPI, UploadFile, File
from app.predictor import ObjectDetectionModel

app = FastAPI(title="Awesome API")
model = ObjectDetectionModel(score_threshold=0.5)

@app.get("/")
async def root():
    return {"message": "hello"}

@app.post("/predict_od")
async def predict_object_detection(image_file: UploadFile = File()):
    return await model.predict_file(image_file.file)
