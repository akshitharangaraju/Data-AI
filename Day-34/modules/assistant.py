import os
import time
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from transformers import pipeline

@st.cache_resource
def load_bert():
    return pipeline("ner", model="dmis-lab/biobert-v1.1", aggregation_strategy="simple")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_specialist_analysis(vectorstore, query, image_file=None):
    medical_ner = load_bert()
    terms = ", ".join([e['word'] for e in medical_ner(query)]) if medical_ner else "None"

    context = ""
    if vectorstore:
        docs = vectorstore.similarity_search(query, k=3)
        context = "\n\n".join([d.page_content[:800] for d in docs])

    prompt = f"Role: Senior Cardiologist. Symptoms: {terms}. Context: {context}. Task: Clinical assessment."

    inputs = [prompt, f"Query: {query}"]
    if image_file: inputs.append(Image.open(image_file))

    # --- 2026 STABLE IDENTIFIERS ---
    models_to_try = ["gemini-3.1-flash-lite-preview", "gemini-3-flash-preview"]
    
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name, 
                contents=inputs,
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    # Enabling 'Thinking' for complex cardiology reasoning
                    thinking_config=types.ThinkingConfig(thinking_level="low") 
                )
            )
            return response.text
        except Exception as e:
            if "429" in str(e).lower():
                st.warning(f"⚠️ {model_name} quota hit. Cooling down...")
                time.sleep(15)
                continue
            if "404" in str(e).lower(): continue
            return f"❌ Error: {str(e)}"
    
    return "🚨 Clinical servers at capacity. Please refresh in 60s."