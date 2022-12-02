import pickle 
import numpy as np
from skimage import io
from skimage.io import imread
from skimage.transform import resize
import matplotlib.pyplot as plt

import Deployment
from Deployment import st
from Deployment import url

CATEGORIES = ['human being','robot']

model = pickle.load(open('image_model.p','rb'))

flat_data = []


#url = input('')
img = imread(url)
img_resized = resize(img, (350,350,3))
flat_data.append(img_resized.flatten())
flat_data = np.array(flat_data)

st.code(img.shape, "python")
# print(img.shape)
# io.imshow(img_resized)

y_out = model.predict(flat_data)
y_out = CATEGORIES[y_out[0]]

# Text
st.text("PREDICTED OUTPUT: ")
st.code(y_out, "python")

# st.code(plt.show(), "python")