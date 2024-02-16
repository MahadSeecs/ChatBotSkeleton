from nltk.tokenize import word_tokenize
import sys
sys.path.append('../engines')
from engines.calculus import differentiater,integrater


def definer(user):
    toks = word_tokenize(user)
    #lists to check keywords
    self = ['your','you']
    diff_words = ["diff", "differential", "derivative","differentiate"]
    intg_words = ["integral","integrate"]

    #differentiate
    if any(word in toks for word in diff_words):
        return differentiater(user)
    #integrate
    elif any(word in toks for word in intg_words):
        return integrater(user)
    
    #inform about itself
    elif any(word in toks for word in self):
        return user