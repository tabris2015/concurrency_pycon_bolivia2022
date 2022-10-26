import asyncio
from PIL import Image
import torchvision.transforms.functional as F
from torchvision.models.quantization import resnet50, ResNet50_QuantizedWeights
from torchvision.models.detection import SSD300_VGG16_Weights, ssd300_vgg16


class ClassificationModel:
    def __init__(self):
        self.weights = ResNet50_QuantizedWeights.DEFAULT
        self.model = resnet50(weights=self.weights, quantize=True)
        self.pre_transforms = self.weights.transforms()

    def preprocess(self, img):
        input_tensor = self.pre_transforms(img)
        input_batch = input_tensor.unsqueeze(0)
        return input_batch

    def predict(self, img):
        prediction = self.model(self.preprocess(img)).squeeze(0).softmax(0)
        class_id = prediction.argmax().item()
        score = prediction[class_id].item()
        category_name = self.weights.meta["categories"][class_id]
        return {category_name: 100 * score}


class ObjectDetectionModel:
    def __init__(self, score_threshold=0.8):
        self.score_threshold = score_threshold
        self.weights = SSD300_VGG16_Weights.DEFAULT
        self.model = ssd300_vgg16(weights=self.weights)
        self.model.eval()
        self.pre_transforms = self.weights.transforms()

    def preprocess(self, img):
        input_tensor = self.pre_transforms(img)
        input_batch = [input_tensor]
        return input_batch

    async def predict(self, img):
        input_batch = self.preprocess(img)
        prediction = (await asyncio.to_thread(self.model, input_batch))[0]
        labels = self.weights.meta["categories"]  # [self.weights.meta["categories"][i] for i in prediction["labels"]]
        boxes = [
            {"bbox": box.tolist(), "score": score.item(), "label": labels[label]}
            for box, score, label in zip(
                prediction["boxes"], prediction["scores"], prediction["labels"]
            ) if score >= self.score_threshold
        ]
        return boxes

    async def predict_file(self, file):
        img = F.to_tensor(Image.open(file))
        return await self.predict(img)
