import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image  # type: ignore
from PIL import Image
import os
import cv2

# Global variables
MODEL_PATH = "C:\\Users\\SUBHASHINI\\Downloads\\pneumonia detection using deeplearning\\pneumonia detection using deeplearning\\models\\VGG16.h5"

IMG_SIZE = (224, 224)
CLASS_NAMES = ["NORMAL", "PNEUMONIA"]

# Load the model
model = None


def load_pneumonia_model():
    global model
    if model is None:
        model = load_model(MODEL_PATH)
    return model


def process_image(img_path):
    """
    Process the input image for model prediction.

    Args:
        img_path: Path to the input image file

    Returns:
        Processed image as a numpy array
    """
    # Read image
    img = cv2.imread(img_path)

    # Convert to RGB if needed (OpenCV uses BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize image to expected input size
    img = cv2.resize(img, IMG_SIZE)

    # Convert to array and normalize
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize to [0,1]

    return img_array


def make_prediction(img_array):
    """
    Make a prediction using the loaded model.

    Args:
        img_array: Processed image as a numpy array

    Returns:
        prediction: Class prediction (NORMAL or PNEUMONIA)
        confidence: Confidence score (probability)
    """
    # Ensure model is loaded
    model = load_pneumonia_model()

    # Make prediction
    predictions = model.predict(img_array)

    # Get the predicted class and confidence
    predicted_class_index = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_class_index]) * 100
    prediction = CLASS_NAMES[predicted_class_index]

    return prediction, confidence
