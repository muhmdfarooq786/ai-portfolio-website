import streamlit as st
import pandas as pd
import io

# Page Configuration
st.set_page_config(page_title="AI Solutions Studio", layout="wide", page_icon="🤖")

# --- CUSTOM CSS FOR DARK THEME & CONTRAST ---
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #121212;
    }
    
    /* Headers - Make them white for contrast */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }
    
    /* Global text - Make it light grey */
    .stMarkdown p {
        color: #E0E0E0 !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background-color: #4CAF50; /* Green */
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    
    /* DataFrame text - ensure readability */
    div[data-testid="stDataFrame"] {
        color: black;
    }

    /* Custom classes from previous code (updated for dark theme) */
    .main-header {
        font-size: 3rem !important;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem !important;
        color: #FFFFFF; /* Green Color */
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
# Title simplified and centered
st.markdown('<div class="main-header">MUHAMMAD FAROOQ</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI Specialist | Python Automation Expert</div>', unsafe_allow_html=True)

st.divider()

# --- PORTFOLIO SECTION (AI IMAGERY SHOWCASE) ---
st.header("📸 AI Imagery Portfolio")
st.write("Examples of high-quality, professional images generated using advanced AI tools.")

col1, col2, col3 = st.columns(3)

# New Direct Links (Guaranteed to load)
img_url1 = "https://cdn.pixabay.com/photo/2023/12/12/10/59/ai-generated-8445101_1280.jpg" # Professional AI Visual
img_url2 = "https://cdn.pixabay.com/photo/2023/12/12/10/59/ai-generated-8445102_1280.jpg" # Futuristic Technology Visual
img_url3 = "https://cdn.pixabay.com/photo/2023/12/12/10/59/ai-generated-8445100_1280.jpg" # Clean Product Aesthetic (New Attractive Image)

with col1:
    st.image(img_url1, caption="AI Concept Visual", use_container_width=True)
with col2:
    st.image(img_url2, caption="Advanced Tech Concept", use_container_width=True)
with col3:
    st.image(img_url3, caption="Realistic Product Photography", use_container_width=True) # New Label

st.divider()

# --- TOOLS SECTION (LIVE DEMO) ---
st.header("🛠️ Interactive AI Tools")
st.write("Test these live tools to see Python and AI solving business data problems.")

tab1, tab2 = st.tabs(["🧹 Data Cleaner Tool", "📝 Text Analyzer"])

with tab1:
    st.subheader("Automated CSV Data Cleaner")
    st.write("Upload a messy CSV file, and I'll clean it instantly (remove empty rows, duplicates).")
    uploaded_file = st.file_uploader("Upload your messy CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            # --- Python Power Logic ---
            df = pd.read_csv(uploaded_file)
            st.write("### Original (Messy) Data Preview:")
            st.dataframe(df.head(5))

            df_cleaned = df.dropna(how='all').drop_duplicates()
            st.write("### Cleaned Data Preview:")
            st.dataframe(df_cleaned.head(5))
            
            csv_buffer = io.StringIO()
            df_cleaned.to_csv(csv_buffer, index=False)
            csv_string = csv_buffer.getvalue()

            st.download_button(
                label="📥 Download Cleaned CSV",
                data=csv_string,
                file_name="cleaned_data.csv",
                mime="text/csv"
            )
            st.success("Data cleaning successful!")

        except Exception as e:
            st.error(f"Error processing file: {e}")

with tab2:
    st.subheader("Smart Text Analyzer")
    text_input = st.text_area("Paste text here (e.g., customer review):")
    if st.button("Analyze Now"):
        if text_input:
            word_count = len(text_input.split())
            unique_words = len(set(text_input.split()))
            st.success("Analysis Complete!")
            # Metrics show up clearly in dark theme
            st.metric("Total Words", word_count)
            st.metric("Unique Words", unique_words)
        else:
            st.warning("Please enter text first.")

st.divider()

# --- HIRE ME / CONTACT SECTION ---
st.header("🤝 Let's Collaborate")
st.write("Are you looking for a custom AI solution, API integration, or Python automation?")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### Contact Info")
    # Simple clear emojis used
    st.write("📧 **Email:**muhmdfarooq786@gmail.com") # UPDATE THIS
    st.write("📞 **Phone:** +971 581796545") # UPDATE THIS
    st.write("📞 **Phone:** +92 3411898419") # UPDATE THIS
    st.write("📍 **Location:** Dubai, UAE")

with col_right:
    st.markdown("### Hire Me")
    st.write("Ready to scale your business with smart technology.")
    # Professional dark theme button with contrasting white writing
    st.markdown('<a href="YOUR_FIVERR_PROFILE_LINK" target="_blank"><button style="background-color: #4CAF50; color: white; padding: 12px 24px; border: none; border-radius: 5px; cursor: pointer; font-size: 1rem;">View Fiverr Profile</button></a>', unsafe_allow_html=True) # UPDATE THIS

st.markdown("---")
st.markdown("<p style='text-align: center; color: #FFFFFF;'> Designed and Developed by Muhammad Farooq | © 2026</p>", unsafe_allow_html=True)
