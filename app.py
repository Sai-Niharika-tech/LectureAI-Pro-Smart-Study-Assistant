import streamlit as st
import os
import time
from engine import process_any_file

# 1. Page Config
st.set_page_config(page_title="LectureAI Pro", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    
    h1 {
        color: #3174b7 !important;
        
    }
    
    [data-testid="stSidebar"] section[data-testid="stSidebarNav"] span, 
    [data-testid="stSidebar"] .stMarkdown p {
        color: white !important;
        
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.title(" 📘 Smart Study Assistant")
    st.markdown("---")
    
    # NEW: Navigation for About Section
    page = st.sidebar.radio("Navigate", ["Home/Generator", "About Project"])
    
    
    
    # Only show input options if on Generator page
    if page == "Home/Generator":
        st.markdown("---")
        option = st.radio("Choose Input Method:", ("📁 Upload File", "🎙️ Record Live"))
    
    st.markdown("---")
    # RESET BUTTON LOGIC
    if st.button("🔄 Reset ", use_container_width=True):
        # Clear all stored data
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

    st.divider()

# --- PAGE LOGIC ---

if page == "About Project":
    # 4. About Section UI
    st.markdown("<h1 style='color: #020a2e'>ℹ️ About LectureAI Pro</h1>", unsafe_allow_html=True)
    
    col_about, col_dev = st.columns([2, 1], gap="large")
    
    with col_about:
        st.write("### 🎯 Project Goal")
        st.write("""
        LectureAI Pro is a project designed to assist students in converting 
        complex lecture materials like Video and Audio into organized study kits. It has File upload and Live Record optons for ease of use. Using Generative AI, the system 
        identifies key academic topics, generates technical notes, and creates practice 
        quizzes to enhance learning retention.
        """)
        
        st.write("### ✨ Key Features")
        st.write("- **Intelligent Analysis**: Powered by Gemini 2.5 Flash for rapid content processing.")
        st.write("- **Multi-format Support**: Handles Video, Audio, and PDF inputs seamlessly.")
        st.write("- **Has Live Recording Option**: Capture and analyze lectures in real-time.")
        st.write("- **Supports Multiple Languages**: Can process content in various languages, like Hindi, Telugu, English, etc.")
        st.write("- **Visual Anchoring**: Detects and describes critical visual moments in video lectures.")
        st.write("- **Interactive Quizzing**: Automatically formats MCQs with an included answer key.")

    with col_dev:
        st.write("### 👩‍💻 Developer Info")
        st.info("**Name:** Venkata Sai Niharika Sirikonda\n\n**Department:** Computer Science\n\n")

else:
    # 4. Main Generator UI (Your Existing Logic)
    st.markdown("<h1 style='color: #020a2e'>🎓 LectureAI Pro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: rgb(3, 17, 62)'>✨ Transform your lectures into beautiful, organized study kits.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("📤 Input")
        input_data = None
        if option == "📁 Upload File":
            input_data = st.file_uploader("📤 Upload Lecture (MP4, MP3, PDF, Video)", type=['mp3', 'mp4', 'pdf', 'm4a', 'wav'])
        else:
            input_data = st.audio_input("🎙️ Record live lecture")

        if input_data:
            if st.button("🚀 Generate Study Materials", type="primary", use_container_width=True):
                # Save local temp file
                temp_path = f"temp_{int(time.time())}_{input_data.name if hasattr(input_data, 'name') else 'live.wav'}"
                with open(temp_path, "wb") as f:
                    f.write(input_data.getbuffer())

                with st.status("AI is analyzing...", expanded=True) as status:
                    try:
                        # Detect Category
                        if hasattr(input_data, 'type') and input_data.type == "application/pdf":
                            cat = "PDF Document"
                        elif hasattr(input_data, 'type') and "video" in input_data.type:
                            cat = "Video Lecture"
                        else:
                            cat = "Audio Recording"

                        # Run Engine
                        st.session_state['result'] = process_any_file(temp_path, cat)
                        status.update(label="✅ Analysis Complete!", state="complete", expanded=False)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        if os.path.exists(temp_path): os.remove(temp_path)

    # 5. Result Display Section
    if 'result' in st.session_state:
        st.divider()
        content = st.session_state['result']
        
        # Split the response into Notes and Quiz for better UI
        parts = content.split("### PRACTICE QUIZ")
        notes = parts[0]
        quiz = parts[1] if len(parts) > 1 else "No quiz generated."

        tab1, tab2 = st.tabs(["📚 Detailed Notes & Summary", "✍️ Interactive Quiz"])
        
        with tab1:
            st.markdown(notes)
            st.download_button("📥 Download Notes", notes, file_name="notes.txt")

        with tab2:
            st.markdown(quiz)

            st.info("Check the bottom of the quiz for the Answer Key!")

