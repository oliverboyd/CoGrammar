import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "The dog that I had really loved bones.",
    "The man who whistles tunes pianos.",
    "Mary gave the child a Band-Aid",
    "That Jill is never here hurts",
    "The cotton clothing is made of grows in Mississippi"]

for sentence in gardenpathSentences:
    print('Sentence ' + str(gardenpathSentences.index(sentence) + 1) + ': ')
    print('Tokens: ' + str([token.orth_ for token in nlp(sentence)])) # Tokenisation
    print('Entities: ' + str([(i, i.label_, i.label) for i in nlp(sentence).ents])) # Entity Recognition
    for i in nlp(sentence).ents:
        print('Meaning of ' + str(i.label_) + ': ' + str(spacy.explain(i.label_))) # meaning of entities
    print() # new line

# Let's consider two of the entities which we looked up: 'PERSON' is self-explanatory. 
# It refers to people, including fictional characters. Mary and Jill are names of people, so this is correct.
# 'GPE' referes to countries, cities and states. GPE is presumably short for geo-political entity. 
# Mississippi, being a state of the US, clearly belongs to the GPE type.