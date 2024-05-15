from translation import translate_text
import streamlit as st
from extract import extract_text_from_pdf
from summarise import summarize_text
from save_to_pdf import save_text_to_pdf
import tempfile

def main():
    st.title("Legal Document Translator and Summarizer")
    
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf"])
    target_language = st.text_input("Enter the target language for translation (e.g., 'es' for Spanish)", value="es")

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "text/plain":
            text = str(uploaded_file.read(), "utf-8")
        else:
            st.error("Unsupported file type")
            return

        st.text_area("Extracted Text", text, height=300)
        
        if st.button("Translate and Summarize"):
            # Perform translation
            translation = translate_text(text, 'en')
            st.text_area("Translated Text", translation, height=300)

            # Perform summarization
            summary = summarize_text(text, language='en')  # Assuming input language is English
            st.text_area("Summary in Input Language", summary, height=150)

            # Save translation as PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                save_text_to_pdf(translation, tmp_file.name)
                tmp_file.seek(0)
                st.download_button(
                    label="Download Translation as PDF",
                    data=tmp_file.read(),
                    file_name="translated_text.pdf",
                    mime="application/pdf"
                )

if __name__ == "__main__":
    main()
