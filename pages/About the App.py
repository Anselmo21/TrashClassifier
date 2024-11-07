import streamlit as st

st.title("About the App")

st.subheader("Single Object Classification (Multi-Class)")
st.text('''The single object classifier makes use of multi-class classification and transfer 
learning to provide accurate results. The model was trained from a trash image 
dataset from Kaggle. DenseNet201 was utilized in order to facilitate the transfer 
learning portion of the project.''')
st.image('site_images/multi_class.png', caption='A confusion matrix representing the accuracy of the multi-class model.')

st.subheader("Multiple Object Classification (Multi-Label)")
st.text('''The multi object classifier used multi-label classification techniques along 
with transfer learning to provide accurate results. Due to a lack of a reliable 
dataset, the model was trained on a custom dataset which involved scraping the 
internet for photos of trash and providing the appropriate labels. The YOLO model 
was used to help train the application.''')
st.image('site_images/multi_label.png', caption='A confusion matrix representing the accuracy of the multi-label model.')
