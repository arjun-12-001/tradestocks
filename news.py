from GoogleNews import GoogleNews
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

gn = GoogleNews(lang='en',region='India',period='7d')

analyzer = SentimentIntensityAnalyzer()
gn.search('wipro company india')

for i in gn.result():
  print(i['date'])
  print(i['title'])
  print(i['desc'])

  text = i['desc']
  # Create an instance of SentimentIntensityAnalyzer

  # Analyze the sentiment of a text
  scores = analyzer.polarity_scores(text)

  # Extract sentiment scores
  compound_score = scores['compound']
  positive_score = scores['pos']
  negative_score = scores['neg']
  neutral_score = scores['neu']

  # Print the sentiment scores
  print('--------------------------------------------------------------------')
  print('Compound Score:', compound_score)
  print('Positive Score:', positive_score)
  print('Negative Score:', negative_score)
  print('Neutral Score:', neutral_score)