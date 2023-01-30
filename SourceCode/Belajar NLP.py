import nltk
import spacy as sp
nltk.download('punkt')

from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize

my_string = "hello every one. i have brother, then name is farhan"
print(sp.__version__)


print(word_tokenize(my_string))
print(sent_tokenize(my_string))