# face-extractor
MTCNN based face extractor

## Introduction
Detect faces from input images, and save the cropped face images to the output directory. It helps to generate the customized dataset for neural network trainings.

## Usage
1. Put input images to `./data/input` directory.
2. `python main.py`
3. Find the result in `./data/output` directory.

## MTCNN

MTCNN (Multi-Task Cascaded Convolutional Neural Network) is a deep learning model used for face detection, alignment, and recognition. It was proposed in 2016 by Zhang et al. and has since become a popular tool for face-related tasks in computer vision.

MTCNN consists of three stages of deep convolutional neural networks (CNNs), each of which performs a specific task in the face detection and alignment pipeline. The first stage, called the "Proposal Network" (P-Net), generates candidate face regions using a sliding window approach. The second stage, called the "Refinement Network" (R-Net), filters out false positives and produces more accurate bounding boxes around faces. The final stage, called the "Output Network" (O-Net), performs facial landmark localization and alignment.

MTCNN has several advantages over previous face detection and alignment methods. It is able to detect faces at different scales and orientations, handle occlusions and partial views, and produce accurate facial landmark locations for subsequent recognition tasks. MTCNN has been widely adopted in various applications such as security systems, social media, and virtual reality.