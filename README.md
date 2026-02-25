LEctureAI Pro: A Smart Study Assistant
LectureAI Pro is an intelligent study companion designed to transform classroom lectures—whether audio, video, or PDF—into structured, high-quality study kits. Built with Streamlit and powered by the Google Gemini 2.5 Flash model, it automates the tedious parts of learning so students can focus on mastery.

✨ Key Features
Multimodal Input: Supports MP3, WAV, MP4, and PDF file uploads or live microphone recording.

Intelligent Transcription: Converts speech to technical text with high accuracy.

MultiLanguage Support: Supports Multiple Indian languages like Hindi, English, Telugu etc. or mix of languages.

Visual Anchoring: (Unique Feature) Automatically identifies and describes critical visual moments in video lectures (e.g., diagrams, whiteboard notes).

Cognitive Summarization: Generates three-tier summaries: High-level overview, Detailed Technical Notes, and Practice Quizzes.

Instant Assessment: Creates interactive MCQs with an answer key to test knowledge retention immediately.

🛠️ Technical Stack
Frontend: Streamlit (Python-based web framework)

AI Engine: Google Generative AI (Gemini 2.5 Flash)

Backend: Python 3.10+

Media Handling: MoviePy / Pydub (via Gemini Cloud processing)

🚀 Getting Started
1. Prerequisites
Python 3.10 or higher

A Google Gemini API Key (Get it from Google AI Studio)

2. Installation
Clone the repository and install the dependencies:

Bash
git clone https://github.com/yourusername/lexis-study-assistant.git
cd lexis-study-assistant
pip install -r requirements.txt
3. Configuration
Create a .streamlit/secrets.toml file in the root directory and add your API key:

Ini, TOML
GOOGLE_API_KEY = "your_actual_api_key_here"
4. Running the App
Bash
streamlit run app.py
