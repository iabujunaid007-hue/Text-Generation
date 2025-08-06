import random

# Step 1: Read the input text file
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Step 2: Build the Markov Chain model
def build_chain(text):
    words = text.split()
    chain = {}
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        if word not in chain:
            chain[word] = []
        chain[word].append(next_word)
    return chain

# Step 3: Generate random text
def generate_text(chain, start_word, length=20):
    word = start_word
    result = [word]
    for _ in range(length - 1):
        next_words = chain.get(word)
        if not next_words:
            break
        word = random.choice(next_words)
        result.append(word)
    return ' '.join(result)

# Main program
if __name__ == "__main__":
    file_path = r"C:\Users\delll\first.js\develop\input.txt"  # Use raw string for Windows path
    text = read_file(file_path)
    chain = build_chain(text)
    
    start_word = random.choice(list(chain.keys()))
    generated_text = generate_text(chain, start_word, length=20)
    
    print("\n🌟 Generated Text:\n")
    print(generated_text)
