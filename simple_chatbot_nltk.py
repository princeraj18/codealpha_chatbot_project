import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
# Defining the keywords
users_keyword = {
    ("hii", "hello", "hey"): "greeting",
    ("bye", "goodbye"): "goodbye",
    ("thank", "thanks"): "thanks",
    ("good","very good"):"news",
}
# Defining the responses
responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "news":"how are you today?",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
}

# Defining the Tokenization
def tokenize(text):
    return word_tokenize(text.lower())

# Removing the stopwords
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

# Lemmatization
def lemmatize(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in tokens]

# Get WordNet POS tag
def get_wordnet_pos(token):
    tag = nltk.pos_tag([token])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

# Match keywords and get response
def get_response(tokens):
    for keywords, response_key in users_keyword.items():
        for keyword in keywords:
            if keyword in tokens:
                return responses[response_key]
    return responses["default"]

# Main function
def chat():
    print("Chatbot: " + responses["greeting"])
    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == 'exit':
            print("Chatbot: " + responses["goodbye"])
            break
        tokens = tokenize(user_input)
        tokens = remove_stopwords(tokens)
        tokens = lemmatize(tokens)
        response = get_response(tokens)
        print("Chatbot: " + response)

# Run the chatbot
if __name__ == "__main__":
   chat()