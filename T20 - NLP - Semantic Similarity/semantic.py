import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Practical task 1: Write a note on what you noticed about the similarities between cat, monkey and banana and think of an example of your own.
# Answer: The two words which are most similar of the three are cat and monkey, for they are both animals. The similarity score is ~0.593, the
# highest of the three values returned. The similarity of banana and monkey is ~0.404 and the similarity of banana and cat is ~0.224. This 
# is most likely because monkeys are known to eat bananas so there is more of an association between the words than with cat and banana.

# Here is an example of my own, using the words "mirror", "glass" and "identity". It is clear that mirror and glass are the most similar words,
# scoring ~0.56. Mirror and identity are somewhat similar conceptually, for obvious reasons, and scores ~0.25. Glass and identity score 0.06, since 
# there is very little similarity there. 

word4 = nlp("mirror")
word5 = nlp("glass")
word6 = nlp("identity")

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

# What is unclear to me, looking back, is why cat and banana scores ~0.22. This seems rather high, bearing in mind the results for words 4, 5 and 6.

# Let's consider another example. Words: 

word7 = nlp("book")
word8 = nlp("knowledge")
word9 = nlp("tree")

print(word7.similarity(word8))
print(word9.similarity(word8))
print(word9.similarity(word7))

# The similarity of book and knowledge is 0.34. This makes sense. The similarity of knowledge and tree is only 0.15 and the similarity of
# book and tree is 0.063. This is perhaps unusual: I would say that the words book and tree are more similar because books are made of paper
# and paper comes from wood which comes from trees, whereas I fail to see much connection between the words knowledge and tree. I would
# say book and tree are more similar.

# If I use the model en_core_web_sm, I get the following error:
#       UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
# It is evident indeed from the output that the results are not useful: cat and apple are more similar than apple and banana. This is absurd.

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity))