import gensim, logging
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
input_file_path = 'Data/content'

# Build Sentences from Corpus
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

				
sentences = MySentences(input_file_path) # a memory-friendly iterator

# Use word2Vec model
model = gensim.models.Word2Vec(sentences)

model.save('all_word2vec.model')

word_vectors = model.wv
word_vectors.save('word2vec.txt')
