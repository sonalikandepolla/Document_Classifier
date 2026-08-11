

---

# Document-Classification Project using VGG16 Model

This project focuses on Document(image) classification model using the VGG16 architecture to classify images into different classes. The model is trained to identify various types of documents, including Aadhaar cards, PAN cards, and driving licenses.
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Usage](#usage)
- [Results](#results)
- [Dependencies](#dependencies)
- [Setup](#setup)
- [Contributing](#contributing)
- [Author](#Author)
- [License](#license)

## Introduction

This project is developed to classify Documents(images) using an image classification model i.e VGG16 model architecture. The goal is to classify images of documents into categories such as Aadhaar cards, PAN cards, and driving licenses. In cases where the model is unsure about the classification, it labels the image as "unknown."

## Dataset

Images are segeregated based on training and validation in folders named "train and "val" Respectively.
The dataset used for training and validation consists of images categorized into Aadhaar cards, PAN cards, and driving licenses. The images have been preprocessed and resized to a common size for training and evaluation.
(some images are downloaded from roboflow and some from google)

## Model Architecture

The VGG16 model is utilized as the base architecture. The convolutional layers of the pre-trained VGG16 model are frozen to leverage its feature extraction capabilities. Additional dense layers are added on top of the pre-trained model to adapt it for the specific classification task. The model is trained using categorical cross-entropy loss and the Adam optimizer.

## Usage

1. Clone this repository to your local machine.
2. Set up the required dependencies (see Dependencies section).
3. Organize your dataset into appropriate directories: train and validation.
4. Configure the dataset paths and hyperparameters in the provided Python script.
5. Run the Python script -: app.py
6. The model is trained based on dataset that i provided in folders named "train" is "classify.h5" in the project directory.
7. Use the saved model to classify images using the provided test code.(already provided in the code just change the dir path)

## Results

The model is performing good ,is able to classify images better when the resolution is better
the val_accuracy is 85.47%
(NOTE-: The performance can be improved further as i used only limited no of images for training the model because govt documents aren't available)

## Dependencies

- Python 3.x
- TensorFlow 2.x
- Keras
- NumPy
- flask
- django

Install the required packages using the following command:

```
pip install tensorflow keras numpy flask 
```

## Setup

1. Clone this repository:

```
git clone https://github.com/yourusername/your-project.git
```

2. Navigate to the project directory:

```
cd <path to rootfolder>
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Organize your dataset into train and validation directories within the project directory(already did no changes to be done).

5. Configure the necessary paths and hyperparameters in the provided Python script.(change the paths to folders and model)

6. Run the training script:
 ```
 python app.py
 ```
  (you will be redirected to localhost server on your browser)

 7. Give the path of image to be tested or directly drop the image


    OUTPUT-:
    CLASS NAME OF IMAGE 

## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to create a pull request.

## Author

K.HARSHA VARDHAN

harshharsha360@gmail.com 

## License

This project is licensed under the MIT License - see the [LICENSE](#LICENSE) file for details.

---
