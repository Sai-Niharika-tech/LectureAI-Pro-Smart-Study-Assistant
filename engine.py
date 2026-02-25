import google.generativeai as genai
import streamlit as st
import time

# Use the secure key from secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def process_any_file(file_path, file_type):
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    # Upload to Gemini Cloud
    uploaded_file = genai.upload_file(path=file_path)
    
    # Monitor processing
    while uploaded_file.state.name == "PROCESSING":
        time.sleep(2)
        uploaded_file = genai.get_file(uploaded_file.name)

    # UNIQUE FEATURE PROMPT: Visual Anchoring
    prompt = f"""
    You are an academic mentor. Analyze this {file_type}.
    SPECIAL FEATURE: 
    If this is a Video, identify the 3-4 most critical visual moments (like a diagram on a whiteboard or a main slide). 
    Describe these visual moments in detail within the notes using the header '### VISUAL ANCHORS'.
    
    STEP 1: Check if there is any specific educational topic or academic content discussed.
    
    STEP 2: 
    - IF NO ACADEMIC TOPIC IS FOUND (e.g., just background noise, silence, or casual greeting):
      Return ONLY a section titled '### SUMMARY' explaining that no educational content was detected. 
      DO NOT generate Notes or a Quiz.
      
    - IF ACADEMIC TOPIC IS FOUND:
      1. ### SUMMARY: 3 bullet points.
      2. ### DETAILED NOTES: Technical headings and details.
      3. ### VISUAL ANCHORS: Describe key visual moments if it's a video.
      4. ### PRACTICE QUIZ: 3 MCQs with options.
      5. ### ANSWERS: At the bottom.
    
    Always respond in English.
    """
    
    response = model.generate_content([prompt, uploaded_file])
    genai.delete_file(uploaded_file.name)
    return response.text