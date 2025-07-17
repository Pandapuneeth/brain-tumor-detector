import streamlit as st
import numpy as np
from PIL import Image
import os
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load model
model = load_model("brain_tumor_model.h5")
classes = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']
folders = ['glioma', 'meningioma', 'notumor', 'pituitary']

st.title("🧠 Brain Tumor Detector")
st.markdown("Upload an MRI scan or choose a sample to detect tumor type using deep learning.")

# --- Sample image selector ---
with st.sidebar:
    st.header("📂 Choose Sample Image")
    selected_folder = st.selectbox("Tumor Type", folders)
    images = os.listdir(f"sample_images/{selected_folder}")
    selected_image = st.selectbox("Sample Image", images)

    use_sample = st.checkbox("Use selected sample image instead of uploading")

# --- Image input ---
uploaded_file = None
if not use_sample:
    uploaded_file = st.file_uploader("Upload MRI image", type=['jpg', 'jpeg', 'png'])

if uploaded_file or use_sample:
    if use_sample:
        path = f"sample_images/{selected_folder}/{selected_image}"
        img = Image.open(path).convert('L')  
    else:
        img = Image.open(uploaded_file).convert('L')  


    st.image(img, caption="MRI Scan", use_container_width=True)

    # Preprocessing
    img_resized = img.resize((150, 150))
    img_array = np.array(img_resized) / 255.0
    img_array = img_array.reshape(1, 150, 150, 1)

    # Prediction
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    # Output
    st.subheader(f"🔍 Prediction: **{classes[class_index]}**")
    st.write(f"📊 Confidence: **{confidence:.2f}%**")
