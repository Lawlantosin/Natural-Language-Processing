import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from bs4 import BeautifulSoup
import contractions
import string

text = """<p>Text preprocessing is the process of turning a document’s ﬂow of text into the quantiﬁable chunks needed for analysis. 
The initial step in text preprocessing is text indexing, which is the process of converting a text or texts into a list of words
. <br> Since a text or texts are given as unstructured forms by itself or themselves essentially, it's almost impossible to process 
its raw form directly by using a computer program. <br> In other words, text indexing means the process of segmenting a text which 
consists of sentences into individual words. <br> Note, this isn't exhaustive.</p>"""

# create an instance of beautiful soup
soup = BeautifulSoup(text, 'html.parser')

# get the text
cleaned_text = soup.get_text()

# fix the contractions
cleaned_text = contractions.fix(cleaned_text)

# convert the text to lower case
cleaned_text=cleaned_text.lower()

# tokenize into sentences
cleaned_tokens = sent_tokenize(cleaned_text)

clean_words= [word_tokenize(sent) for sent in cleaned_tokens]


# tokenize into individual words
cleaned_word_tokens = word_tokenize(cleaned_text)

# create an instance of english stopwords
stop_word=stopwords.words('english')

# remove the stopwords from the text
cleaned_text= [word for sent in clean_words for word in sent if word not in stop_word]

cleaned_text= [word for word in cleaned_text if word not in string.punctuation]

cleaned_text= [word for word in cleaned_text if word.isalpha()]

# create an instance of the stemmer
stem= PorterStemmer()
# Apply the stemmer on the text
clean_stem =[stem.stem(word) for word in cleaned_text]

# create an instance of the lemmatizer
wm=WordNetLemmatizer()

# Apply the lemmatizer on the text
cleaned_lema= [wm.lemmatize(word) for word in cleaned_text]
cleaned_lema