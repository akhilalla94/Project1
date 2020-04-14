import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "aKdKSlQdkdzE8rvJ9XvRw", "isbns": "9781632168146"})
print(res.json())