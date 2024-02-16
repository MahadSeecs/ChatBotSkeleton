import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer
# nltk.download("averaged_perceptron_tagger")
port = PorterStemmer()

user = 'What is your name'
toks = word_tokenize(user)
print(toks)

"""this function decides where to which module the user's input will go"""
def definer():
    #lists to check keywords
    self = ['your','you']
    diff_words = ["diff", "differential", "derivative","differentiate"]
    intg_words = ["integral","integrate"]

    if any(word in toks for word in diff_words):
        return [user,'d']
    
    elif any(word in toks for word in intg_words):
        return [user,'i']
    
    elif any(word in toks for word in self):
        return user





# lotr_quote = "It's a dangerous business, Frodo, going out your door."
# l = word_tokenize(lotr_quote)
# l = nltk.pos_tag(l)

# grammar = "NP: {<DT>?<JJ>*<NN>}"
# chunk_parser = nltk.RegexpParser(grammar)
# tree = chunk_parser.parse(l)
# tree.draw()