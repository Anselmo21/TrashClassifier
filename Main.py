import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import model_from_json
from ultralytics import YOLO

# For more information on the method calls, visit the Streamlit API Reference site 
# https://docs.streamlit.io/library/api-reference

def main():
    settitle()
    radio = st.radio(label="Switch between classifying one or multiple objects", options=['One object', 'Multiple objects'])
    submission_file = dropbox()

    if 'submission_file' not in st.session_state or st.session_state.submission_file != submission_file:
        st.session_state.submission_file = submission_file

    if not submission_file is None:
        with open(submission_file.name, 'wb') as f:
            f.write(submission_file.read())
        button = st.button(label="Submit File")
        if button:
            st.session_state.radio = radio
            init_model()


def settitle():
    st.write('''
     # EECS 4404 Garbage Classifier
     Welcome to our garbage classifier project! 
     Upload an image to get started. 
     ''')


def dropbox():
    dropbox = st.file_uploader(label='Note: The picture must be in colour', type=['jpg'])
    return dropbox


def init_model():
    if st.session_state.radio == 'One object':
        json_file = open('multi_class_classification_model/garbage_model.json', 'r').read()
        model = model_from_json(json_file)
        model.load_weights('multi_class_classification_model/garbage_model.h5')
        returned_data = image_prediction(st.session_state.submission_file, model)

        st.set_option('deprecation.showPyplotGlobalUse', False)  # Due to visible deprecation warning

        st.divider()
        st.write("## Your Results")
        st.pyplot(returned_data.pop('Plot'))
        st.error(f'''
           Image: {returned_data["Image"]}\n
           Prediction: {returned_data["Prediction"]}\n
           Probability: {returned_data["Probability"]}\n
           Comments: {returned_data["Comments"]}
           ''')
    else:
        # Load the YOLOv8 model
        model = YOLO('multi_label_classification_model/garbage.pt')

        # Read the image
        frame = cv2.imread(st.session_state.submission_file.name)

        # Run YOLOv8 inference on the image
        resized_frame = cv2.resize(frame, (600, 500))
        results = model(resized_frame, conf=0.3)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        st.subheader("Your Results")
        st.image(annotated_frame)


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
