import streamlit as st
import pandas as pd
import io

# Page Configuration - Set title and wide layout
st.set_page_config(page_title="AI Solutions Studio", layout="wide", page_icon="🤖")

# --- Custom Styling (Optional but nice) ---
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.5rem !important;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .service-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown('<div class="main-header">Custom AI & Python Automation Solutions</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">I help businesses automate repetitive tasks and leverage AI for better productivity.</div>', unsafe_allow_html=True)

st.divider()

# --- Section 1: Portfolio (AI Imagery Showcase) ---
st.header("📸 AI Imagery Portfolio")
st.write("Examples of photorealistic and high-quality images I can generate using AI tools.")

# Creating 3 columns for portfolio images
col1, col2, col3 = st.columns(3)

# Option A: Using Free Placeholder Image Links (You can change these URLs)
# Example Links from Unsplash (for demo)
img_url1 = "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=600&auto=format&fit=crop" # AI Robot
img_url2 = "https://images.unsplash.com/photo-1549497538-303791108f94?q=80&w=600&auto=format&fit=crop" # Professional Watch
img_url3 = "https://images.unsplash.com/photo-1598128558393-70ff21433be0?q=80&w=600&auto=format&fit=crop" # Modern Headphone

with col1:
    st.image(img_url1, caption="AI Concept Visual", use_container_width=True)
with col2:
    st.image(img_url2, caption="Realistic Product Photography", use_container_width=True)
with col3:
    st.image(img_url3, caption="Commercial Style Branding Image", use_container_width=True)

# Tip for user: "For your final website, replace these URLs with links to images you generated via AI."

st.divider()

# --- Section 2: Live Demo Tools (Data Cleaner & Text Analyzer) ---
st.header("🛠️ Live Demo Tools")
st.write("Test these interactive tools to see how Python solves real problems.")

# Two tabs for different tools
tab1, tab2 = st.tabs(["🧹 Data Cleaner Tool", "📝 Text Analyzer"])

with tab1:
    st.subheader("Automated CSV Data Cleaner")
    st.write("Upload a messy CSV file, and I'll clean it (remove empty rows, duplicates).")
    
    # Simple example CSV data for client to copy-paste and test
    st.info("💡 Pro Tip: Try uploading a CSV file with empty lines or duplicate rows.")

    uploaded_file = st.file_uploader("Upload your messy CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            # Read the CSV
            df = pd.read_csv(uploaded_file)
            st.write("### Original (Messy) Data:")
            st.dataframe(df.head(10))

            # --- Cleaning Logic (Python Power!) ---
            # 1. Remove rows with all empty cells
            df_cleaned = df.dropna(how='all')
            # 2. Remove duplicate rows
            df_cleaned = df_cleaned.drop_duplicates()
            # 3. Trim whitespace from string columns (optional but good)
            # (Example of real cleaning)

            st.write("### Cleaned Data:")
            st.dataframe(df_cleaned.head(10))
            
            # --- Provide Cleaned File for Download ---
            # Convert DF to CSV in memory
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
    st.write("Paste your business text, feedback, or data for instant analysis.")
    
    text_input = st.text_area("Enter text here (e.g., customer review):")
    
    if st.button("Analyze Text"):
        if text_input:
            # --- Text Processing Logic ---
            words = text_input.split()
            word_count = len(words)
            char_count = len(text_input)
            unique_words = len(set(words))

            st.success("✅ Analysis Complete!")
            # Display results in 3 metrics
            m1, m2, m3 = st.columns(3)
            m1.metric("Word Count", word_count)
            m2.metric("Character Count", char_count)
            m3.metric("Unique Words", unique_words)
            
            # Optional: Add Sentiment analysis later with libraries like TextBlob

        else:
            st.warning("Please enter some text first.")

st.divider()

# --- Section 3: Contact & Hire Me ---
st.header("🤝 Let's Collaborate")
st.write("Are you ready to automate your workflow or integrate AI into your business?")

# Custom style for freelance button
st.markdown('<a href="YOUR_FIVERR_OR_UPWORK_PROFILE_LINK" target="_blank"><button style="background-color: #4CAF50; color: white; padding: 12px 24px; border: none; border-radius: 5px; cursor: pointer; font-size: 1rem;">Hire Me on Freelance Platform</button></a>', unsafe_allow_html=True)
st.write("---")
st.write("Designed and Developed by [Muhammad Farooq]")