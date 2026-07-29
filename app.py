# =============================================================================
# Crop Disease Prediction System — Premium UI
# Developer: Hariharan S
# Framework: Streamlit + TensorFlow MobileNetV2
# =============================================================================

import os, sys, time
import numpy as np
from PIL import Image, ImageOps
import streamlit as st

# Auto-detect Python 3.11 site-packages (portable across machines)
_PY311_CANDIDATES = [
    r"C:\Users\ELCOT\Documents\python311\Lib\site-packages",  # this laptop
    os.path.join(os.path.expanduser("~"), "Documents", "python311", "Lib", "site-packages"),
    r"C:\Python311\Lib\site-packages",
    r"C:\Program Files\Python311\Lib\site-packages",
    r"C:\Program Files (x86)\Python311\Lib\site-packages",
]
for _candidate in _PY311_CANDIDATES:
    if os.path.exists(_candidate) and _candidate not in sys.path:
        sys.path.insert(0, _candidate)
        break

try:
    import tensorflow as tf
    TF_AVAILABLE = True
except Exception as _e:
    TF_AVAILABLE = False
    _TF_ERROR = str(_e)

from disease_info import get_disease_info, is_healthy

# =============================================================================
# PAGE CONFIG
# =============================================================================
st.set_page_config(
    page_title="Crop Disease Prediction — Machine Learning",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =============================================================================
# PREMIUM CSS
# =============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root {
  --emerald:       #10B981;
  --emerald-dark:  #059669;
  --emerald-deep:  #047857;
  --forest:        #064E3B;
  --mint:          #ECFDF5;
  --mint-2:        #D1FAE5;
  --slate:         #1e293b;
  --slate-mid:     #334155;
  --slate-light:   #64748B;
  --white:         #FFFFFF;
  --glass-bg:      rgba(255,255,255,0.82);
  --glass-border:  rgba(16,185,129,0.18);
  --shadow-sm:     0 4px 16px -4px rgba(6,95,70,0.10);
  --shadow-md:     0 12px 40px -12px rgba(6,95,70,0.18);
  --shadow-lg:     0 24px 64px -16px rgba(5,150,105,0.22);
  --r-xl:  28px;
  --r-lg:  20px;
  --r-md:  14px;
  --r-sm:  10px;
}

/* ── Reset Streamlit Chrome ────────────────────────────────── */
[data-testid="stSidebar"],
[data-testid="collapsedControl"],
header[data-testid="stHeader"],
[data-testid="stHeader"],
footer,
div[data-testid="stDecoration"],
[data-testid="stToolbar"] {
  display: none !important;
  height: 0 !important;
  min-height: 0 !important;
  padding: 0 !important;
  margin: 0 !important;
}

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
  font-family: 'Inter', -apple-system, sans-serif !important;
  color: var(--slate) !important;
  -webkit-font-smoothing: antialiased !important;
}

h1, h2, h3, h4, h5, h6 { font-family: 'Sora', sans-serif !important; }

/* ── App Shell ────────────────────────────────────────────── */
.stApp {
  margin-top: 0 !important;
  padding-top: 0 !important;
  background-color: #f8fffe !important;
  background-image:
    radial-gradient(ellipse 80% 60% at 85% -5%,  rgba(52,211,153,0.18) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 10% 105%, rgba(16,185,129,0.13) 0%, transparent 55%),
    radial-gradient(ellipse 40% 40% at 50% 50%,  rgba(209,250,229,0.08) 0%, transparent 70%) !important;
  background-attachment: fixed !important;
}

.stMain, .main, section.main { padding-top: 0 !important; margin-top: 0 !important; }

.main .block-container,
[data-testid="stMainBlockContainer"],
div.block-container {
  max-width: 1160px !important;
  padding: 0.25rem 2rem 4rem 2rem !important;
  margin-top: 0 !important;
}

/* ── Brand bar ────────────────────────────────────────────── */
.brandbar {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 1.25rem 0 0.75rem 0;
  margin-bottom: 0;
  border-bottom: 1px solid rgba(16,185,129,0.1);
}
.brandbar .mark {
  width: 40px; height: 40px;
  border-radius: 12px;
  background: linear-gradient(145deg, #10b981, #047857);
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 6px 18px -4px rgba(16,185,129,0.5);
}
.brandbar .brand-name {
  font-family: 'Sora', sans-serif;
  font-weight: 800;
  font-size: 1.15rem;
  color: var(--forest);
  letter-spacing: -0.02em;
}
.brandbar .brand-tag {
  margin-left: auto;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10.5px;
  font-weight: 600;
  color: var(--emerald-deep);
  background: var(--mint);
  border: 1px solid var(--glass-border);
  padding: 4px 10px;
  border-radius: 999px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

/* ── Hero ─────────────────────────────────────────────────── */
.hero-wrap {
  padding: 2.8rem 0 2rem 0;
}
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--emerald-deep);
  background: var(--mint);
  border: 1px solid var(--glass-border);
  padding: 5px 12px 5px 9px;
  border-radius: 999px;
  margin-bottom: 1.1rem;
}
.eyebrow .dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--emerald);
  animation: pulseDot 2.2s ease-in-out infinite;
}
@keyframes pulseDot {
  0%,100%  { box-shadow: 0 0 0 0   rgba(16,185,129,0.55); }
  50%      { box-shadow: 0 0 0 7px rgba(16,185,129,0);    }
}

.hero-title {
  font-size: clamp(2rem, 3.8vw, 3rem) !important;
  font-weight: 800 !important;
  line-height: 1.1 !important;
  color: var(--forest) !important;
  letter-spacing: -0.025em !important;
  margin: 0 0 0.9rem 0 !important;
}
.hero-title .accent {
  background: linear-gradient(110deg, #10b981 5%, #059669 95%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent !important;
}
.hero-sub {
  font-size: 1.05rem !important;
  line-height: 1.7 !important;
  color: var(--slate-light) !important;
  max-width: 480px;
  margin-bottom: 1.6rem !important;
}

/* ── Trust Chips ──────────────────────────────────────────── */
.trust-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 0; }
.trust-chip {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 12.5px; font-weight: 600; color: var(--forest);
  background: rgba(255,255,255,0.85);
  border: 1px solid rgba(16,185,129,0.2);
  backdrop-filter: blur(8px);
  padding: 7px 13px;
  border-radius: 999px;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.trust-chip:hover {
  border-color: var(--emerald);
  box-shadow: 0 2px 12px rgba(16,185,129,0.15);
}

/* ── Stat Cards ───────────────────────────────────────────── */
.stat-card {
  background: #ffffff;
  border: 1px solid rgba(16,185,129,0.14);
  border-radius: var(--r-lg);
  padding: 1.1rem 1.3rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  align-items: center;
  gap: 13px;
  transition: box-shadow 0.25s, transform 0.25s;
}
.stat-card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }
.stat-card .ico {
  width: 40px; height: 40px; flex-shrink: 0;
  border-radius: 12px;
  background: linear-gradient(145deg, #ecfdf5, #d1fae5);
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 4px 10px -3px rgba(16,185,129,0.25);
}
.stat-card .num {
  font-family: 'Sora', sans-serif; font-weight: 800;
  font-size: 1.3rem; color: var(--forest); line-height: 1;
}
.stat-card .lbl {
  font-size: 0.78rem; color: var(--slate-light);
  font-weight: 500; margin-top: 2px; letter-spacing: 0.01em;
}

/* ── Right hero column vertical centering ─────────────────── */
.upload-center-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 1rem 0;
}

/* ── Dropzone ─────────────────────────────────────────────── */
[data-testid="stFileUploaderDropzone"] {
  background: rgba(236,253,245,0.55) !important;
  border: 2px dashed rgba(16,185,129,0.4) !important;
  border-radius: var(--r-lg) !important;
  padding: 2.4rem 1.5rem !important;
  text-align: center !important;
  transition: all 0.3s ease !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
}
[data-testid="stFileUploaderDropzone"] > div {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  gap: 10px !important;
  width: 100% !important;
}
[data-testid="stFileUploaderDropzone"] section {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
  border-color: var(--emerald) !important;
  background: rgba(209,250,229,0.6) !important;
  transform: translateY(-3px) !important;
  box-shadow: 0 8px 28px rgba(16,185,129,0.12) !important;
}
[data-testid="stFileUploaderDropzone"] button {
  background: linear-gradient(135deg, #10b981, #059669) !important;
  color: #fff !important; border: none !important;
  border-radius: 11px !important;
  font-family: 'Sora', sans-serif !important;
  font-weight: 700 !important;
  padding: 0.55rem 1.8rem !important;
  box-shadow: 0 6px 18px rgba(16,185,129,0.4) !important;
  transition: all 0.22s ease !important;
  margin: 0 auto !important;
  display: block !important;
}
[data-testid="stFileUploaderDropzone"] button:hover {
  box-shadow: 0 10px 26px rgba(16,185,129,0.5) !important;
  transform: translateY(-1px) !important;
}
[data-testid="stFileUploaderDropzone"] span,
[data-testid="stFileUploaderDropzone"] small,
[data-testid="stFileUploaderDropzone"] p {
  text-align: center !important;
  display: block !important;
  width: 100% !important;
}

/* ── Format Pills ─────────────────────────────────────────── */
.dz-formats { display: flex; justify-content: center; gap: 7px; margin-top: 0.9rem; }
.fmt-pill {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10.5px; font-weight: 600;
  color: var(--emerald-deep);
  background: var(--mint);
  border: 1px solid rgba(16,185,129,0.22);
  padding: 3px 9px; border-radius: 6px;
}

/* ── Predict Button ───────────────────────────────────────── */
div[data-testid="stButton"], .stButton {
  display: flex !important;
  justify-content: center !important;
  margin-top: 1.6rem !important;
}
div[data-testid="stButton"] > button, .stButton > button {
  width: 500px !important;
  min-width: unset !important;
  max-width: 100% !important;
  margin-left: auto !important;
  margin-right: auto !important;
  display: block !important;
  padding: 0.8rem 2rem !important;
  font-family: 'Sora', sans-serif !important;
  font-weight: 700 !important;
  font-size: 0.95rem !important;
  letter-spacing: 0.04em !important;
  color: #fff !important;
  background: linear-gradient(135deg, #10b981 0%, #047857 100%) !important;
  border: none !important;
  border-radius: var(--r-md) !important;
  box-shadow: 0 6px 22px rgba(16,185,129,0.38) !important;
  transition: all 0.25s ease !important;
  position: relative !important;
  overflow: hidden !important;
}
div[data-testid="stButton"] > button::after, .stButton > button::after {
  content: "" !important;
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(135deg, rgba(255,255,255,0.15), transparent) !important;
  border-radius: inherit !important;
}
div[data-testid="stButton"] > button:hover, .stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 12px 30px rgba(16,185,129,0.5) !important;
}
div[data-testid="stButton"] > button:active, .stButton > button:active {
  transform: scale(0.97) !important;
}

/* ── Section Divider ──────────────────────────────────────── */
.section-divider {
  display: flex; align-items: center; gap: 1rem;
  margin: 2.2rem 0 1.5rem 0;
}
.section-divider .line { flex: 1; height: 1px; background: rgba(16,185,129,0.15); }
.section-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px; font-weight: 600; letter-spacing: 0.09em;
  text-transform: uppercase; color: var(--emerald-deep);
  background: var(--mint); border: 1px solid var(--glass-border);
  padding: 4px 12px; border-radius: 999px;
}

/* ── Result Anchor ────────────────────────────────────────── */
#result-anchor { scroll-margin-top: 24px; }

/* ── Result Hero Card ─────────────────────────────────────────── */
.result-hero {
  background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 60%, #a7f3d0 100%);
  border: 1.5px solid rgba(16,185,129,0.28);
  border-radius: var(--r-xl);
  padding: 2rem 2.2rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 12px 40px -8px rgba(16,185,129,0.2), 0 2px 8px rgba(16,185,129,0.08);
  animation: slideIn 0.5s cubic-bezier(0.16,1,0.3,1);
}
@keyframes slideIn {
  from { opacity:0; transform: translateY(20px) scale(0.98); }
  to   { opacity:1; transform: translateY(0)   scale(1);    }
}
.result-hero::before {
  content: "";
  position: absolute; top: -50px; right: -50px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(16,185,129,0.15), transparent 70%);
  pointer-events: none;
}
.result-hero::after {
  content: "";
  position: absolute; bottom: -35px; left: -35px;
  width: 160px; height: 160px;
  background: radial-gradient(circle, rgba(52,211,153,0.12), transparent 70%);
  pointer-events: none;
}
.result-tag {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10.5px; font-weight: 600;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--emerald-deep);
  margin-bottom: 0.5rem;
}
.result-disease {
  font-family: 'Sora', sans-serif;
  font-weight: 800; font-size: 1.65rem;
  color: #064E3B; line-height: 1.2;
  letter-spacing: -0.01em;
  margin-bottom: 1rem;
}
.badge-healthy {
  display: inline-flex; align-items: center; gap: 7px;
  background: rgba(16,185,129,0.15);
  border: 1.5px solid rgba(16,185,129,0.5);
  color: #065f46;
  font-weight: 700; font-size: 0.85rem;
  padding: 6px 16px; border-radius: 999px;
}
.badge-diseased {
  display: inline-flex; align-items: center; gap: 7px;
  background: rgba(239,68,68,0.12);
  border: 1.5px solid rgba(239,68,68,0.45);
  color: #b91c1c;
  font-weight: 700; font-size: 0.85rem;
  padding: 6px 16px; border-radius: 999px;
}
.badge-dot { width: 7px; height: 7px; border-radius: 50%; background: currentColor; }

/* ── Metric Bar ───────────────────────────────────────────── */
.metric-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  margin-top: 1.75rem;
  animation: slideIn 0.55s cubic-bezier(0.16,1,0.3,1) 0.1s both;
}
.metric-card {
  background: #ffffff;
  border: 1px solid rgba(16,185,129,0.14);
  border-radius: var(--r-lg);
  padding: 1.1rem 1.3rem;
  box-shadow: var(--shadow-sm);
  position: relative;
  overflow: hidden;
}
.metric-card::before {
  content: "";
  position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #10b981, #047857);
  border-radius: var(--r-lg) var(--r-lg) 0 0;
}
.metric-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10.5px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--slate-light); margin-bottom: 0.4rem;
}
.metric-value {
  font-family: 'Sora', sans-serif;
  font-weight: 800; font-size: 1.6rem;
  color: var(--forest); line-height: 1;
  letter-spacing: -0.02em;
}
.metric-sub {
  font-size: 0.78rem; color: var(--slate-light);
  margin-top: 3px; font-weight: 500;
}

/* ── Progress Bar ─────────────────────────────────────────── */
.conf-bar-wrap { margin-top: 0.75rem; }
.conf-bar-track {
  height: 6px; background: #e2e8f0;
  border-radius: 999px; overflow: hidden;
}
.conf-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #10b981, #059669);
  border-radius: 999px;
  transition: width 1.2s cubic-bezier(0.2,0.8,0.2,1);
}

/* ── Tabs ─────────────────────────────────────────────────── */
[data-baseweb="tab-list"] {
  background: #ffffff !important;
  border-radius: var(--r-md) var(--r-md) 0 0 !important;
  border-bottom: 2px solid rgba(16,185,129,0.15) !important;
  gap: 4px !important; padding: 6px 6px 0 !important;
}
button[data-baseweb="tab"] {
  font-family: 'Sora', sans-serif !important;
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  color: var(--slate-light) !important;
  border-radius: var(--r-sm) var(--r-sm) 0 0 !important;
  padding: 0.55rem 1.1rem !important;
  transition: all 0.18s !important;
}
button[aria-selected="true"] {
  background: var(--mint) !important;
  color: var(--emerald-deep) !important;
  border-bottom: 3px solid var(--emerald) !important;
}
[data-baseweb="tab-panel"] {
  background: #ffffff !important;
  border: 1px solid rgba(16,185,129,0.12) !important;
  border-top: none !important;
  border-radius: 0 0 var(--r-md) var(--r-md) !important;
  padding: 1.5rem !important;
  box-shadow: 0 6px 20px rgba(0,0,0,0.03) !important;
}

/* ── Streamlit Metrics override ───────────────────────────── */
[data-testid="stMetric"] {
  background: #fff !important;
  border: 1px solid rgba(16,185,129,0.14) !important;
  border-radius: var(--r-md) !important;
  padding: 0.9rem 1rem !important;
  box-shadow: var(--shadow-sm) !important;
}
[data-testid="stMetricLabel"] { color: var(--slate-light) !important; font-size: 0.8rem !important; }
[data-testid="stMetricValue"] { color: var(--forest) !important; font-family: 'Sora', sans-serif !important; }

/* ── Progress (Streamlit) ─────────────────────────────────── */
.stProgress > div > div > div {
  background: linear-gradient(90deg, #10b981, #059669) !important;
  border-radius: 999px !important;
}

/* ── Alerts ───────────────────────────────────────────────── */
[data-testid="stAlertContainer"] { border-radius: var(--r-md) !important; }

/* ── Image ────────────────────────────────────────────────── */
[data-testid="stImage"] img {
  border-radius: var(--r-lg) !important;
  box-shadow: var(--shadow-md) !important;
}

/* ── Input Mode Toggle ────────────────────────────────────── */
.input-toggle-row {
  display: flex;
  gap: 8px;
  margin-bottom: 0.9rem;
  justify-content: center;
}
.input-toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: 'Sora', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  padding: 7px 18px;
  border-radius: 999px;
  border: 1.5px solid rgba(16,185,129,0.28);
  background: rgba(255,255,255,0.85);
  color: var(--slate-mid);
  cursor: pointer;
  transition: all 0.2s ease;
  backdrop-filter: blur(6px);
}
.input-toggle-btn.active {
  background: linear-gradient(135deg, #10b981, #059669);
  color: #fff;
  border-color: transparent;
  box-shadow: 0 4px 14px rgba(16,185,129,0.38);
}
.input-toggle-btn:hover:not(.active) {
  border-color: var(--emerald);
  box-shadow: 0 2px 10px rgba(16,185,129,0.15);
}

/* ── Camera widget styling ────────────────────────────────── */
[data-testid="stCameraInput"] > div {
  border-radius: var(--r-lg) !important;
  overflow: hidden !important;
  border: 2px dashed rgba(16,185,129,0.4) !important;
  background: rgba(236,253,245,0.55) !important;
}
[data-testid="stCameraInputButton"] button,
[data-testid="stCameraInput"] button {
  background: linear-gradient(135deg, #10b981, #059669) !important;
  color: #fff !important;
  border: none !important;
  border-radius: 11px !important;
  font-family: 'Sora', sans-serif !important;
  font-weight: 700 !important;
  box-shadow: 0 6px 18px rgba(16,185,129,0.4) !important;
  transition: all 0.22s ease !important;
}
[data-testid="stCameraInputButton"] button:hover,
[data-testid="stCameraInput"] button:hover {
  box-shadow: 0 10px 26px rgba(16,185,129,0.5) !important;
  transform: translateY(-1px) !important;
}

/* ── Footer ───────────────────────────────────────────────── */
.footer-wrap {
  text-align: center;
  padding: 3.5rem 0 2rem 0;
  margin-top: 3.5rem;
  border-top: 1px solid rgba(16,185,129,0.1);
}
.footer-credit {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--slate-light); margin-bottom: 5px;
}
.footer-name {
  font-family: 'Sora', sans-serif;
  font-weight: 800; font-size: 1.2rem;
  color: var(--emerald-deep);
  letter-spacing: -0.01em;
}
.footer-role { font-size: 12px; color: var(--slate-light); margin-top: 2px; }
.footer-line {
  width: 36px; height: 2px; background: var(--emerald);
  opacity: 0.45; margin: 14px auto; border-radius: 2px;
}
.footer-copy { font-size: 11.5px; color: #94a3b8; }
/* ── ALL text — force dark visible color everywhere ───────────── */

/* Markdown containers */
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] span,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] strong,
[data-testid="stMarkdownContainer"] em {
  color: #1e293b !important;
}
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4,
[data-testid="stMarkdownContainer"] h5,
[data-testid="stMarkdownContainer"] h6 {
  color: #064e3b !important;
}
[data-testid="stMarkdownContainer"] code {
  color: #047857 !important;
  background: #ecfdf5 !important;
}

/* Alert / info / success / warning boxes */
[data-testid="stAlertContainer"] p,
[data-testid="stAlertContainer"] span,
[data-testid="stAlertContainer"] div,
[data-testid="stAlertContainer"] li,
[data-testid="stNotification"] p,
[data-testid="stNotification"] span,
div[role="alert"] p,
div[role="alert"] span,
div[role="alert"] div {
  color: #1e293b !important;
}

/* st.warning yellow box */
[data-baseweb="notification"] p,
[data-baseweb="notification"] span,
[data-baseweb="notification"] div {
  color: #713f12 !important;
}

/* Tab labels */
button[data-baseweb="tab"] span,
button[data-baseweb="tab"] p,
button[data-baseweb="tab"] {
  color: #334155 !important;
}
button[aria-selected="true"],
button[aria-selected="true"] span,
button[aria-selected="true"] p {
  color: #047857 !important;
}

/* Tab panel text */
[data-baseweb="tab-panel"] p,
[data-baseweb="tab-panel"] span,
[data-baseweb="tab-panel"] li,
[data-baseweb="tab-panel"] h1,
[data-baseweb="tab-panel"] h2,
[data-baseweb="tab-panel"] h3,
[data-baseweb="tab-panel"] h4 {
  color: #1e293b !important;
}

/* Generic Streamlit text */
.stMarkdown p,
.stMarkdown span,
.stMarkdown li,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
  color: #1e293b !important;
}
.element-container p,
.element-container span,
.element-container li {
  color: #1e293b !important;
}

</style>
""", unsafe_allow_html=True)

# =============================================================================
# CONSTANTS & LOADERS
# =============================================================================
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH   = os.path.join(BASE_DIR, "crop_disease_model.keras")
CLASSES_PATH = os.path.join(BASE_DIR, "class_names.txt")
IMG_SIZE     = 224

@st.cache_data(show_spinner=False)
def load_class_names():
    if not os.path.exists(CLASSES_PATH):
        return None, f"class_names.txt not found at: {CLASSES_PATH}"
    with open(CLASSES_PATH, encoding="utf-8") as f:
        names = [l.strip() for l in f if l.strip()]
    return names, f"{len(names)} classes loaded"

@st.cache_resource(show_spinner=False)
def load_model():
    if not TF_AVAILABLE:
        return None, globals().get("_TF_ERROR", "TensorFlow unavailable")
    if not os.path.exists(MODEL_PATH):
        return None, f"Model file not found: {MODEL_PATH}"
    try:
        m = tf.keras.models.load_model(MODEL_PATH)
        return m, "OK"
    except Exception as ex:
        return None, str(ex)

def predict(img: Image.Image, model, class_names: list) -> dict:
    img = ImageOps.exif_transpose(img).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE), Image.Resampling.BILINEAR)
    arr = np.array(img, dtype=np.float32) / 255.0
    batch = np.expand_dims(arr, 0)
    t0 = time.time()
    probs = model.predict(batch, verbose=0)[0]
    elapsed = time.time() - t0
    top_idx    = int(np.argmax(probs))
    confidence = float(probs[top_idx]) * 100.0
    disease    = class_names[top_idx] if top_idx < len(class_names) else f"Class {top_idx}"
    top5_idx   = np.argsort(probs)[::-1][:5]
    top5 = [(class_names[i] if i < len(class_names) else f"Class {i}", float(probs[i])*100.0) for i in top5_idx]
    return {"disease": disease, "confidence": confidence, "probs": probs, "top5": top5, "elapsed": elapsed}

class_names, cn_msg = load_class_names()
model, m_msg = load_model()

# =============================================================================
# BRAND BAR
# =============================================================================
num_classes = len(class_names) if class_names else 38
st.markdown(f"""
<div class="brandbar">
  <div class="mark">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M11 20A7 7 0 0 1 4 13a7 7 0 0 1 7-7 9 9 0 0 1 9 9c0 3-2 7-9 7Z"/>
      <path d="M11 6c-1 4-2 7-6 9"/>
    </svg>
  </div>
  <span class="brand-name">Crop Disease Prediction</span>
  <span class="brand-tag">AI · Machine Learning</span>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# HERO SECTION
# =============================================================================
h_left, h_right = st.columns([1.1, 0.9], gap="large")

with h_left:
    st.markdown(f"""
    <div class="hero-wrap">
      <div class="eyebrow"><span class="dot"></span>AI-Powered Plant Diagnostics</div>
      <h1 class="hero-title">AI-Powered <span class="accent">Crop Leaf Disease</span><br>Prediction</h1>
      <p class="hero-sub">Upload a crop leaf image and receive an instant disease prediction using machine learning.</p>
      <div class="trust-row">
        <div class="trust-chip">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h7l-1 8 10-12h-7l1-8Z"/></svg>
          Instant results
        </div>
        <div class="trust-chip">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
          Machine Learning
        </div>
        <div class="trust-chip">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="m9 12 2 2 4-4"/></svg>
          {num_classes} Crop Classes
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with h_right:
    st.markdown('<div class="upload-center-wrap">', unsafe_allow_html=True)

    # ── Input mode toggle (Upload / Camera) ───────────────────────────
    if "input_mode" not in st.session_state:
        st.session_state["input_mode"] = "upload"

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        upload_active = "active" if st.session_state["input_mode"] == "upload" else ""
        if st.button(
            "📁  Upload Image",
            key="btn_upload_mode",
            use_container_width=True,
            type="primary" if st.session_state["input_mode"] == "upload" else "secondary",
        ):
            st.session_state["input_mode"] = "upload"
            st.rerun()
    with col_btn2:
        if st.button(
            "📷  Take Photo",
            key="btn_camera_mode",
            use_container_width=True,
            type="primary" if st.session_state["input_mode"] == "camera" else "secondary",
        ):
            st.session_state["input_mode"] = "camera"
            st.rerun()

    # ── Show the appropriate input widget ────────────────────────────
    uploaded = None
    camera_img = None

    if st.session_state["input_mode"] == "upload":
        uploaded = st.file_uploader(
            "Select a leaf photo",
            type=["jpg", "jpeg", "png", "webp"],
            key="leaf_upload",
            label_visibility="collapsed"
        )
        st.markdown("""
        <div class="dz-formats">
          <span class="fmt-pill">JPG</span>
          <span class="fmt-pill">JPEG</span>
          <span class="fmt-pill">PNG</span>
          <span class="fmt-pill">WEBP</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        camera_img = st.camera_input(
            "Point camera at a crop leaf and capture",
            key="leaf_camera",
            label_visibility="collapsed"
        )
        st.markdown("""
        <div class="dz-formats" style="margin-top:0.7rem;">
          <span class="fmt-pill">📷 Live Camera</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Guards
if model is None:
    st.error(f"Model load failed: {m_msg}")
    st.stop()
if class_names is None:
    st.error(f"Class names error: {cn_msg}")
    st.stop()


disp_img = None
img_source = uploaded if uploaded is not None else camera_img
if img_source:
    try:
        raw_img = Image.open(img_source)
        disp_img = ImageOps.exif_transpose(raw_img).convert("RGB")
        is_camera = (camera_img is not None and uploaded is None)
        caption = "📷 Camera Capture" if is_camera else "Uploaded Leaf Image"
        st.markdown("<br>", unsafe_allow_html=True)
        col_img, col_info = st.columns([1, 1], gap="medium")
        with col_img:
            st.image(disp_img, caption=caption, use_container_width=True)
        with col_info:
            st.success("**Image Loaded Successfully**")
            if is_camera:
                st.write("**Source:** `Camera Capture`")
            else:
                st.write(f"**Filename:** `{uploaded.name}`")
                st.write(f"**File Size:** `{uploaded.size / 1024:.1f} KB`")
            st.write(f"**Dimensions:** `{disp_img.width} × {disp_img.height} px`")
    except Exception as ex:
        st.error(f"Invalid image file: {ex}")
        disp_img = None

# =============================================================================
# PREDICT BUTTON & RESULTS
# =============================================================================
if disp_img is not None:
    predict_btn = st.button("Predict Disease")

    if predict_btn:
        try:
            with st.spinner("Analysing leaf & running ML inference..."):
                res = predict(disp_img, model, class_names)

            disease    = res["disease"]
            confidence = res["confidence"]
            elapsed    = res["elapsed"]
            top5       = res["top5"]
            healthy    = is_healthy(disease)

            # ── Auto-scroll to result ──────────────────────────────────────
            st.markdown("""
            <script>
              (function() {
                function scrollToResult() {
                  var el = document.getElementById('result-anchor');
                  if (el) {
                    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                  } else {
                    setTimeout(scrollToResult, 120);
                  }
                }
                setTimeout(scrollToResult, 300);
              })();
            </script>
            """, unsafe_allow_html=True)

            # ── Result Section ────────────────────────────────────────────
            st.markdown("""
            <div class="section-divider">
              <div class="line"></div>
              <div class="section-label">Diagnosis Result</div>
              <div class="line"></div>
            </div>
            <div id="result-anchor"></div>
            """, unsafe_allow_html=True)

            badge_html  = f'<div class="badge-healthy"><span class="badge-dot"></span>Healthy — No Infection</div>' if healthy else f'<div class="badge-diseased"><span class="badge-dot"></span>Disease Detected — Action Required</div>'
            conf_pct    = int(confidence)

            st.markdown(f"""
            <div class="result-hero">
              <div class="result-tag">Prediction Complete</div>
              <div class="result-disease">{disease}</div>
              {badge_html}
            </div>
            """, unsafe_allow_html=True)

            # ── Custom Metrics Row ────────────────────────────────────────
            reliability = "High" if confidence >= 90 else "Moderate" if confidence >= 75 else "Low"
            st.markdown(f"""
            <div class="metric-row">
              <div class="metric-card">
                <div class="metric-label">Certainty Score</div>
                <div class="metric-value">{confidence:.1f}%</div>
                <div class="conf-bar-wrap">
                  <div class="conf-bar-track">
                    <div class="conf-bar-fill" style="width:{min(confidence,100):.1f}%"></div>
                  </div>
                </div>
              </div>
              <div class="metric-card">
                <div class="metric-label">Inference Speed</div>
                <div class="metric-value">{elapsed*1000:.0f}<span style="font-size:1rem;font-weight:600;"> ms</span></div>
                <div class="metric-sub">Neural network runtime</div>
              </div>
              <div class="metric-card">
                <div class="metric-label">Model Reliability</div>
                <div class="metric-value" style="font-size:1.35rem;">{reliability}</div>
                <div class="metric-sub">Confidence</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            # ── Disease Information Tabs ──────────────────────────────────
            st.markdown("""
            <div class="section-divider" style="margin-top:2rem;">
              <div class="line"></div>
              <div class="section-label">Disease & Care Guide</div>
              <div class="line"></div>
            </div>
            """, unsafe_allow_html=True)

            info = get_disease_info(disease)
            tab_desc, tab_symp, tab_treat, tab_prev, tab_top5 = st.tabs([
                "Description", "Symptoms", "Treatment", "Prevention", "Top-5 Probabilities"
            ])

            with tab_desc:
                st.markdown("#### About the Disease")
                st.info(info.get("description", "N/A"))
                st.markdown("#### Pathogen / Cause")
                st.write(info.get("cause", "N/A"))

            with tab_symp:
                st.markdown("#### Observed Symptoms")
                st.warning(info.get("symptoms", "N/A"))

            with tab_treat:
                col_o, col_c = st.columns(2)
                with col_o:
                    st.markdown("#### Organic Treatment")
                    st.success(info.get("organic_treatment", "N/A"))
                with col_c:
                    st.markdown("#### Chemical Treatment")
                    st.warning(info.get("chemical_treatment", "N/A"))

            with tab_prev:
                st.markdown("#### Prevention & Field Management")
                st.success(info.get("prevention", "N/A"))

            with tab_top5:
                st.markdown("#### Model Output Probabilities")
                for rank, (c_name, c_prob) in enumerate(top5):
                    label = "Top Match" if rank == 0 else f"#{rank+1}"
                    bar_color = "#10b981" if rank == 0 else "#059669" if rank == 1 else "#6b7280"
                    st.markdown(f"""
                    <div style="margin-bottom:0.85rem;">
                      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
                        <span style="font-family:'Sora',sans-serif;font-weight:700;font-size:0.88rem;color:#1e293b;">
                          <span style="color:{bar_color};font-weight:800;">{label}</span>
                          &nbsp;—&nbsp;{c_name}
                        </span>
                        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.82rem;font-weight:600;
                                     color:#ffffff;background:{bar_color};padding:2px 9px;border-radius:999px;">
                          {c_prob:.2f}%
                        </span>
                      </div>
                      <div style="height:8px;background:#e2e8f0;border-radius:999px;overflow:hidden;">
                        <div style="height:100%;width:{min(c_prob,100):.2f}%;
                                    background:linear-gradient(90deg,{bar_color},{bar_color}cc);
                                    border-radius:999px;transition:width 0.8s ease;"></div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)

        except Exception as err:
            st.error(f"Prediction error: {err}")

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("""
<div class="footer-wrap">
  <div class="footer-credit">Designed &amp; Developed by</div>
  <div class="footer-name">Hariharan S</div>
  <div class="footer-role">Developer</div>
  <div class="footer-line"></div>
  <div class="footer-copy">&copy; 2026 Crop Disease Prediction System</div>
</div>
""", unsafe_allow_html=True)
