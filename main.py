import nltk
import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt

# Fetch and parse HTML
r = requests.get("https://www.gutenberg.org/files/2701/2701-h/2701-h.htm")
html_text = r.text
soup = BeautifulSoup(html_text, "html.parser")
raw_text = soup.get_text()

# Split off the unnecessary text
initial_split = raw_text.split("*** START OF THE PROJECT GUTENBERG EBOOK MOBY-DICK; OR THE WHALE ***")
second_split = initial_split[1].split("*** END OF THE PROJECT GUTENBERG EBOOK MOBY-DICK; OR THE WHALE ***")
story_text = second_split[0]

# Prepare the data
word_tokenizer = nltk.RegexpTokenizer("\w+")
words = word_tokenizer.tokenize(story_text)
words_list = [word.lower() for word in words]

# Cleanup stop words (commonly used words)
stopwords = nltk.corpus.stopwords.words('english')
words_list_nostop = [word for word in words_list if word not in stopwords]

# Count word frequency
word_freq_all = Counter(words_list_nostop)
word_freq_top10 = word_freq_all.most_common(20)

# Plot the top words
plt.bar(*zip(*word_freq_top10))
plt.title("Top 10 Words by Occurrence")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
