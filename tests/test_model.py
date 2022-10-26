import time
from torchvision.io import read_image
from app.predictor import ObjectDetectionModel

img = read_image("cars.jpg")

model = ObjectDetectionModel()
start_time = time.time()
print(model.predict(img))
print(f"{100*(time.time() - start_time):.3f}ms")
