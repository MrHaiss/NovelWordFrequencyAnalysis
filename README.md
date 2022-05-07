# NovelWordFrequencyAnalysis
 Simple project that analyses the word frequency of the text of Moby Dick. The text of the book is scraped from the website Project Gutenberg, which has a large store of publicly available books:
 
 https://www.gutenberg.org/
 
 Uses requests to fetch the text for the story and BeautifulSoup to parse the HTML. Some basic data cleansing is performed to remove non-story text and common English words such as "I" and "you". Finally, displays the top 10 most common words in a bar chart plotted using matplotlib.
