import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import model_from_json


def main():
    settitle()
    submission_file = dropbox()

    if not submission_file is None:
        with open(submission_file.name, 'wb') as f:
            f.write(submission_file.read())

        if 'submission_file' not in st.session_state:
            st.session_state.submission_file = submission_file

        button = st.button(label="Submit File")
        if button:
            init_model()


def settitle():
    st.write('''
     # EECS 4404 Garbage Classifier
     Welcome to our garbage classifier project! 
     Upload an image to get started. 
     ''')


def dropbox():
    dropbox = st.file_uploader(label='Note: The picture must be in colour', type=['png', 'jpg'])
    return dropbox


def init_model():
    json_file = open('resources/garbage_model.json', 'r').read()
    model = model_from_json(json_file)

    returned_data = image_prediction(st.session_state.submission_file, model)

    st.set_option('deprecation.showPyplotGlobalUse', False) # Due to visible deprecation warning

    st.divider()
    st.write("## Your Results")
    st.pyplot(returned_data.pop('Plot'))
    st.error(f'''
    Image: {returned_data["Image"]}\n
    Prediction: {returned_data["Prediction"]}\n
    Probability: {returned_data["Probability"]}\n
    Comments: {returned_data["Comments"]}
    ''')


def image_prediction(path, model):
    mask_label = {0: "cardboard", 1: "glass", 2: "metal", 3: "paper", 4: "plastic", 5: "trash"}
    sample_mask_img = cv2.imread(path.name)
    img = cv2.resize(sample_mask_img, (224, 224))
    sample_mask_img = np.reshape(img, [1, 224, 224, 3])
    sample_mask_img = sample_mask_img / 255.0
    prediction = model.predict(sample_mask_img, verbose=0)
    labels = [mask_label[i] for i in range(len(mask_label))]
    probabilities = prediction[0]
    label = np.argmax(prediction)
    probability = probabilities[label]
    plt.imshow(img)
    title = f"Predicted: {mask_label[label]}\n"
    title += "Class Probabilities:\n"
    for i in range(len(mask_label)):
        title += f"{mask_label[i]}: {probabilities[i]:.2f} "
        if i % 3 == 1:
            title += f"\n"
    plt.title(title, fontsize=12)

    text = ''
    if mask_label[label] == 'trash':
        text = 'Non-recylable'
    else:
        text = 'Recylable'
    return {"Image": path.name, "Prediction": mask_label[label], 'Probability': probability, 'Comments': text, 'Plot': plt.show()}


if __name__ == "__main__":
    main()