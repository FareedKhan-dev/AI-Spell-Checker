## AI Spell Correction App
<img src="https://i.ibb.co/QNNTvb5/screely-1710759136187.png">

This Streamlit app utilizes the GenerativeAI library and the Gemini model to identify and correct spelling errors within your text.
Features
1. Identifies misspelled words and suggests corrections.
2. Highlights misspelled words in red within the original text.
3. Displays the corrected text with the replaced words highlighted in green.
4. Provides a user-friendly interface for easy interaction.

## Technologies Used
1. Streamlit: For building the interactive web application.
2. GenerativeAI: For accessing and utilizing the Gemini language model.
3. Google Generative AI: Provides access to the Gemini model via API.

## Installation and Usage
Clone or download this repository.
1. Install the required libraries using requirements.txt `streamlit` and `google-generativeai`.
2. Obtain a Google Generative AI API key and replace `YOUR_API_KEY` in the code with your key.
3. Run the app using `streamlit run streamlit_app.py`.
4. Enter your text in the text area and click "Check Spelling".

## Disclaimer
This app is for demonstration purposes only. The accuracy of the spell correction depends on the GenerativeAI model and may not always be perfect.
