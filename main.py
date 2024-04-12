import requests
from send_email import send_email

topic = "tesla"

api_key = "f64765660c394c1781fbcc5fafe717ad"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2024-03-12&sortBy=publishedAt&apiKey=" \
      "f64765660c394c1781fbcc5fafe717ad&language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = "Subject: Todays's news" + "\n"

# Access the article titles and description
for article in content["articles"][:5]:
      body = body + article["title"] \
             + "\n" + article["description"] \
             + "\n" + article["url"] + "\n\n"
      

text = body.encode("utf-8")
send_email(text)


