import streamlit as st

import google.generativeai as genai  # Importing GenerativeAI library for Gemini model

# Configure the library with your API key
myapikey = st.secrets["multimodel_api_key"]
genai.configure(api_key=myapikey)


model = genai.GenerativeModel('gemini-1.0-pro-latest')

def text_spellcheck(user_input: str) -> tuple:
    prompt_template = f'''Given the input text:
    user input: {user_input}
    output must be in this format:
    misspelled_word:corrected_word
    ...
    output must not contain any other information than the format
    '''

    # check if parameters are of correct type
    if not isinstance(user_input, str):
        raise TypeError("user_input must be of type str")

    try:
        # Generate response using the provided model (assuming it's defined elsewhere)
        response = model.generate_content(prompt_template)
        response1 = response.text

        response1 = response1.split("\n")
        result = [(line.split(":")[0], line.split(":")[1]) for line in response1 if line.strip()]

        # replace the misspelled words with the corrected words
        for word, corrected_word in result:
            user_input = user_input.replace(word, corrected_word)

        return user_input, result
    except Exception as e:
        raise ValueError("Please provide a correct API key or try again.")

# Function to highlight wrong words in red
def highlight_wrong_words(text, wrong_words):
    for word, _ in wrong_words:
        text = text.replace(word, f'<span style="background-color:red">{word}</span>')
    return text

# Function to replace corrected words in green
def highlight_corrected_words(text, result):
    for _, corrected_word in result:
        text = text.replace(corrected_word, f'<span style="background-color:green">{corrected_word}</span>')
    return text

# Streamlit app
def main():
    st.set_page_config(page_title="AI Spell Correction", page_icon="✨", layout="wide")

    st.title("AI Spell Correction App")

    st.markdown("This app uses the GenerativeAI library to correct spelling mistakes in the input text. Created by [Fareed Khan](https://github.com/FareedKhan-dev)")
    

    # Input text area
    user_input = st.text_area("Enter your text here:", value="As the sun beganned to set on the horizen, casting a warm gloy across the skye, Sara laid on the gras in her backyerd, savoring the tranquil moment. She could here the chirpping of the birds and the gentle rustle of the leves in the breeze. Suddenly, she remembred she had forgoten to turn off the stove after cooking diner, causing her hart to race with panick. With hast, she jumped up and ruched into the house, hopeing that no damage had been done by her absent-minded mistake.")

    if st.button("Check Spelling"):
        if user_input:
            # Call the spellcheck function
            corrected_text, result = text_spellcheck(user_input)

            # Create two columns
            col1, col2 = st.columns(2)

            # Highlight wrong words in red
            wrong_words_highlighted = highlight_wrong_words(user_input, result)
            col1.markdown(f"**Original Text with Wrong Words Highlighted in Red:**")
            col1.markdown(f'<div class="full-width" style="background-color:#f9f9f9;padding-left:10px;border-radius:10px">{wrong_words_highlighted}</div>', unsafe_allow_html=True)

            # Highlight corrected words in green
            corrected_text_highlighted = highlight_corrected_words(corrected_text, result)
            col2.markdown(f"**Corrected Text with Corrected Words Highlighted in Green:**")
            col2.markdown(f'<div class="full-width" style="background-color:#f9f9f9;padding:10px;border-radius:5px">{corrected_text_highlighted}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
