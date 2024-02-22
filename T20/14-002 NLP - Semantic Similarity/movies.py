import spacy
nlp = spacy.load('en_core_web_md')
file = open('movies.txt','r') # opening the txt file
movies = file.readlines() # parsing the file line by line
movie_descs = {}
for line in movies:
    movie_descs[line[0:7]] = line[9:].strip() # we have created (and are appending) a dictionary, the keys of which are Movie A, Movie B etc. and the values are the descriptors extracted from the txt file

planet_hulk_desc = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

def similar_movie(desc):
    similarity_array = []
    for movie in movie_descs:
        desc = nlp(desc) 
        movie_desc = nlp(movie_descs[movie])
        similarity_array.append((movie,desc.similarity(movie_desc))) # building an array with the similarity values
    most_similar = max(similarity_array, key=lambda x:x[1])[0] # taking the maximum value and returning the corresponding movie letter 
    return most_similar

print(similar_movie(planet_hulk_desc))
