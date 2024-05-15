import openai
def summarize_text(text, language='en'):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text in {language}:\n{text}"}
        ]
    )
    summary = response.choices[0].message['content'].strip()
    return summary