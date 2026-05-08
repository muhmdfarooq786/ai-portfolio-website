import streamlit as st
import pandas as pd
import io

# Page Configuration
st.set_page_config(page_title="AI Solutions Studio", layout="wide", page_icon="🤖")

# --- DARK THEME & CUSTOM STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stApp {
        background-color: #0e1117;
    }
    .main-title {
        font-size: 3.5rem !important;
        color: #4CAF50; /* Green Color */
        text-align: center;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.2rem !important;
        color: #cccccc;
        text-align: center;
        margin-bottom: 2rem;
    }
    footer {
        background-color: #1a1c23;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
# Yahan Apna Asli Naam Likhein
st.markdown('<p class="main-title">MUHAMMAD FAROOQ</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI Engineer & Python Automation Expert</p>', unsafe_allow_html=True)

st.divider()

# --- PORTFOLIO SECTION ---
st.header("📸 AI Imagery Portfolio")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=600&auto=format&fit=crop", caption="AI Visualization")
with col2:
    st.image("https://images.unsplash.com/photo-1549497538-303791108f94?q=80&w=600&auto=format&fit=crop", caption="Product Concept")
with col3:
    st.image("https://images.unsplash.com/photo-1598128558393-70ff21433be0?q=80&w=600&auto=format&fit=crop", caption="Modern Branding")

st.divider()

# --- TOOLS SECTION ---
st.header("🛠️ Interactive AI Tools")
tab1, tab2 = st.tabs(["🧹 Data Cleaner", "📝 Text Analyzer"])

with tab1:
    st.subheader("Smart CSV Cleaner")
    uploaded_file = st.file_uploader("Upload Messy Data", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Cleaned Data Preview:")
        st.dataframe(df.dropna().drop_duplicates().head(5))

with tab2:
    st.subheader("Fast Text Analyzer")
    text = st.text_area("Paste text for analysis:")
    if st.button("Analyze"):
        st.info(f"Analysis: {len(text.split())} words found.")

st.divider()

# --- CONTACT INFO SECTION ---
st.header("📩 Get In Touch")
col_a, col_b = st.columns(2)

with col_a:
    st.write("### Contact Details")
    st.write("📧 **Email:** muhmdfarooq786@gmail.com") # Apna email likhein
    st.write("📞 **Phone:** +971 581796545") # Apna number likhein
    st.write("📞 **Phone:** +92 3411898419") # Apna number likhein
    st.write("📍 **Location:** Dubai, UAE")

with col_b:
    st.write("### Hire Me")
    st.write("Available for Freelance AI & Python Projects.")
    st.markdown("[Visit My Upwork Profile](#)") # Apna link dalien

st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 Muhammad Farooq | Built with Python & Streamlit</p>", unsafe_allow_html=True)