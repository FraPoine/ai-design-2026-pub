#!/usr/bin/env python3
"""
Script per fare una chiamata API usando il template Jinja2
"""

import json
import os
from pathlib import Path
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import requests
from datasets import load_dataset

# Carica le variabili d'ambiente dal .env
load_dotenv()

ds = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset", split="train")

# Configurazione
TEMPLATE_DIR = Path(__file__).parent
TEMPLATE_NAME = "strange_prompt.j2"

# API Configuration (modifica con le tue credenziali)
API_KEY = os.getenv("OPENAI_API_KEY")  # Oppure metti la tua chiave qui
API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4"


def render_template(question: str) -> str:
    """Renderizza il template Jinja2 con la domanda."""
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_NAME)
    return template.render(QUESTION=question)


def call_api(prompt: str) -> dict:
    """Fa una chiamata all'API OpenAI."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
    }
    
    response = requests.post(API_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def main():
    # Esempio di utilizzo
    question = "which is one of your best memories?"
    
    print("=" * 60)
    print("RENDERING TEMPLATE...")
    print("=" * 60)
    
    # Renderizza il template
    rendered_prompt = render_template(question)
    print(rendered_prompt)
    
    print("\n" + "=" * 60)
    print("CALLING API...")
    print("=" * 60)
    
    # Chiama l'API
    if not API_KEY:
        print("⚠️ Manca OPENAI_API_KEY. Esporta la variabile d'ambiente:")
        print("export OPENAI_API_KEY='your-key-here'")
        return
    
    try:
        response = call_api(rendered_prompt)
        
        # Estrai la risposta
        answer = response["choices"][0]["message"]["content"]
        print(f"\nAPI Response:\n{answer}")
        
        # Prova a parsare il JSON dalla risposta
        try:
            result = json.loads(answer)
            print("\n" + "=" * 60)
            print("PARSED RESULT:")
            print("=" * 60)
            print(json.dumps(result, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print("(La risposta non è un JSON valido)")
            
    except Exception as e:
        print(f"❌ Errore nella chiamata API: {e}")


if __name__ == "__main__":
    main()
