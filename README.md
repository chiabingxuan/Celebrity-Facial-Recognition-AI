# Celebrity Facial Recognition AI

## Introduction
This project was inspired by freeCodeCamp's course on "PyTorch for Deep Learning and Machine Learning".

Using PyTorch, an inbuilt ResNet18 convolutional neural network (CNN) was trained further via transfer learning, enabling it to identify the faces of 105 celebrities. `list_of_celebrities.txt` contains the names of all these celebrities.

## Methodology
Image data was sourced from the ["Pins Face Recognition" dataset](https://www.kaggle.com/datasets/hereisburak/pins-face-recognition), which contains 17534 cropped images of 105 celebrities. `setup.py` was the Python script used to format the data appropriately, before splitting them into training and testing datasets. The train-test split used was 75% for training and 25% for testing.

The transform used on the training data was as follows:
```
data_transform = v2.Compose([
    v2.Resize(size=(256, 256)),   # resize images
    v2.TrivialAugmentWide(num_magnitude_bins=31),
    v2.RandomHorizontalFlip(p=0.5),
    v2.RandomVerticalFlip(p=0.5),
    v2.ColorJitter(),
    v2.ToTensor()
])
```
Transfer learning was carried out in the following manner:
* Batch size: 32
* Model: ResNet18 (built into PyTorch)
    * Add a dropout layer with probabilty = 0.5 to the classifier layer
    * Freeze first 4 children of the CNN
* Number of epochs: 50
* Loss function: `nn.CrossEntropyLoss()`
* Optimiser: `torch.optim.AdamW()`
* Learning rate: 0.0002
* Scheduler: `torch.optim.lr_scheduler.MultiStepLR()`, decay by a factor of gamma = 0.3 after 8, 15 and 20 epochs

## Results
After training for 50 epochs, the model attained a training accuracy of 94.54% and a test accuracy of 92.54%. The loss curves and accuracy curves are shown below.

![training results](https://github.com/chiabingxuan/Celebrity-Facial-Recognition-AI/assets/155958349/7bae28db-b45f-491d-b71b-f1ecd4282f36)

## How to Use
Firstly, make sure you get the pretrained state dict (`celebrity_recognition_model.pth`) and the image data (`full_data.zip`) from [here](https://drive.google.com/drive/folders/1C2Z8bg6KHHdtmWkwpubrsvrwxxnZhmtf?usp=sharing). On Google Drive, create a folder named `celebrity_recognition_ai` within My Drive and place the two files inside this folder.

### Use the pretrained model
In `celebrity_recognition_project.ipynb`:
1. Run code chunks 1, 2b and 3
2. Run code chunks 7 - 9

### Train and test your own model
In `celebrity_recognition_project.ipynb`:
1. Run code chunks 1 - 6 (Training phase)
   * If you wish to handle a small dataset from only 4 celebrities: Run code chunk 2a
   * If you wish to handle the full data from all 105 celebrities: Run code chunk 2b
3. Run code chunks 8 - 9 (Testing phase)

**Note:** In code chunk 9, the model will attempt to carry out custom image prediction. If you wish to try this out, please place all your custom images of celebrities (either .jpg, .jpeg or .png format) inside the same `celebrity_recognition_ai` folder on Google Drive. For better performance, do ensure that each custom image is cropped such that only the celebrity's face is being shown. Before running the code block, do also remember to edit the code according to the file name of your custom image.
