# Celebrity Facial Recognition AI

## Introduction
This project was inspired by freeCodeCamp's course on "PyTorch for Deep Learning and Machine Learning".

Using PyTorch, an inbuilt ResNet18 convolutional neural network (CNN) was trained further via transfer learning, enabling it to identify the faces of 105 celebrities.

## Methodology
Image data was sourced from the ["Pins Face Recognition" dataset](https://www.kaggle.com/datasets/hereisburak/pins-face-recognition), which consisted of 17534 faces belonging to 105 celebrities. `setup.py` was the Python script used to format the data appropriately, before splitting them into training and testing datasets. The train-test split used was 75% for training and 25% for testing. 

Transfer learning was carried out in the following manner:
* Model: ResNet18 (built into PyTorch)
* Number of epochs: 50
* Loss function: `nn.CrossEntropyLoss()`
* Optimiser: `torch.optim.AdamW()`
* Learning rate: 0.0002
* Scheduler: `torch.optim.lr_scheduler.MultiStepLR()`, decay by a factor of gamma = 0.3 after 8, 15 and 20 epochs


Get the necessary files here: https://drive.google.com/drive/folders/1C2Z8bg6KHHdtmWkwpubrsvrwxxnZhmtf?usp=sharing
