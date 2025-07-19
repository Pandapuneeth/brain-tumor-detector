# 🧠 Brain Tumor Detector with Deep Learning and Streamlit

This project provides a simple and interactive GUI built with **Streamlit** to detect brain tumors from MRI images using a pre-trained **Keras CNN model**.


## 🔍 Features

- Upload your own MRI scan or choose from sample images
- Predicts tumor type:
  - Glioma
  - Meningioma
  - Pituitary
  - No Tumor
- Clean GUI with fast inference using a trained `.h5` model

## 🧠 Model

The trained model is not included in this repository due to GitHub’s file size limits.

📥 [Download the model from Google Drive](https://drive.google.com/file/d/1G2g4gsEOWWkuZ5ggVT7GdxgflwHbWkQc/view?usp=sharing)

Place the downloaded file in the project root as:



### 🧠 Model
Pretrained CNN model hosted on Google Drive. Automatically downloaded when the app runs.

---

### ✅ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
