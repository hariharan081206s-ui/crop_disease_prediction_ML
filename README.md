# 🌿 Crop Disease Prediction Using Machine Learning

An AI-powered Smart Agriculture Web Application built with **Streamlit** and **TensorFlow MobileNetV2** for diagnosing plant diseases from crop leaf images.

**Developer:** Hariharan S  
**Final Year Engineering Project**

---

## 🌟 Key Features

- **MobileNetV2 Transfer Learning** — Pre-trained on ImageNet, fine-tuned on PlantVillage
- **29 Crop Disease Classes** — Covering 14 plant types (Apple, Tomato, Potato, Corn, Grape, etc.)
- **Sub-second Prediction** — CPU-optimized inference, typically under 500ms
- **Confidence Badges** — High / Moderate / Low confidence indicators
- **Complete Disease Information** — Description, Symptoms, Cause, Organic & Chemical Treatment, Prevention
- **Top-5 Predictions** — Full probability breakdown with progress bars
- **Modern Dark UI** — Professional agriculture-themed dashboard

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Web Framework | Streamlit ≥ 1.28 |
| Deep Learning | TensorFlow ≥ 2.12 (Keras) |
| Model Architecture | MobileNetV2 (Transfer Learning) |
| Image Processing | Pillow (PIL) |
| Numerical Computing | NumPy |
| Language | Python 3.11 |

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Architecture | MobileNetV2 |
| Input Size | 224 × 224 pixels |
| Color Mode | RGB |
| Normalization | pixel / 255.0 |
| Output Classes | 29 |
| Model File | crop_disease_model.keras (~9 MB) |
| Training Dataset | PlantVillage |
| Training Platform | Google Colab |

---

## 📁 Project Structure

```
Crop_Disease_Prediction_Project/
│
├── app.py                    # Main Streamlit application
├── disease_info.py           # Disease information database module
├── crop_disease_model.keras  # Trained MobileNetV2 model (~9 MB)
├── class_names.txt           # 29 disease class names (matches model output order)
├── requirements.txt          # Python dependencies
├── run_app.bat               # One-click Windows launcher
├── train_model_colab.py      # Google Colab training script
└── README.md                 # Project documentation
```

---

## 🚀 Installation & Running

### Prerequisites
- Python 3.11 installed at `C:\Users\ELCOT\Documents\python311\`
- TensorFlow 2.21.0 and Streamlit 1.60.0 installed in that environment

### Option 1: Double-click launcher (Recommended)
```
Double-click run_app.bat
```

### Option 2: PowerShell command
```powershell
C:\Users\ELCOT\Documents\python311\python.exe -m streamlit run app.py
```

The app will open at: **http://localhost:8501**

---

## 📊 Supported Disease Classes (29)

| # | Disease Class |
|---|---|
| 1 | Apple - Apple Scab |
| 2 | Apple - Black Rot |
| 3 | Apple - Cedar Apple Rust |
| 4 | Apple - Healthy |
| 5 | Bell Pepper - Bacterial Spot |
| 6 | Bell Pepper - Healthy |
| 7 | Cherry - Healthy |
| 8 | Cherry - Powdery Mildew |
| 9 | Corn (Maize) - Cercospora Leaf Spot |
| 10 | Corn (Maize) - Common Rust |
| 11 | Corn (Maize) - Healthy |
| 12 | Corn (Maize) - Northern Leaf Blight |
| 13 | Grape - Black Rot |
| 14 | Grape - Esca (Black Measles) |
| 15 | Grape - Healthy |
| 16 | Grape - Leaf Blight |
| 17 | Peach - Bacterial Spot |
| 18 | Peach - Healthy |
| 19 | Potato - Early Blight |
| 20 | Potato - Healthy |
| 21 | Potato - Late Blight |
| 22 | Strawberry - Healthy |
| 23 | Strawberry - Leaf Scorch |
| 24 | Tomato - Bacterial Spot |
| 25 | Tomato - Early Blight |
| 26 | Tomato - Healthy |
| 27 | Tomato - Late Blight |
| 28 | Tomato - Septoria Leaf Spot |
| 29 | Tomato - Yellow Leaf Curl Virus |

---

## 📷 Usage Tips

For best prediction accuracy:
- ✅ Use a **close-up photo of a single leaf**
- ✅ Ensure the **leaf fills most of the frame**
- ✅ Shoot in **natural, indirect lighting**
- ✅ Use a **clean, uncluttered background**
- ❌ Avoid blurry, overexposed, or very dark images
- ❌ Avoid images with water droplets (can trigger false Powdery Mildew)

---

## 📈 Image Preprocessing Pipeline

Preprocessing exactly matches training:
1. Fix EXIF orientation (`ImageOps.exif_transpose`)
2. Convert to RGB
3. Resize to **224 × 224** (BILINEAR)
4. Convert to float32 NumPy array
5. Normalize: `array / 255.0`
6. Expand dims: `(224,224,3)` → `(1,224,224,3)`
7. `model.predict()` → softmax probabilities

---

## 🌱 Dataset Information

- **Name:** PlantVillage Dataset
- **Total Images:** ~87,000 labelled leaf images
- **Plant Types:** 14 different crops
- **Disease Categories:** 26 disease + 3 healthy classes
- **Image Format:** RGB JPEG, various resolutions
- **Source:** Penn State University / Kaggle

---

## 📄 License

This project is developed for Final Year Engineering purposes.  
Dataset: PlantVillage (publicly available for academic research).
