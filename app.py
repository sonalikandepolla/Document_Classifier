import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image

from flask import Flask, request, render_template

app = Flask(__name__)

# Set the path to your saved model
model_path = r'C:\Users\harsha\Desktop\dataset\my_model1.h5'

# Load the saved model
model = keras.models.load_model(model_path)

@app.route('/predict', methods=['POST'])
def upload_and_predict():
    # Get the uploaded file
    image = request.files['image']
    # Save the file to the uploads directory
    image_path = os.path.join('uploads', image.filename)
    image.save(image_path)
    # Make a prediction on the image
    result = predict(image_path)
    # Return the result to the user
    return render_template('index.html', result=result)

# Define the function to make predictions on images
def predict(image_path):
    # Load and preprocess the image
    img = Image.open(image_path).convert('RGB')
    img = img.resize((224, 224))  # Resize the image if needed
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    # Make the prediction
    preds = model.predict(x)
    class_idx = np.argmax(preds[0])
    # Assuming you have a list of class labels
    class_labels = ["adhaar card", "Driving_liscence", "Pan Card"]
    predicted_class = class_labels[class_idx]

    # Return the predicted class
    return predicted_class


# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
