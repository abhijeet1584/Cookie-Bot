# This is a random joke generator
# Powered by https://icanhazdadjoke.com/

import requests

url = "https://icanhazdadjoke.com/"
def getJoke ():
    # Requesting json from https://icanhazdadjoke.com/
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    return (data["joke"])