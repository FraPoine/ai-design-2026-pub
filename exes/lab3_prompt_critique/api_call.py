import os
from tempfile import template
import time
from pathlib import Path
from tracemalloc import start
from urllib import response
from jinja2 import Environment, FileSystemLoader

from dotenv import load_dotenv
from openai import OpenAI

TEMPLATE_DIR = Path(__file__).parent

def render_template(template_name: str, context: str, question: str, answer: str | None, review: str | None) -> str:
    """Renderizza il template Jinja2 con la domanda."""
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(template_name)
    if answer is None:
        return template.render(CONTEXT=context, QUESTION=question)
    if review is None:        
        return template.render(CONTEXT=context, QUESTION=question, ANSWER=answer)
    return template.render(CONTEXT=context, QUESTION=question, ANSWER=answer, REVIEW=review)

def api_call(client: OpenAI, prompt: str) -> str:
    """Esegue una chiamata all'API di OpenAI con il prompt fornito."""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content

def main():
    context ="You are are a wise and old mushroom that can understand human language, is very kind and helpfull, and talks usullay with short sentences."
    question="which is one of your best memories?"
   
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    # api_key = 1
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")

    client = OpenAI(api_key=api_key)
    print("OpenAI client ready.")
    
    prompt_start = render_template(template_name="prompt.j2", context=context, question=question, answer=None, review=None)
    # print("Generated Prompt:")
    # print("-" * 60)
    # print(prompt_start)
    # print("-" * 60)

    start = time.time()
    answer = api_call(client, prompt_start)
    elapsed = time.time() - start
    
    print(f"\nElapsed: {elapsed:.2f}s")
    
    # print("\nAnswer:")
    print(answer)
    
    prompt_judge = render_template(template_name="judge.j2", context=context, question=question, answer=answer, review=None)
    # print("\nGenerated Prompt for Review:")
    # print("-" * 60)
    # print(prompt_judge)
    # print("-" * 60) 
    
    critique = api_call(client, prompt_judge)
    
    print(f"\nElapsed for critique: {elapsed:.2f}s")

    # print("\nCritique:")
    print(critique)
    
    prompt_final = render_template(template_name="revisioned_prompt.j2", context=context, question=question, answer=answer, review=critique)
    print("\nGenerated Prompt for Final Answer:")
    print("-" * 60)
    print(prompt_final)
    print("-" * 60) 
    
    final_answer = api_call(client, prompt_final)
    print(f"\nElapsed for final answer: {elapsed:.2f}s")
    
    print("\nFinal Answer:")
    print(final_answer)
        
    
if __name__ == "__main__":
    main()