import requests

def fetch_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return data["content"]
    else:
        return "Failed to fetch quote"

if __name__ == "__main__":
    print("Random Quote Generator")
    print("----------------------")
    quote = fetch_quote()
    print("Random Quote:", quote)
