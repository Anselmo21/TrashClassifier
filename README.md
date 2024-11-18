# Welcome to the Trash Classifier Project 

## Overview
This repository is dedicated to an image classification project using machine learning. The goal is to develop a model capable of classifying images into various categories with high accuracy.

## Features
- **Data Preprocessing:** Scripts to clean and prepare the dataset.
- **Model Training:** Code for training a machine learning model on the dataset.
- **Model Evaluation:** Evaluation scripts to assess the performance of the model.
- **Inference:** Scripts for making predictions with the trained model.

## Installation
To get started with this project, follow these steps:

1. **Clone the Repository:**
   Clone this repository to your local machine using your preferred method (HTTPS, SSH, or GitHub CLI).

2. **Install Dependencies:**
   Navigate to the project directory and run the following command to install the required dependencies:
   pip install -r requirements.txt


3. **Note:**
   This command does not install all the required libraries for each model_training_pipeline.py to initiate the training. It is only to execute the
   main streamlit application which uses the imported model files (.pt and .json) and as such the training related libraries will have to be installed manually 
   if training is to be redone.


## Running the Application
While the applications can be accessed by directly running each model independently, the most effective way of viewing it is through the StreamLit interface.
This must be completed through a local environment as the process is too memory-intensive for base-level hosting sites. To properly open the interface, follow these 
steps... 

1. Ensure all files from the repository are in your local environment. 
2. Run **pip install -r requirements.txt** to download the correct versions of the libraries 
3. Run **streamlit run Main.py** to open the interface 
4. Follow the prompts on the interface


## Detailed Description of Models

### Multi-Class Classification Model
- **Location:** The training notebook for the multi-class model is located in the `multi_class_classification_model` directory.
- **Training Pipeline:** Detailed in `model_training_pipeline.py`.
- **Data Source:** The dataset is sourced directly from Kaggle. A Kaggle account and API key are required for training: https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification/datas
- **Environment:** Designed for the Google Colab environment (free version). For alternative training purposes, this environment is recommended.
- **Model Output:** The trained model's architecture is saved as `garbage_model.json` and its trained parameters is saved as `garbage_model.h5`.

### Multi-Label Classification Model
- **Location:** The training notebook for the multi-label model is in the `multi_label_classification_model` directory.
- **Training Details:** Found in `model_training_pipeline.py`.
- **Primary Purpose:** The sole purpose of this notebook is to initiate the training of the dataset stored in the Ultralytics Hub.
- **Configuration:** Yolo model configuration is available in the `data.yaml` file within the dataset directory.
- **Data Preparation:** The dataset was primarily assembled by scraping images from Google. It can be found under dataset folder 
- **Ultralytics Hub:** To start training, an Ultralytics Hub account and API key are necessary. The dataset was uploaded here for training purposes.
- **Model Output:** The trained model is stored as `garbage.pt`.
- **Additional Scripts:** 
   - `image_scraper.py` for scraping images using Selenium.
   - `image_detector.py` to test the trained model on pictures in the `images` folder.

### Streamlit Application
- **File:** `main.py` hosts the lightweight web application integrating both models.

---

Feel free to contribute or suggest improvements to this project. Your feedback and contributions are highly appreciated!
