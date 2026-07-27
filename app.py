# ==============================================================================
# Crop Disease Prediction Using Machine Learning
# Developer: Hariharan S
# Framework: Streamlit & TensorFlow (CNN)
# Description: Clean neat UI – No sidebar. Image upload + Predict button only.
# ==============================================================================

import os
import numpy as np
from PIL import Image
import streamlit as st

# TensorFlow import with fallback
try:
    import tensorflow as tf
    TF_AVAILABLE = True
except Exception:
    TF_AVAILABLE = False


# ------------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & EMERALD GREEN THEME
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Crop Disease Prediction | AI Smart Farming",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject dark emerald CSS — works in both dark & light mode
st.markdown("""
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    * { font-family: 'Inter', sans-serif; box-sizing: border-box; }

    /* Hide sidebar & toggle entirely */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"],
    section[data-testid="stSidebarNav"] { display: none !important; }

    /* ── Dark emerald page background ── */
    .stApp {
        background: #0a0f0d !important;
        min-height: 100vh;
    }

    /* Override Streamlit's own body/block backgrounds */
    .main, section.main, [data-testid="stAppViewContainer"] {
        background: #0a0f0d !important;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 800px;
        margin: 0 auto;
        background: transparent !important;
    }

    /* ── Header ── */
    .hero {
        background: linear-gradient(135deg, #064e3b 0%, #047857 55%, #10b981 100%);
        padding: 2.4rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 12px 30px rgba(6, 78, 59, 0.25);
    }
    .hero h1 {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff !important;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.5px;
    }
    .hero p {
        font-size: 1rem;
        color: #bbf7d0;
        margin: 0;
    }

    /* ── Upload Card ── */
    .upload-card {
        background: #111c18;
        border-radius: 18px;
        padding: 2rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.4);
        border: 1px solid #1f4037;
        margin-bottom: 1.5rem;
    }
    .upload-card h3 {
        color: #6ee7b7;
        font-size: 1.15rem;
        font-weight: 700;
        margin: 0 0 0.4rem 0;
    }
    .upload-card p {
        color: #94a3b8;
        font-size: 0.9rem;
        margin: 0 0 1rem 0;
    }

    /* ── Image Preview ── */
    .preview-wrap {
        border-radius: 14px;
        overflow: hidden;
        border: 2px dashed #059669;
        background: #0d1f1a;
        padding: 0.5rem;
        margin-bottom: 1rem;
    }

    /* ── Predict Button ── */
    .stButton > button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        border-radius: 14px;
        font-weight: 800;
        font-size: 1.1rem;
        padding: 0.8rem 2rem;
        border: none;
        width: 100%;
        box-shadow: 0 6px 18px rgba(5, 150, 105, 0.35);
        transition: all 0.3s ease;
        letter-spacing: 0.3px;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #047857 0%, #064e3b 100%);
        box-shadow: 0 8px 24px rgba(5, 150, 105, 0.45);
        transform: translateY(-2px);
        color: #ffffff;
    }

    /* ── Result Card ── */
    .result-card {
        background: #111c18;
        border-radius: 18px;
        padding: 1.8rem;
        box-shadow: 0 6px 28px rgba(0,0,0,0.5);
        border: 1px solid #1f4037;
        margin-top: 1.8rem;
    }
    .result-label {
        font-size: 0.8rem;
        font-weight: 700;
        color: #6ee7b7;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 0.3rem;
    }
    .result-disease {
        font-size: 1.8rem;
        font-weight: 800;
        color: #a7f3d0;
        margin: 0.2rem 0 0.8rem 0;
    }

    /* Healthy / Disease badge */
    .badge-healthy {
        display: inline-flex; align-items: center; gap: 0.4rem;
        background: #064e3b; color: #6ee7b7;
        font-weight: 700; font-size: 1rem;
        padding: 0.45rem 1.1rem;
        border-radius: 50px;
        border: 2px solid #059669;
    }
    .badge-diseased {
        display: inline-flex; align-items: center; gap: 0.4rem;
        background: #3b0a0a; color: #fca5a5;
        font-weight: 700; font-size: 1rem;
        padding: 0.45rem 1.1rem;
        border-radius: 50px;
        border: 2px solid #ef4444;
    }

    /* Confidence bar */
    .conf-row {
        display: flex; justify-content: space-between; align-items: center;
        margin-top: 1.2rem; margin-bottom: 0.4rem;
    }
    .conf-label { font-size: 0.85rem; font-weight: 600; color: #94a3b8; }
    .conf-pct   { font-size: 1.1rem; font-weight: 800; color: #34d399; }
    .conf-bar-bg {
        background: #1a2e28; border-radius: 10px;
        overflow: hidden; height: 18px;
    }
    .conf-bar-fill {
        background: linear-gradient(90deg, #10b981, #059669);
        height: 100%; border-radius: 10px;
    }

    /* Info boxes inside tabs */
    .info-box {
        background: #0d1f1a;
        border-left: 5px solid #10b981;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        font-size: 1rem;
        line-height: 1.65;
        color: #cbd5e1;
        margin-top: 0.5rem;
    }

    /* Radio buttons */
    div[role="radiogroup"] label {
        font-weight: 600 !important;
        color: #34d399 !important;
    }

    /* Streamlit file uploader, tabs & expander overrides for dark */
    [data-testid="stFileUploader"],
    [data-testid="stFileUploadDropzone"] {
        background: #0d1f1a !important;
        border: 2px dashed #059669 !important;
        border-radius: 12px !important;
        color: #94a3b8 !important;
    }
    [data-testid="stFileUploadDropzone"] p {
        color: #94a3b8 !important;
    }
    button[data-testid="stBaseButton-secondary"] {
        background: #1f4037 !important;
        color: #6ee7b7 !important;
        border: 1px solid #059669 !important;
        border-radius: 8px !important;
    }
    /* Tab active colour */
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #10b981 !important;
        border-bottom-color: #10b981 !important;
    }
    /* Expander dark */
    details > summary {
        color: #6ee7b7 !important;
        font-weight: 600 !important;
    }
    /* Spinner text */
    [data-testid="stSpinner"] p { color: #6ee7b7 !important; }

    /* ── Footer ── */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.2rem;
        background: #064e3b;
        color: #bbf7d0;
        border-radius: 14px;
        font-size: 0.95rem;
        font-weight: 500;
    }
    .footer b { color: #6ee7b7; }
    .footer a { color: #34d399; text-decoration: none; font-weight: 700; }

    /* ── Hide ghost/orphan widget containers ── */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:empty,
    div.stRadio { display: none !important; }

    /* Style st.tabs to match dark theme */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        background: #111c18;
        border-radius: 14px 14px 0 0;
        padding: 0.3rem 0.3rem 0 0.3rem;
        gap: 4px;
        border-bottom: 2px solid #1f4037;
    }
    [data-testid="stTabs"] button[data-baseweb="tab"] {
        background: transparent;
        color: #64748b;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.6rem 1.4rem;
        border-radius: 10px 10px 0 0;
        border: none;
    }
    [data-testid="stTabs"] button[data-baseweb="tab"]:hover {
        color: #34d399;
        background: #0d1f1a;
    }
    [data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
        background: #0d1f1a;
        color: #10b981;
        border-bottom: 2px solid #10b981;
    }
    [data-testid="stTabs"] [data-baseweb="tab-panel"] {
        background: #111c18;
        border-radius: 0 0 14px 14px;
        padding: 1.4rem;
        border: 1px solid #1f4037;
        border-top: none;
    }
    </style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# 2. CLASS NAMES (29 CROP DISEASE CLASSES)
# NOTE: Replace/reorder to match your model's training class order!
# ------------------------------------------------------------------------------
CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot"
]


# ------------------------------------------------------------------------------
# 3. DISEASE RECOMMENDATIONS & PREVENTION DICTIONARY
# ------------------------------------------------------------------------------
DISEASE_DETAILS = {
    "Apple___Apple_scab": {
        "name": "Apple — Apple Scab",
        "status": "Diseased",
        "description": "Fungal infection (Venturia inaequalis) causing olive-green to brown spots on leaves and fruit.",
        "treatment": "Apply copper-based fungicides or sulfur sprays during early spring bud break. Remove infected fallen leaves.",
        "prevention": "Plant scab-resistant apple varieties. Prune canopy for airflow and sunlight penetration."
    },
    "Apple___Black_rot": {
        "name": "Apple — Black Rot",
        "status": "Diseased",
        "description": "Botryosphaeria obtusa causing frog-eye leaf spots, limb cankers, and black mummified apples.",
        "treatment": "Prune dead branches. Apply captan or thiophanate-methyl during bloom.",
        "prevention": "Remove mummified apples and dead wood from the orchard to cut fungal overwintering."
    },
    "Apple___Cedar_apple_rust": {
        "name": "Apple — Cedar Apple Rust",
        "status": "Diseased",
        "description": "Rust fungus alternating between cedar and apple trees, producing bright orange-yellow leaf spots.",
        "treatment": "Apply myclobutanil or immunox fungicide in early spring when cedar galls swell.",
        "prevention": "Remove nearby eastern red cedar trees or select rust-resistant apple cultivars."
    },
    "Apple___healthy": {
        "name": "Apple — Healthy Leaf",
        "status": "Healthy",
        "description": "Vibrant green apple leaf with intact cell structure and no pathogen lesions.",
        "treatment": "No treatment required. Maintain standard watering and fertilization.",
        "prevention": "Inspect leaves regularly and maintain soil nutrition balance."
    },
    "Blueberry___healthy": {
        "name": "Blueberry — Healthy Leaf",
        "status": "Healthy",
        "description": "Healthy blueberry foliage with strong photosynthetic activity.",
        "treatment": "No chemical treatment needed.",
        "prevention": "Maintain soil pH 4.5–5.5, mulch with pine bark, and irrigate at base."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "name": "Cherry — Powdery Mildew",
        "status": "Diseased",
        "description": "Podosphaera clandestina causing powdery white coating on leaves and young shoots.",
        "treatment": "Spray sulfur or potassium bicarbonate fungicides at first infection signs.",
        "prevention": "Prune for canopy air circulation; avoid excess nitrogen fertilizers."
    },
    "Cherry_(including_sour)___healthy": {
        "name": "Cherry — Healthy Leaf",
        "status": "Healthy",
        "description": "Clean cherry leaf with deep green colour and smooth undamaged margins.",
        "treatment": "No treatment needed.",
        "prevention": "Maintain well-drained soil and standard orchard sanitation."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "name": "Corn — Gray Leaf Spot",
        "status": "Diseased",
        "description": "Cercospora zeae-maydis causing rectangular tan-gray lesions parallel to leaf veins.",
        "treatment": "Apply strobilurin or triazole fungicides before tasseling.",
        "prevention": "Rotate crops with non-host plants such as soybeans."
    },
    "Corn_(maize)___Common_rust_": {
        "name": "Corn — Common Rust",
        "status": "Diseased",
        "description": "Puccinia sorghi producing reddish-brown powdery pustules on both leaf surfaces.",
        "treatment": "Foliar fungicide spray on susceptible hybrids under high humidity.",
        "prevention": "Plant rust-resistant corn hybrids."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "name": "Corn — Northern Leaf Blight",
        "status": "Diseased",
        "description": "Exserohilum turcicum causing large cigar-shaped grayish-green or tan lesions.",
        "treatment": "Apply azoxystrobin or pyraclostrobin fungicides.",
        "prevention": "Use resistant seed hybrids; practice 2-year crop rotation."
    },
    "Corn_(maize)___healthy": {
        "name": "Corn — Healthy Leaf",
        "status": "Healthy",
        "description": "Robust green corn leaf with smooth veins and no blight.",
        "treatment": "No treatment required.",
        "prevention": "Monitor fields during damp weather; maintain nitrogen levels."
    },
    "Grape___Black_rot": {
        "name": "Grape — Black Rot",
        "status": "Diseased",
        "description": "Guignardia bidwellii producing reddish-brown leaf spots and shrivelled black mummified grapes.",
        "treatment": "Apply copper or mancozeb fungicides from bloom until 4 weeks post-bloom.",
        "prevention": "Remove mummified berries during winter pruning; keep canopy open."
    },
    "Grape___Esca_(Black_Measles)": {
        "name": "Grape — Esca (Black Measles)",
        "status": "Diseased",
        "description": "Trunk disease producing tiger-stripe interveinal leaf discoloration.",
        "treatment": "Prune away dead wood and seal large pruning cuts.",
        "prevention": "Avoid pruning during damp weather to reduce fungal entry."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "name": "Grape — Leaf Blight",
        "status": "Diseased",
        "description": "Dark brown irregular spots causing premature leaf drop.",
        "treatment": "Apply copper fungicides post-harvest and during early leaf burst.",
        "prevention": "Clear fallen leaf debris around grape trellises."
    },
    "Grape___healthy": {
        "name": "Grape — Healthy Leaf",
        "status": "Healthy",
        "description": "Healthy grapevine leaf with rich green colour.",
        "treatment": "No treatment needed.",
        "prevention": "Maintain drip irrigation and proper trellising."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "name": "Orange — Citrus Greening (HLB)",
        "status": "Diseased",
        "description": "Bacterial disease spread by psyllids causing yellow leaf mottling and bitter fruit.",
        "treatment": "Remove infected trees promptly to limit vector spread.",
        "prevention": "Control psyllid vectors using systemic insecticides."
    },
    "Peach___Bacterial_spot": {
        "name": "Peach — Bacterial Spot",
        "status": "Diseased",
        "description": "Xanthomonas arboricola causing purple-black spots that drop out (shot-holes).",
        "treatment": "Apply copper sprays during dormancy; oxytetracycline during growing season.",
        "prevention": "Select resistant cultivars; avoid overhead irrigation."
    },
    "Peach___healthy": {
        "name": "Peach — Healthy Leaf",
        "status": "Healthy",
        "description": "Clean green peach foliage with smooth leaf surfaces.",
        "treatment": "No treatment needed.",
        "prevention": "Provide adequate sunlight and balanced nutrients."
    },
    "Pepper,_bell___Bacterial_spot": {
        "name": "Pepper — Bacterial Spot",
        "status": "Diseased",
        "description": "Dark water-soaked leaf spots with yellow margins caused by Xanthomonas.",
        "treatment": "Spray copper bactericides combined with mancozeb.",
        "prevention": "Use certified disease-free seeds; practice crop rotation."
    },
    "Pepper,_bell___healthy": {
        "name": "Pepper — Healthy Leaf",
        "status": "Healthy",
        "description": "Healthy bell pepper leaf with deep green colour.",
        "treatment": "No treatment needed.",
        "prevention": "Ensure good soil drainage; avoid wetting foliage."
    },
    "Potato___Early_blight": {
        "name": "Potato — Early Blight",
        "status": "Diseased",
        "description": "Alternaria solani producing concentric 'target' brown spots on lower leaves.",
        "treatment": "Apply chlorothalonil, mancozeb, or copper fungicides at first signs.",
        "prevention": "Maintain plant vigor with nitrogen; practice 3-year crop rotation."
    },
    "Potato___Late_blight": {
        "name": "Potato — Late Blight",
        "status": "Diseased",
        "description": "Phytophthora infestans causing dark water-soaked lesions with white mold underneath.",
        "treatment": "Apply systemic fungicides (metalaxyl / dimethomorph) immediately.",
        "prevention": "Plant certified seed potatoes; eliminate cull piles."
    },
    "Potato___healthy": {
        "name": "Potato — Healthy Leaf",
        "status": "Healthy",
        "description": "Vibrant green potato leaf with no necrotic spots.",
        "treatment": "No treatment required.",
        "prevention": "Keep foliage dry; use drip irrigation."
    },
    "Raspberry___healthy": {
        "name": "Raspberry — Healthy Leaf",
        "status": "Healthy",
        "description": "Healthy green raspberry leaf with clean serrated edges.",
        "treatment": "No treatment needed.",
        "prevention": "Prune old spent canes annually."
    },
    "Soybean___healthy": {
        "name": "Soybean — Healthy Leaf",
        "status": "Healthy",
        "description": "Clean soybean leaf with lush green colour.",
        "treatment": "No treatment required.",
        "prevention": "Rotate crops; use quality seed varieties."
    },
    "Squash___Powdery_mildew": {
        "name": "Squash — Powdery Mildew",
        "status": "Diseased",
        "description": "White talcum-powder-like fungal growth on upper squash leaf surfaces.",
        "treatment": "Spray neem oil, potassium bicarbonate, or sulfur fungicides.",
        "prevention": "Plant in full sun; maintain adequate spacing."
    },
    "Strawberry___Leaf_scorch": {
        "name": "Strawberry — Leaf Scorch",
        "status": "Diseased",
        "description": "Diplocarpon earlianum causing dark purplish leaf spots.",
        "treatment": "Apply captan or copper fungicides post-harvest.",
        "prevention": "Remove dead leaves in autumn; straw-mulch beds."
    },
    "Strawberry___healthy": {
        "name": "Strawberry — Healthy Leaf",
        "status": "Healthy",
        "description": "Healthy strawberry foliage with clean green margins.",
        "treatment": "No treatment needed.",
        "prevention": "Mulch beds to keep leaves off damp soil."
    },
    "Tomato___Bacterial_spot": {
        "name": "Tomato — Bacterial Spot",
        "status": "Diseased",
        "description": "Small dark water-soaked spots on tomato leaves caused by Xanthomonas species.",
        "treatment": "Apply copper sprays mixed with mancozeb.",
        "prevention": "Avoid overhead watering; sanitize garden tools."
    }
}


# ------------------------------------------------------------------------------
# 4. MODEL LOADER
# ------------------------------------------------------------------------------
MODEL_PATH = "crop_disease_model.keras"

@st.cache_resource(show_spinner=False)
def load_disease_model():
    """
    Loads the trained TensorFlow Keras CNN model.
    Returns (model, status_message, is_loaded).
    """
    if not TF_AVAILABLE:
        return None, "TensorFlow is not installed. Please install it using the command shown below.", False
    if not os.path.exists(MODEL_PATH):
        return None, f"Model file '{MODEL_PATH}' not found in project directory.", False
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model, "Model loaded successfully.", True
    except Exception as e:
        return None, f"Failed to load model: {str(e)}", False


# ------------------------------------------------------------------------------
# 5. PREPROCESSING & PREDICTION ENGINE
# ------------------------------------------------------------------------------
def predict_crop_disease(image: Image.Image, model):
    """
    Preprocesses the uploaded leaf image and runs TF CNN prediction:
    1. Resize to 224x224 pixels
    2. Normalize pixel values by dividing by 255.0
    3. Expand dims to (1, 224, 224, 3) batch format
    4. Run model.predict() and return top class + confidence
    """
    # Step 1: Resize to 224x224
    img_224 = image.resize((224, 224), Image.Resampling.BILINEAR)
    img_array = np.array(img_224, dtype=np.float32)

    # Step 2: Ensure 3-channel RGB
    if img_array.ndim == 2:
        img_array = np.stack((img_array,) * 3, axis=-1)
    elif img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    # Step 3: Normalize pixel values [0, 255] -> [0.0, 1.0]
    img_norm = img_array / 255.0

    # Step 4: Add batch dimension -> (1, 224, 224, 3)
    img_batch = np.expand_dims(img_norm, axis=0)

    # Step 5: Real TF CNN Prediction
    raw_probs = model.predict(img_batch, verbose=0)[0]

    top_idx = int(np.argmax(raw_probs))
    confidence = float(raw_probs[top_idx]) * 100.0
    return top_idx, confidence, raw_probs


# ==============================================================================
# 6. STREAMLIT UI  — Clean, centred, no sidebar
# ==============================================================================

model, model_status_msg, model_is_loaded = load_disease_model()

# ── Hero Banner ──────────────────────────────────────────────────────────────
st.markdown("""
    <div class="hero">
        <h1>🌿 Crop Disease Prediction</h1>
        <p>Upload a leaf photo and get an instant AI-powered disease diagnosis</p>
    </div>
""", unsafe_allow_html=True)



# ── Input Tabs (no orphan radio box) ─────────────────────────────────────────
upload_tab, camera_tab = st.tabs(["📤 Upload Image", "📸 Camera Capture"])

image = None

with upload_tab:
    st.markdown("""
        <p style="color:#94a3b8; font-size:0.9rem; margin:0 0 0.8rem 0;">
            Drag &amp; drop or browse a clear, close-up photo of the crop leaf (JPG, JPEG, PNG).
        </p>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Drop leaf image here", type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
        except Exception as e:
            st.error(f"Error opening image: {e}")

with camera_tab:
    st.markdown("""
        <p style="color:#94a3b8; font-size:0.9rem; margin:0 0 0.8rem 0;">
            Position the crop leaf in good lighting and take a snapshot.
        </p>
    """, unsafe_allow_html=True)
    cam_file = st.camera_input("Take a photo", label_visibility="collapsed")
    if cam_file is not None:
        try:
            image = Image.open(cam_file)
        except Exception as e:
            st.error(f"Error reading camera photo: {e}")

# ── Preview + Predict ─────────────────────────────────────────────────────────
if image is not None:
    # Leaf preview
    st.markdown('<div class="preview-wrap">', unsafe_allow_html=True)
    st.image(image, caption=f"Preview  •  {image.size[0]} × {image.size[1]} px",
             use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Predict button
    predict_clicked = st.button("🔍 Predict Crop Disease", use_container_width=True)

    if predict_clicked:
        with st.spinner("🔬 Running CNN neural network analysis…"):
            top_idx, confidence, probabilities = predict_crop_disease(image, model)

        raw_cls = CLASS_NAMES[top_idx] if top_idx < len(CLASS_NAMES) else f"Class_{top_idx}"
        info = DISEASE_DETAILS.get(raw_cls, {
            "name": raw_cls.replace("___", " — ").replace("_", " "),
            "status": "Unknown",
            "description": "No description available.",
            "treatment": "Consult a local agricultural expert.",
            "prevention": "Practice good field sanitation."
        })

        is_healthy = (info["status"] == "Healthy")

        # ── Result Card ──────────────────────────────────────────────────────
        badge = (
            '<span class="badge-healthy">🟢 Healthy Crop</span>'
            if is_healthy else
            '<span class="badge-diseased">🔴 Disease Detected</span>'
        )
        border_col = "#059669" if is_healthy else "#ef4444"

        st.markdown(f"""
            <div class="result-card" style="border-left:6px solid {border_col};">
                <div class="result-label">Diagnostic Analysis Result</div>
                <div class="result-disease">{info['name']}</div>
                {badge}
                <div class="conf-row">
                    <span class="conf-label">Prediction Confidence</span>
                    <span class="conf-pct">{confidence:.2f}%</span>
                </div>
                <div class="conf-bar-bg">
                    <div class="conf-bar-fill" style="width:{confidence:.2f}%;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # ── Recommendation Tabs ───────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        t1, t2, t3 = st.tabs(["💊 Treatment", "🛡️ Prevention", "🔬 Details"])

        with t1:
            st.markdown(f'<div class="info-box">{info["treatment"]}</div>',
                        unsafe_allow_html=True)
        with t2:
            st.markdown(f'<div class="info-box">{info["prevention"]}</div>',
                        unsafe_allow_html=True)
        with t3:
            st.markdown(f'<div class="info-box">{info["description"]}</div>',
                        unsafe_allow_html=True)
            with st.expander("📈 Top-5 Probability Breakdown"):
                top5 = np.argsort(probabilities)[::-1][:5]
                for idx in top5:
                    cn = CLASS_NAMES[idx] if idx < len(CLASS_NAMES) else f"Class {idx}"
                    cp = float(probabilities[idx]) * 100.0
                    st.write(f"**{cn.replace('___', ' — ')}** — `{cp:.2f}%`")
                    st.progress(min(cp / 100.0, 1.0))

else:
    # Placeholder hint before any image is provided
    st.markdown("""
        <div style="text-align:center; background:#111c18; border:1px dashed #1f4037;
                    border-radius:16px; padding:3rem 1rem; margin-top:1rem;">
            <div style="font-size:2.5rem; margin-bottom:0.6rem;">🌱</div>
            <div style="color:#6ee7b7; font-size:1.05rem; font-weight:600;">
                Upload or capture a crop leaf image above to get started
            </div>
            <div style="color:#64748b; font-size:0.9rem; margin-top:0.4rem;">
                Supports JPG, JPEG, PNG • Up to 200 MB
            </div>
        </div>
    """, unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        🌿 <b>Crop Disease Prediction System</b> &nbsp;|&nbsp; Final Year Engineering Project<br>
        Developed with ❤️ by <a href="#" target="_blank">Hariharan S</a>
    </div>
""", unsafe_allow_html=True)
