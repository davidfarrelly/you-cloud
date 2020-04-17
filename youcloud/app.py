import sys
import requests
from wordcloud import WordCloud

import matplotlib.pyplot as plt

def getComments(apiKey, videoId):
    url = "https://www.googleapis.com/youtube/v3/commentThreads?key=" + apiKey + "&videoId=" + videoId + "&part=snippet&maxResults=100";
    response = requests.get(url)
    text = ''

    data = response.json()
    items = data['items']

    for item in items:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        text += comment

    return text

def createWordcloud(text):
    stop_words = getStopwords()
    wordcloud = WordCloud(stopwords=stop_words, background_color="white", min_word_length=4).generate(text)

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    wordcloud.to_file("img/first_review.png")

def getStopwords():
    with open('stopwords.txt') as f:
        stop_words = f.read().splitlines()

    return stop_words

if __name__ == '__main__':
    apiKey = 'AIzaSyBgLguJzHT-DgcabnPwARwaoke5SnFvShU'
    videoId = sys.argv[1]

    comments = getComments(apiKey, videoId)
    createWordcloud(comments)