import time, hashlib, requests

apiKey = "9e7d8b5843787356fbd7cdebbf4b7abf"
secret = "0baa473b16"

ts = str(int(time.time()))
signature = hashlib.sha256((apiKey + secret + ts).encode()).hexdigest()

headers = {
    "Accept": "application/json",
    "Api-key": apiKey,
    "X-Signature": signature,
}

url = "https://api.test.hotelbeds.com/hotel-api/1.0/status"
r = requests.get(url, headers=headers)
print(r.status_code, r.json())


HOTELS = {
    "key": "9e7d8b5843787356fbd7cdebbf4b7abf",
    "secret": "0baa473b16",
    "base": "https://api.test.hotelbeds.com/hotel-api/1.0"
}
