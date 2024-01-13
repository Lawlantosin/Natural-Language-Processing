import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from bs4 import BeautifulSoup
import re
import contractions
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def load_data(file_path):
    # Load the data from the given file path
    df = pd.read_csv(file_path)  # Assuming the data is in CSV format
    return df

def print_process_start(process_name):
    print(f"Processing {process_name}...")

def print_process_done(process_name):
    print(f"{process_name} Done")
    
def remove_duplicates(df):
    print_process_start("Remove Duplicates")
    # Check for duplicated values
    if df.duplicated().sum() > 0:
        # Remove duplicated values
        df.drop_duplicates(keep='first', inplace=True)
        df.reset_index(drop=True, inplace=True)
        print_process_done("Remove Duplicates")
    else:
        print("No duplicated values.")
    return df

def fix_contractions(text):
    result = contractions.fix(text)
    return result

def remove_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    result = soup.get_text()
    return result

def remove_special_chars(text):
    result = re.sub('[^a-zA-Z]', ' ', text)
    return result

def text_preprocessing(df):
    print_process_start("Text Preprocessing")
    # Text preprocessing - Fix contractions
    df['text'] = df['text'].apply(lambda x: fix_contractions(x))

    
    print_process_start("Remove HTML")
    # Text preprocessing - Remove HTML
    df['text'] = df['text'].apply(lambda x: remove_html(x))
    print_process_done("Remove HTML")
    
    print_process_start("Remove special characters")
    # Text preprocessing - Remove special characters
    df['text'] = df['text'].apply(lambda x: remove_special_chars(x))
    print_process_done("Remove special characters")

    print_process_start("Convert to lowercase")
    # Text preprocessing - Convert to lowercase
    df['text'] = df['text'].apply(lambda x: x.lower())
    print_process_done("Convert to lowercase")
    
    print_process_start("Tokenize")
    # Text preprocessing - Tokenize
    df['text'] = df['text'].apply(lambda x: nltk.word_tokenize(x))
    print_process_done("Tokenize")
    
    print_process_start("Remove stopwords")
    # Text preprocessing - Remove stopwords
    df['text'] = df['text'].apply(lambda x: remove_stopwords(x))
    print_process_done("Remove stopwords")
    
    
    print_process_start("Lemmatize")
    # Text preprocessing - Lemmatize
    df['text'] = df['text'].apply(lambda x: lemmatize(x))
    print_process_done("Lemmatize")
    
    
    print_process_start("Join words")
    # Text preprocessing - Join words
    df['text'] = df['text'].apply(lambda x: join_word(x))
    print_process_done("Join words")
    
    print_process_done("Text Preprocessing")
    return df

def remove_stopwords(row):
    stop_words = stopwords.words('english')
    words = [word for word in row if word not in stop_words]
    return words

def lemmatize(row):
    wn = WordNetLemmatizer()
    words = [wn.lemmatize(word) for word in row]
    return words

def join_word(row):
    words = " ".join([word for word in row])
    return words

def create_wordcloud(data, sent_value):
    reviews = data[data['label'] == sent_value]
    words = ' '.join(reviews['text'])

    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='black',
                          width=3000,
                          height=2500
                          ).generate(words)

    plt.figure(figsize=(12, 12))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    print_process_done("Create Word Cloud")

def sentiment_preprocess(file_path):
    # Load data
    df = load_data(file_path)

    # Data processing - Remove duplicates
    df = remove_duplicates(df)

    # Text preprocessing
    df = text_preprocessing(df)

    # Plot value counts of the label
    label_counts = df['label'].value_counts()
    label_counts.plot(kind='bar')
    plt.title('Label Value Counts')
    plt.xlabel('Label')
    plt.ylabel('Count')
    plt.show()

    # Print label value counts
    print("Label value counts:")
    print(label_counts)

    # Create word clouds
    print('Negative Reviews')
    create_wordcloud(df, 0)
    
    print('Positive Reviews')
    create_wordcloud(df, 1)

    return df
