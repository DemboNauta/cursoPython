import requests


dominio = "https://devthreads.es/backend/tweets-api.php"
r=requests.get(f"{dominio}")

for cliente in r.json():
    print(cliente['tweet_text'])