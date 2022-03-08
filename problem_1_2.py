#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import required libraries

import pandas as pd
import streamlit as st

import re
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob


# In[ ]:


#defining functions

def review_cleaning(text):
    '''
    Input: Text that needs to be cleaned
    
    This function Make text lowercase, remove text in square brackets,remove punctuation
    and remove words containing numbers.
    
    Output: Cleaned text
    '''
    
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
#dealing with emojis by removing them
def remove_emoji(string):
    """
    Input: Text that need emojis to be removed
    
    this function removes emoticons,symbols,pictograms,map symbols
    flags
    
    output: cleaned text
    
    """
    
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F" # emoticons
                           u"\U0001F300-\U0001F5FF" # symbols & pictographs
                           u"\U0001F680-\U0001F6FF" # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF" # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def getPolarity(text):
    """
    Input: text
    
    using Textblob, finding out polarity of the text which ranges from (-1,1)
    
    Output: sentiment polarity of a sentence   
       
    """ 
    return TextBlob(text).sentiment.polarity

def getAnalysis(score):
    """
    Input: Sentiment polarity Score    
    This function returns sentiment for given text review based on polarity value 
    output: return sentiment based on polarity score
    """

    
    if score >= 0.35:
        return "Positive"
    elif -0.25< score <0.35:
        return "Neutral"
    else:
        return "Negative"
def star_senti(inp_val): 
    '''
    Input: Integer from column star
    This function returns sentiment value based on the overall ratings from the user
    output: sentiment based on star value
    '''

    
    if inp_val == 3.0:
        val = 'Neutral'
    elif inp_val == 1.0 or inp_val == 2.0:
        val = 'Negative'
    elif inp_val == 4.0 or inp_val == 5.0:
        val = 'Positive'
    
    return val


# In[ ]:


#url = "C:\\Users\\Anvesh\\Documents\\MLDL_class_notebooks\\interview preps\\next_labs_assignment\\data\\chrome_reviews.csv"
#chrome_data = pd.read_csv(file)


# In[ ]:


def process_df(chrome_data):
    """
    Input: Dataframe that needs to be processed
    
    This function applies "Review Cleaning", "Remove Emoji", "Getpolarity"
    "getAnalysis", "Star_senti" to the required columns
    
    Output: Provides output 'Text','Star', 'User Name', 'Text_sentiment','star_sentiment'
    for the user on web page
    
    """
    
    
    chrome_data['Text'] = chrome_data['Text'].apply(lambda x:review_cleaning(x))
    chrome_data['Text'] = chrome_data['Text'].apply(lambda x:remove_emoji(x))
    chrome_data['Text_polarity'] = chrome_data['Text'].apply(getPolarity)
    chrome_data['Text_sentiment'] = chrome_data['Text_polarity'].apply(getAnalysis)
    chrome_data['star_sentiment'] = chrome_data['Star'].apply(star_senti)
    unmatched_reviews = chrome_data.loc[(chrome_data['Text_sentiment'] == 'Positive') & (chrome_data['star_sentiment'] == 'Negative')]
    outputdf = unmatched_reviews[['Text','Star', 'User Name', 'Text_sentiment','star_sentiment']]
    st.write('unmatched text review and ratings:')
    st.write(outputdf)


# In[ ]:





# In[ ]:


def main():
    st.title('sentiment analysis of user review dataset')
    file = st.file_uploader("Upload file", type='csv')
    if not file:
        st.write("Upload a .csv to get started")
    return
    chrome_data = pd.read_csv(file)
    process_df(chrome_data)
main()

