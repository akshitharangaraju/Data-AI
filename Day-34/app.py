import streamlit as st
from streamlit_lottie import st_lottie
import requests, os, time
from dotenv import load_dotenv

from ingestion import process_medical_library, get_gemini_embeddings
from modules.vector_db import initialize_vector_db
from modules.assistant import get_specialist_analysis
from modules.tools import generate_medical_document

load_dotenv()
st.set_page_config(page_title="Cardio-AI Elite", layout="wide")

# UI Polish
def load_lottie(url):
    try: return requests.get(url, timeout=3).json()
    except: return None

heart_anim = load_lottie("https://lottie.host/7db801b6-d5f4-4e20-9114-1e05a3962b92/3kXp6I0x0L.json")

with st.sidebar:
    if heart_anim: st_lottie(heart_anim, height=120)
    st.header("🫀 Clinical Portal")
    med_img = st.file_uploader("Upload ECG (Photo)", type=['png', 'jpg', 'jpeg'])
    st.info("Now using Dual-Model Fallback (1.5 + 2.0)")

st.title("Cardiology Specialist AI")

# Knowledge Sync
if "vectorstore" not in st.session_state:
    with st.status("🧠 Syncing Medical Knowledge...") as s:
        chunks = process_medical_library("data/")
        if chunks:
            st.session_state.vectorstore = initialize_vector_db(chunks, get_gemini_embeddings())
        else:
            st.session_state.vectorstore = None
        s.update(label="✅ Ready", state="complete")

if "messages" not in st.session_state: st.session_state.messages = []

# Display Chat
for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])

if prompt := st.chat_input("Ex: Explain the risks of Stage 2 Hypertension..."):
    # Anti-Spam Check
    if "lock" in st.session_state and st.session_state.lock:
        st.error("Please wait for the current analysis to finish.")
    else:
        st.session_state.lock = True
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("👨‍⚕️ Analyzing (this may take 20s if quota is resetting)..."):
                res = get_specialist_analysis(st.session_state.vectorstore, prompt, med_img)
                st.markdown(res)
                st.session_state.messages.append({"role": "assistant", "content": res})
        
        st.session_state.lock = False
        st.rerun() # Refresh to clear buttons/state