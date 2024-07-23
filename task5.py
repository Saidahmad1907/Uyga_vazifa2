import requests

class DummyJson:
    def __init__(self, url):
        self.url = url

    def request(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  
            data = response.json()
            print(data)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

dummy_json = DummyJson("https://dummyjson.com/users")
dummy_json.request()
