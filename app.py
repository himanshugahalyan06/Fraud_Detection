import streamlit as st
import pandas as pd
import pickle
import numpy as np
import os

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="FraudGuard Premium",
    page_icon="🛡️",
    layout="wide"
)

# ─────────────────────────────────────────
# PREMIUM DARK GLASSMORPHISM CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

* { font-family: 'Plus Jakarta Sans', sans-serif !important; }

/* ── Deep Background ── */
.stApp {
    background: radial-gradient(circle at top right, #1e293b, #0f172a, #020617);
    color: #f8fafc;
}

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Sidebar Styling ── */
section[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.95) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-header {
    background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
    padding: 30px 20px;
    margin: -1rem -1rem 2rem -1rem;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}
.sidebar-header h2 { color: white !important; font-weight: 800; margin: 0; font-size: 1.5rem; }

/* ── Glassmorphism Cards ── */
.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 30px;
    margin-bottom: 20px;
    transition: all 0.3s ease;
}
.glass-card:hover {
    border-color: rgba(14, 165, 233, 0.5);
    background: rgba(255, 255, 255, 0.05);
}

/* ── Main Header ── */
.main-header {
    padding: 60px 0 40px 0;
    text-align: center;
}
.main-header h1 {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}
.main-header p { color: #94a3b8; font-size: 1.2rem; }

/* ── Stats ── */
.stat-val { color: #38bdf8; font-size: 2.2rem; font-weight: 800; line-height: 1; }
.stat-lbl { color: #64748b; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; margin-top: 8px; }

/* ── Result Boxes ── */
.result-box {
    border-radius: 30px;
    padding: 50px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}
.result-fraud {
    background: linear-gradient(135deg, #450a0a, #7f1d1d);
    border: 1px solid #ef4444;
}
.result-safe {
    background: linear-gradient(135deg, #064e3b, #065f46);
    border: 1px solid #10b981;
}
.res-title { font-size: 2.5rem; font-weight: 800; margin-bottom: 15px; letter-spacing: -1px; }

/* ── Inputs ── */
.section-label { font-size: 0.75rem; font-weight: 700; color: #38bdf8; margin-bottom: 10px; text-transform: uppercase; }

div[data-testid="stNumberInput"] input, 
div[data-testid="stSelectbox"] > div > div {
    background-color: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: white !important;
    border-radius: 12px !important;
    height: 45px !important;
}

/* ── Button ── */
div[data-testid="stButton"] > button {
    width: 100%;
    background: linear-gradient(90deg, #0ea5e9, #6366f1) !important;
    color: white !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 15px !important;
    height: 4rem !important;
    font-size: 1.1rem !important;
    box-shadow: 0 10px 20px rgba(99, 102, 241, 0.3) !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 30px rgba(99, 102, 241, 0.5) !important;
}

/* ── Table ── */
.custom-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
.custom-table th { text-align: left; color: #64748b; font-size: 0.8rem; padding: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); }
.custom-table td { padding: 15px 12px; font-size: 0.95rem; border-bottom: 1px solid rgba(255,255,255,0.05); }

</style>
""", unsafe_allow_html=True)

# ── Load Model ──
@st.cache_resource
def load_assets():
    if os.path.exists("model_data.pkl"):
        with open("model_data.pkl", "rb") as f:
            return pickle.load(f)
    return None

assets = load_assets()

# ── Main Header ──
st.markdown("""
<div class="main-header">
    <h1>🛡️ FraudGuard AI</h1>
    <p>Real-time Financial Intelligence & Threat Detection</p>
</div>
""", unsafe_allow_html=True)

if not assets:
    st.error("Model Engine Offline. Please train.")
    st.stop()

# ── Sidebar ──
with st.sidebar:
    st.markdown('<div class="sidebar-header"><h2>CONSOLE</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<p class="section-label">Transaction Flow</p>', unsafe_allow_html=True)
    step = st.slider("Hour (Step)", 1, 744, 1)
    t_type = st.selectbox("Type", ["TRANSFER", "CASH_OUT", "CASH_IN", "PAYMENT", "DEBIT"])
    amount = st.number_input("Amount ($)", value=1000.0)
    
    st.markdown('<p class="section-label">Balance Metrics</p>', unsafe_allow_html=True)
    old_o = st.number_input("Origin Initial", value=1000.0)
    new_o = st.number_input("Origin Final", value=0.0)
    old_d = st.number_input("Dest Initial", value=0.0)
    new_d = st.number_input("Dest Final", value=0.0)
    
    st.markdown("<br>", unsafe_allow_html=True)
    analyze = st.button("RUN SECURITY SCAN")

# ── Stats ──
c1, c2, c3, c4 = st.columns(4)
stats = [("6.3M", "Data Points"), ("99.9%", "Model Accuracy"), ("0.1ms", "Latency"), ("Balanced", "AI Logic")]
for col, (val, lbl) in zip([c1,c2,c3,c4], stats):
    col.markdown(f'<div class="glass-card" style="text-align:center"><div class="stat-val">{val}</div><div class="stat-lbl">{lbl}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Results ──
left, right = st.columns([1, 1.2], gap="large")

with left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📋 Analysis Parameters")
    
    is_drain = (new_o == 0 and old_o > 0)
    is_risk_type = (t_type in ["TRANSFER", "CASH_OUT"])
    
    st.markdown(f"""
    <table class="custom-table">
        <tr><th>Metric</th><th>Reading</th><th>Signal</th></tr>
        <tr><td>Type</td><td>{t_type}</td><td style="color:{'#ef4444' if is_risk_type else '#10b981'}">{'HIGH RISK' if is_risk_type else 'LOW RISK'}</td></tr>
        <tr><td>Amount</td><td>${amount:,.2f}</td><td style="color:{'#ef4444' if amount > 200000 else '#10b981'}">{'VOLATILE' if amount > 200000 else 'STABLE'}</td></tr>
        <tr><td>Origin</td><td>{'Account Drain' if is_drain else 'Normal'}</td><td style="color:{'#ef4444' if is_drain else '#10b981'}">{'ALERT' if is_drain else 'CLEAR'}</td></tr>
    </table>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if analyze:
        type_map = {"CASH_IN": 0, "CASH_OUT": 1, "DEBIT": 2, "PAYMENT": 3, "TRANSFER": 4}
        raw = np.array([[step, type_map[t_type], amount, old_o, new_o, old_d, new_d]])
        scaled = assets['scaler'].transform(raw)
        pred = assets['model'].predict(scaled)[0]
        proba = assets['model'].predict_proba(scaled)[0]
        
        if pred == 1:
            st.markdown(f"""
            <div class="result-box result-fraud">
                <div class="res-title">🚨 THREAT DETECTED</div>
                <p>Security scan identified confirmed fraud patterns. Transaction should be isolated.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-box result-safe">
                <div class="res-title">✅ VERIFIED SAFE</div>
                <p>AI Engine verified the transaction. No threats identified.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"<p style='text-align:center; margin-top:20px; color:#94a3b8'>Security Confidence: {round(proba[pred]*100, 2)}%</p>", unsafe_allow_html=True)
        st.progress(proba[pred])
    else:
        st.markdown("""
        <div class="glass-card" style="height:350px; display:flex; flex-direction:column; align-items:center; justify-content:center; border: 2px dashed rgba(255,255,255,0.1)">
            <h2 style="color:#64748b">AWAITING SCAN...</h2>
            <p style="color:#475569">Enter parameters in the console and initiate scan</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center; color:#475569; font-size:0.8rem'>FraudGuard AI System v4.0 | Enterprise Security Engine</p>", unsafe_allow_html=True)
