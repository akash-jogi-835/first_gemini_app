import streamlit as st
import google.generativeai as genai
from datetime import datetime

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="wide")

# Custom CSS for modern chat UI (white background)
st.markdown("""
<style>
    body, .stApp { background: #fff !important; }
    .main { font-family: 'Poppins', sans-serif !important; }
    .stChatMessage[data-testid="user-message"] {
        background: #f5f5f5;
        color: #222;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .stChatMessage[data-testid="assistant-message"] {
        background: #e9e9e9;
        color: #222;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .stTextInput > div > div > input {
        background: #fff;
        border-radius: 15px;
        padding: 1rem;
        font-size: 1rem;
        border: 2px solid #e9e9e9;
        color: #222;
    }
    .stTextInput > div > div > input:focus {
        border-color: #aaa;
        box-shadow: 0 0 10px #aaa3;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Session management for multiple chats
if 'chat_sessions' not in st.session_state:
    st.session_state.chat_sessions = {}
if 'current_session_id' not in st.session_state:
    st.session_state.current_session_id = None
if 'gemini_api_key' not in st.session_state:
    st.session_state.gemini_api_key = "AIzaSyCzXXpTfz894Z9M5hgvlegtvaDp9F2RGDs"

def create_new_session():
    session_id = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    st.session_state.chat_sessions[session_id] = {
        'messages': [],
        'title': f"Chat {len(st.session_state.chat_sessions) + 1}",
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    st.session_state.current_session_id = session_id
    return session_id

def configure_gemini(api_key):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        return model
    except Exception as e:
        st.error(f"Error configuring Gemini: {str(e)}")
        return None

# Configure Gemini model
model = configure_gemini(st.session_state.gemini_api_key)
if not model:
    st.stop()

# Create first session if none exists
if not st.session_state.chat_sessions:
    create_new_session()

# Get current session
current_session = st.session_state.chat_sessions.get(st.session_state.current_session_id)
if not current_session:
    create_new_session()
    current_session = st.session_state.chat_sessions[st.session_state.current_session_id]

# Display chat messages
st.title("Gemini Chatbot 🤖")
if current_session['messages']:
    for message in current_session['messages']:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
else:
    st.markdown("Welcome! Start chatting below.")

# Chat input
if prompt := st.chat_input("Type your message here..."):
    current_session['messages'].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Gemini is thinking..."):
            try:
                chat_history = []
                for msg in current_session['messages'][:-1]:
                    chat_history.append({
                        'role': 'user' if msg['role'] == 'user' else 'model',
                        'parts': [msg['content']]
                    })
                chat = model.start_chat(history=chat_history)
                response = chat.send_message(prompt)
                response_text = response.text
                st.markdown(response_text)
                current_session['messages'].append({"role": "assistant", "content": response_text})
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                current_session['messages'].append({"role": "assistant", "content": error_msg})

