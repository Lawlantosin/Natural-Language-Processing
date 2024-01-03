import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from bs4 import BeautifulSoup
import contractions

text = """<p>Text preprocessing is the process of turning a document’s ﬂow of text into the quantiﬁable chunks needed for analysis. 
The initial step in text preprocessing is text indexing, which is the process of converting a text or texts into a list of words
. <br> Since a text or texts are given as unstructured forms by itself or themselves essentially, it's almost impossible to process 
its raw form directly by using a computer program. <br> In other words, text indexing means the process of segmenting a text which 
consists of sentences into individual words. <br> Note, this isn't exhaustive.</p>"""


# create an instance of beautiful soup
soup = BeautifulSoup(text, 'html.parser')

# get the text
cleaned_text = soup.get_text()
cleaned_text