# Deplyment Options:
# 1. WebPage - HTML/CSS/JavaScript - Flask/Django
# 2. WebApp - Streamlit/Dash
# 3. Mobile App - Kotlin/Java

#!pip install streamlit     # Deploying model
#!pip install pyngrok       # To turn Data SCience script into a website using Streamlit

from pyngrok import ngrok
import streamlit as st
#import prediction
from PIL import Image
import urllib.request

#st.set_option('showWarningOnDirectExecution',False)
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")

st.title('Image classifier')
st.text('Upload JPG format image link')


url = st.text_input("Enter your URL")

urllib.request.urlretrieve(url, "image_toPredict.jpg")
image = Image.open('image_toPredict.jpg')

st.image(image, caption='Is it a human or robot?')
# To run the file on VSCODE:
# python -m streamlit run Deployment.py