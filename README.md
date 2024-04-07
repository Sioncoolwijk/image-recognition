# Image Classifier Flask Application

## Introduction
This Flask application leverages a pretrained ResNet50 model from PyTorch's model library to classify images. It includes a web interface for users to upload images and receive predictions.

## Set-up
`python -m venv .venv`

`source .venv/bin/activate`

`pip install -r requirements.text`

`cd image-recognition`

`python app.py`

This will start the Flask application on `localhost` with default port `5000`.

## Usage
Open your web browser and go to `http://127.0.0.1:5000/` to access the application. Follow these steps to use the application:

1.  Click on the "Select image" button and choose an image to upload.
2.  Click on the "Upload" button to upload the image.
3.  If the image is successfully uploaded, it will be displayed on the web page.
4.  Click on the "Detect Image" button to classify the image. The predicted object in the image and the confidence level will be displayed.

## Screenshots from Application
![Screenshot 2024-04-05 at 17 04 17](https://github.com/Sioncoolwijk/image-recognition/assets/70899366/11bef60f-13f9-401a-a2aa-d5cd36bb8f41)

![Screenshot 2024-04-05 at 17 04 26](https://github.com/Sioncoolwijk/image-recognition/assets/70899366/05833058-9f65-4f14-a130-22dd055a6cd0)

![Screenshot 2024-04-05 at 17 03 37](https://github.com/Sioncoolwijk/image-recognition/assets/70899366/1308f216-2d05-48b4-9ab9-57da632605e7)
