import io
import cv2
from fastapi import FastAPI, UploadFile, File
from starlette.responses import StreamingResponse
from app.predictor import ObjectDetectionModel, SelfieSegmentationModel

app = FastAPI(title="Awesome API")
model = ObjectDetectionModel(score_threshold=0.5)
seg_model = SelfieSegmentationModel()


@app.get("/")
async def root():
    return {"message": "hello"}


@app.post("/predict")
def predict_object_detection(image_file: UploadFile = File()):
    return model.predict_file(image_file.file)


@app.post("/async_predict")
async def async_predict_object_detection(image_file: UploadFile = File()):
    return await model.async_predict_file(image_file.file)


@app.post("/predict_segmentation")
def predict_segmentation(image_file: UploadFile = File()):
    output = seg_model.predict_file(image_file.file)
    res, img_png = cv2.imencode(".png", output)
    return StreamingResponse(io.BytesIO(img_png.tobytes()), media_type="image/png")
