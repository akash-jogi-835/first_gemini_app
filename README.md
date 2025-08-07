# Gemini Chatbot

A modern Streamlit chatbot interface powered by Google Gemini (Generative AI) API.

# To Access 
Link : https://firstgeminiapp-3gwjuhxefehjpjw5krvakk.streamlit.app/

# Features
- Chat with Gemini using Google's official Python client
- Multi-session chat history
- Stylish, clean UI with custom CSS
- Easy setup and configuration

# Requirements
- Python 3.8+
- Streamlit
- google-generativeai

# Installation

1. Clone this repository or copy the files to your project folder.
2. Install dependencies:
   ```bash
   pip install streamlit google-generativeai
   ```
3. (Optional) Create a virtual environment for isolation:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

# Usage

1. Get your Gemini API key from [Google MakerSuite](https://makersuite.google.com/app/apikey).
2. Add your API key to the code (default is set in `streamlit_app.py`).
3. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```
4. Open the provided local URL in your browser.

# Customization
- Change the model name in `streamlit_app.py` for different Gemini models (e.g., `gemini-1.5-flash`, `gemini-1.5-pro`).
- Edit the CSS in `streamlit_app.py` for your own look and feel.

# Screenshots
![Gemini Chatbot UI](screenshot.png)

# License
MIT

# Credits
- [Streamlit](https://streamlit.io/)
- [Google Generative AI Python Client](https://github.com/google/generative-ai-python)

