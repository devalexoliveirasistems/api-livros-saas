import os
import google.generativeai as genai
from prompt import build_prompt

# 🔑 COLOQUE SUA API KEY AQUI (Google AI Studio)
genai.configure(api_key="SUA_API_KEY_AQUI")

# 🧠 Modelo gratuito recomendado
model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_text(text: str):
    """
    Envia o texto para o Gemini e retorna a análise estruturada
    """
    prompt = build_prompt(text)
    
    response = model.generate_content(prompt)
    
    return response.text