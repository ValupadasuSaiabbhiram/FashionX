import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import streamlit as st
from PIL import Image
import numpy as np
import pickle
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm

# Create uploads directory if it doesn't exist
os.makedirs('uploads', exist_ok=True)

# Load precomputed features and filenames
feature_list = np.array(pickle.load(open('embeddings.pkl', 'rb')))
filenames = pickle.load(open('filenames.pkl', 'rb'))

# Initialize the model
model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.trainable = False

model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

st.title('Fashion Recommender System')

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads', uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return 0

def feature_extraction(img_path, model):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        expanded_img_array = np.expand_dims(img_array, axis=0)
        preprocessed_img = preprocess_input(expanded_img_array)
        result = model.predict(preprocessed_img, verbose=0).flatten()
        normalized_result = result / norm(result)
        return normalized_result
    except Exception as e:
        st.error(f"Error in feature extraction: {e}")
        return None

def recommend(features, feature_list):
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)
    distances, indices = neighbors.kneighbors([features])
    return indices

# File upload and processing
uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # Display the uploaded image
        display_image = Image.open(uploaded_file)
        st.image(display_image, caption="Uploaded Image", use_container_width=True)
        
        # Extract features
        features = feature_extraction(os.path.join("uploads", uploaded_file.name), model)
        
        if features is not None:
            # Get recommendations
            indices = recommend(features, feature_list)
            
            # Display recommendations
            st.subheader("Recommended Items")
            cols = st.columns(5)
            
            for i, col in enumerate(cols):
                if i < 5:  # Display first 5 recommendations
                    try:
                        col.image(filenames[indices[0][i]], use_container_width=True)
                    except Exception as e:
                        col.error(f"Error loading image: {e}")
        else:
            st.error("Feature extraction failed")
    else:
        st.error("File upload failed")