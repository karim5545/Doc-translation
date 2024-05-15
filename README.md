# Doc-translation

# HOW TO USE
install vscode. Copy the github link into vscode. Type 'pip install -r requirements.txt' into the terminal
Go into translation.py and remove -ELIEKHOURY-. It appears 3 times. Open a terminal and type: streamlit run main.py


Current language translation is initialised as french to english. To change the target language you can edit it directly in the webapp, and change the last two letters from en to whatever you want(fr for french, en for english, fr for french...). The model is supposed to detect the current language. There is a limit to the amount of words in the file, if it is too long you can cut it up. Either upload a pdf or simply copy paste the text into the webapp
