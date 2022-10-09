from gnews import GNews

google_news = GNews()
google_news.period = '7d'  # News from last 7 days
#google_news.results = 300  # number of responses across a keyword
#google_news.country = 'US'  # News from a specific country 
#google_news.language = 'en'  # News in a specific language
#google_news.exclude_websites = ['yahoo.com', 'cnn.com']  # Exclude news from specific website i.e Yahoo.com and CNN.com
#google_news.start_date = (2022, 10, 1) # Search from 1st Jan 2020
#google_news.end_date = (2022, 10, 9) # Search until 1st March 2020

cat_news = google_news.get_news('Ukraine')
print(cat_news[0])