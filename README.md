# Kewlarization
Image colorization using Deep neural network techniques

[Project Page](https://docs.google.com/document/d/1fVftGix7oQKbv8RJVrcg32wUZP8UkuLyyuD77DEFeR4/edit#heading=h.u1nhoxyp55w)

A collection of Deep Learning based Image Colorization techniques and corresponding source code/demo program.

## Prerequisites
- Linux/macOS/Windows
- Python 3.7+
- Tensorflow GPU recommended (2.6)
- Virtual env/conda recommended

## Structure

1) extract_unsplash.ipynb - all the functions related to downloading images from the image url in Unsplash lite dataset to png format
2) GAN_colorization.ipynb - Generative Adversarial Networks (GAN) using keras for image colorization 
3) image_urls_unsplash.csv - image urls from the Unsplash lite dataset
4) model_training_baseline.ipynb (Baseline model)- Basic deep learning model for image colorization trained on a single image
5) model_training_level2.ipynb - Model trained for image colorization model using CNN and dense neural network using images from celebrity cropped face images, unsplash lite, tiny imageNet,

## Requirements

Install the following packages using 
```
pip install -r requirements.txt
```
- keras
- tensorflow-gpu
- scikit-image
- pandas
- pillow
- numPy
- scikit-learn

## Dataset preparation

Mainly we used a subset of [Tiny-ImageNet](http://www.image-net.org), [Unsplash lite dataset](https://github.com/unsplash/datasets) and [Face Images](https://github.com/2014mchidamb/DeepColorization/tree/master/face_images)
datasets to run the experiments. 

The following datasets are used for the specific experiments:

1) model_training_baseline.ipynb (Baseline experiment): Trained on a single image
2) model_training_level2.ipynb: Subset of the Tiny-ImageNet dataset (500 images)
3) ImageColorization_With_GANs.ipynb: ImageNet/all_kinds

## Examples

1) Baseline Experiments

![1](readme_images/baseline.png)

2) Deep Convolution Experiment

![2](readme_images/level2.png)

3)  Generative Adversarial Networks

![2](readme_images/gan.png)

