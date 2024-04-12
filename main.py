import requests

api_key = "f64765660c394c1781fbcc5fafe717ad"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-03-12&sortBy=publishedAt&apiKey=" \
      "f64765660c394c1781fbcc5fafe717ad"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
      print(article["title"])
      print(article["description"])


