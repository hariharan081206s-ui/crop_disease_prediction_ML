# 🌿 Crop Disease Prediction Using Machine Learning

An AI-powered Smart Agriculture Web Application built using **Streamlit** and **TensorFlow (Convolutional Neural Networks)** to diagnose plant diseases from leaf imagery and provide targeted treatment and prevention recommendations.

Designed & Developed by: **Hariharan S**

---

## 🌟 Key Features

- **Deep Learning Model Integration**: Loads pre-trained Keras model (`crop_disease_model.keras`) with high-performance caching (`@st.cache_resource`).
- **Automated Image Preprocessing**: Automatically resizes leaf images to **224×224 pixels** and normalizes pixel values (`/ 255.0`).
- **29 Crop Disease Pathologies**: Supports diagnostic classification across 29 crop disease categories (Apple, Corn, Grape, Potato, Tomato, Pepper, Peach, etc.).
- **Diagnostic Confidence Gauge**: Displays model confidence as a percentage with visual progress meters.
- **Actionable Treatment Plans & Prevention**: Provides a comprehensive dictionary of symptoms, chemical/organic treatments, and cultural prevention tips for every disease class.
- **Emerald Green Modern UI**: Designed with glassmorphism cards, responsive layouts, badges, and developer attribution footer.
- **Sidebar Analytics**: Displays project description, technology stack badges, model input dimensions, and usage guide.

---

## 🛠️ Technology Stack

- **Python 3.x**
- **Streamlit** (Interactive Web UI Framework)
- **TensorFlow / Keras** (Deep Learning & Computer Vision)
- **Pillow (PIL)** & **NumPy** (Image Data Manipulation)

---

## 📁 Project Structure

```text
Crop_Disease_Prediction_Project/
│
├── crop_disease_model.keras   # Pre-trained TensorFlow CNN Model
├── app.py                     # Main Streamlit Application Script
├── requirements.txt           # Python Dependencies
└── README.md                  # Project Documentation
```

---

## 🚀 Installation & Running Guide

### 1. Clone or Open Project Directory
Open your terminal or command prompt in the project root folder:
```bash
cd Crop_Disease_Prediction_Project
```

### 2. Install Dependencies
Install all required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Web Application
Start the Streamlit dev server:
```bash
streamlit run app.py
```

After executing the command, Streamlit will automatically open the web application in your default web browser at `http://localhost:8501`.

---

## 📝 Customizing Disease Class Names

The `app.py` script contains a `CLASS_NAMES` list with 29 crop disease categories:

```python
CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    # ... (29 classes)
]
```

If your trained model uses a different class order or custom labels, simply update the `CLASS_NAMES` list in `app.py` to match the exact order of class indices output by your TensorFlow model during training.

---

## 👨‍💻 Developer Credits

- **Developer**: Hariharan S
- **Project**: Final Year Engineering Demonstration - Crop Disease Prediction System
