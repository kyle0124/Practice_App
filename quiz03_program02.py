# SoyNLP Library

# pip install soynlp

import urllib.request
import pickle
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor
from soynlp.tokenizer import LTokenizer


# Training Data
# urllib.request.urlretrieve('https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt', filename='data_train.txt')

train_data = DoublespaceLineCorpus('data_train.txt')
print(len(train_data))
print(type(train_data))

model = WordExtractor()
model.train(train_data)

# cohesion Tokenize

score_table = model.extract()
scores = {word:score.cohesion_forward for word, score in score_table.items()}
tokenizer = LTokenizer(scores=scores)

with open('./resources/tokenizer01.model', 'wb') as f :
    pickle.dump(tokenizer, f)

# branch entropy
scores = {word:score.right_branching_entropy for word, score in score_table.items()}
tokenizer = LTokenizer(scores=scores)

with open('./resources/tokenizer02.model', 'wb') as f :
    pickle.dump(tokenizer, f)

# multi
scores = {word:score.cohesion_forward * score.right_branching_entropy 
          for word, score in score_table.items()}
tokenizer = LTokenizer(scores=scores)

with open('./resources/tokenizer03.model', 'wb') as f :
    pickle.dump(tokenizer, f)












































