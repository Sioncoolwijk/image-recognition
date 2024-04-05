import torch
from torchvision import models, transforms
from PIL import Image
import ast
import os

def fit_image(image_path):

    # Load a pretrained model (e.g., ResNet50)
    model = models.resnet50(pretrained=True)
    model.eval()

    # Define the image transformations
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Load and preprocess the image
    img = Image.open(image_path)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)

    # Predict the class
    with torch.no_grad():
        out = model(batch_t)

    # Decode the prediction
    _, index = torch.max(out, 1)
    
    # Get classes and return predicted class and probability
    classes_file_path = os.path.join('app/static', 'classes.txt')
    with open(classes_file_path, 'r') as f:
        class_dict_str = f.read()
        labels_dict = ast.literal_eval(class_dict_str)

    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    predicted_index = index.item()

    return labels_dict[predicted_index], int(percentage[predicted_index].item())