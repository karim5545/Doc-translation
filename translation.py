import openai
openai.api_key = 'sk-proj-ELIEKOURY--psYgAG0WCYoA-ELIEKHOURY-V1BpRGxUT3BlbkFJ7-ELIEKHOURY-dPOC3wvamMAVBXpUUmj'

def translate_text(text, target_language):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You need to make a word for word translation of the input text"},
            {"role": "user", "content": f"Translate the following text to {target_language} in a word-for-word manner without summarization:\n{text}"}
        ]
    )
    translation = response.choices[0].message['content'].strip()
    return translation