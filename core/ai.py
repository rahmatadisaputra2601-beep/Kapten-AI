import ollama
from core.settings import MODEL, SYSTEM_PROMPT

history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

def ask(prompt):

    history.append({
        "role": "user",
        "content": prompt
    })

    response = ollama.chat(
        model=MODEL,
        messages=history
    )

    answer = response["message"]["content"]

    history.append({
        "role": "assistant",
        "content": answer
    })

    return answer