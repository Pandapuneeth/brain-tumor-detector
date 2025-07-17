# 🧠 Brain Tumor Detector

An AI-powered web app that predicts brain tumor types (Glioma, Meningioma, Pituitary) from MRI scans using deep learning.

### 🚀 Live Demo
[Click here to launch app](https://your-app.streamlit.app)  ← (update this after deployment)

### 🔍 Features
- Upload your own MRI or choose a sample
- Uses a trained CNN model
- Real-time prediction with confidence score
- Clean GUI built with Streamlit

### 📦 Tech Stack
- Python 🐍
- TensorFlow / Keras
- Streamlit
- Google Drive (for model storage)

### 🧠 Model
Pretrained CNN model hosted on Google Drive. Automatically downloaded when the app runs.

---

### ✅ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
