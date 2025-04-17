# Automated Attendance System using CNN

An intelligent face recognition-based attendance management system utilizing Convolutional Neural Networks (CNN). This system can automatically process webcam feeds, videos, or images to identify individuals and mark their attendance in real-time. The solution is designed to be robust against common challenges such as occlusion (partially visible/covered faces), varying orientations, alignment issues, and different lighting conditions.

## Features

- **Face Detection and Recognition**: Uses MTCNN for face detection and FaceNet for face recognition
- **User-friendly GUI**: Built with Tkinter for ease of use
- **Multiple Input Options**: Supports webcam feeds, video files, and image inputs
- **Automated Attendance Recording**: Generates Excel spreadsheets with attendance records
- **Customizable Parameters**: Adjustable thresholds for detection and recognition confidence
- **Robust Performance**: Works with varying lighting conditions and partial face visibility

## System Requirements

### Hardware
- CPU with decent processing power (Intel i5 or equivalent recommended)
- Minimum 4GB RAM (8GB or more recommended)
- Webcam (for live capture functionality)
- GPU support is beneficial for faster processing

### Software Dependencies
1. Python 3.6+
2. TensorFlow 1.14
3. NumPy
4. OpenCV
5. MTCNN
6. scikit-learn
7. xlsxwriter, xlrd, xlutils
8. SciPy
9. Pickle
10. PIL (Python Imaging Library)

## Installation

1. Clone this repository or download the source code.
2. Create a Python virtual environment (Conda environment recommended):
   ```
   conda create -n attendance_env python=3.6
   conda activate attendance_env
   ```
3. Install the required libraries:
   ```
   pip install tensorflow==1.14 numpy opencv-python mtcnn scikit-learn xlsxwriter xlrd xlutils scipy pillow
   ```
4. Download the pre-trained FaceNet model from [here](https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-) and extract it to the project directory.
5. Create the required directory structure:
   - Create an `attendance` folder in the main directory (for storing attendance sheets)
   - Create an `output` folder in the main directory (for storing processed face images)
   - Ensure the `20180402-114759` model folder is in the main directory

## Directory Structure

The project requires the following directory structure:

1. **Main Directory**: Contains all code files and subdirectories
2. **output Directory**: Contains subdirectories for each person's face images
3. **attendance Directory**: Stores the generated attendance Excel sheets
4. **20180402-114759 Directory**: Contains the pre-trained FaceNet model

Each person's dataset should be stored in a separate folder within the `output` directory with their name as the folder name. These folders will contain the face images used for training.

## Usage Instructions

### Getting Started

To verify that everything is installed properly, run the user interface:
```
python user_interface.py
```

### Creating a Dataset

1. Run `user_interface.py`
2. Click on the 'Create' button in the main menu
3. Select 'webcam' if you wish to create a live dataset (you can leave other fields empty)
4. Click the 'Continue' button to start streaming webcam feed
5. Press 's' to save face images (capturing approximately 80-100 images is recommended)
6. Press 'q' to exit
7. Repeat this process to create datasets for different individuals

### Training the Model

1. Run `user_interface.py`
2. Click on the 'Train' button in the main menu
3. Wait for the training process to complete (this may take several minutes depending on your system configuration)
4. Upon completion, a 'classifier.pkl' file will be generated in the main directory

### Running the Attendance System

1. Run `user_interface.py`
2. Click on the 'Run' button in the main menu
3. Select the input source:
   - 'Webcam' for live camera feed
   - 'Video' for pre-recorded video files
   - 'Image' for still images
4. Adjust parameters if needed or leave them at default values
5. Click on 'Mark Attendance' button to start the detection and recognition process
6. The system will automatically generate an attendance sheet in the 'attendance' folder

## Technical Overview

This system uses a two-stage approach for attendance management:

1. **Face Detection**: MTCNN (Multi-task Cascaded Convolutional Networks) is used to detect and align faces in the input stream.

2. **Face Recognition**: The detected faces are passed through a pre-trained FaceNet model to generate 128-dimensional face embeddings, which are then classified using an SVM classifier to identify individuals.

The workflow consists of:
- Creating datasets by capturing face images
- Processing and aligning these faces
- Training a classifier on the processed face embeddings
- Using the trained model to recognize faces in new inputs
- Recording attendance in Excel spreadsheets

## Research Paper

The implementation is based on the research paper:
[CNN-Based End-to-End Face Recognition System](https://ieeexplore.ieee.org/document/9029001)

## License

This project is licensed under the terms of the included LICENSE file.

## Acknowledgments

- FaceNet paper: "FaceNet: A Unified Embedding for Face Recognition and Clustering"
- MTCNN paper: "Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks"
