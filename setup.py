import os
import shutil
import random
from pathlib import Path


def setup(celeb_names=None, training_prop=0.75, folders_unedited=False):
    absolute_path = Path("")  # please add the path to your working directory

    # Check for invalid celebrity names
    folders = os.listdir(absolute_path / "105_classes_pins_dataset")
    if celeb_names is None:
        celeb_names = folders
    invalid_names = list()
    for celeb_name in celeb_names:
        if celeb_name not in folders:
            invalid_names.append(celeb_name)
            print(f"Dataset does not contain pictures of {celeb_name}, will skip this celebrity...")
    for invalid_names in invalid_names:
        celeb_names.remove(invalid_names)

    # Editing folder names if they haven't been edited yet
    if folders_unedited:
        os.chdir(absolute_path / "105_classes_pins_dataset")
        for folder_name in folders:
            new_name = folder_name.split("_")[1].upper()
            os.rename(folder_name, new_name)
        print("Folder names of the dataset have now been correctly formatted!")
    else:
        print("Folder names of the dataset are already in the correct format, skipping folder name formatting...")
    os.chdir(absolute_path)

    # Remove existing folders
    train_path, test_path = absolute_path / "train", absolute_path / "test"
    if os.path.exists(train_path):
        shutil.rmtree(train_path)
    if os.path.exists(test_path):
        shutil.rmtree(test_path)
    print("Deleted existing training and testing folders!")

    # Create new folders
    os.makedirs(train_path)
    for name in celeb_names:
        if not os.path.exists(train_path / name):
            os.makedirs(train_path / name)
    os.makedirs(test_path)
    for name in celeb_names:
        if not os.path.exists(test_path / name):
            os.makedirs(test_path / name)
    print("New training and testing folders have now been created!")

    # Populating folders with random training and test samples (corresponding to the celebrities chosen)
    print("Populating training and testing folders...")
    for folder_name in folders:
        if folder_name in celeb_names:
            pictures = os.listdir(absolute_path / "105_classes_pins_dataset" / folder_name)
            num_pictures = len(pictures)
            print(f"Number of pictures for {folder_name}: {num_pictures}")
            num_training = int(training_prop * num_pictures)
            num_testing = num_pictures - num_training
            print(f"Number of training pictures for {folder_name}: {num_training}")
            print(f"Number of testing pictures for {folder_name}: {num_testing}")
            training_picture_names = random.sample(pictures, k=num_training)
            for picture_name in pictures:
                if picture_name in training_picture_names:  # training picture
                    shutil.copy(absolute_path / "105_classes_pins_dataset" / folder_name / picture_name,
                                absolute_path / train_path / folder_name)
                else:  # testing picture
                    shutil.copy(absolute_path / "105_classes_pins_dataset" / folder_name / picture_name,
                                absolute_path / test_path / folder_name)
    print("Training and testing folders have now been populated!")


if __name__ == "__main__":
    chosen_celeb_names = ["ANDY SAMBERG", "TOM CRUISE", "AVRIL LAVIGNE", "GWYNETH PALTROW",
                          "HARRY STYLES"]  # choose your celebrities here (write names in all caps)
    setup(celeb_names=chosen_celeb_names, folders_unedited=False)
