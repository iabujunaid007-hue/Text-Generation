This is a simple Python project that generates random text using a first-order Markov Chain algorithm. It analyzes an input .txt file and creates new text by predicting the next word based on the current word — mimicking the style and structure of the original content.

🚀 Features
Reads plain text from a file (input.txt)

Builds a word-to-word transition dictionary

Generates random, natural-looking sentences

Fully written in Python and easy to modify or extend

🧠 How It Works
Input: You provide a text file (input.txt) with any content — stories, articles, or poems.

Model Building: The code splits the text into words and creates a mapping of which words can follow each other.

Text Generation: It randomly selects a starting word and builds a new sentence by following word transitions.

