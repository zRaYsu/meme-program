import requests
import json

def get_meme_images():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['url']

def download_meme_image(url):
    response = requests.get(url)
    with open("meme.jpg", "wb") as f:
        f.write(response.content)
    print(f"Downloaded meme image from {url}")

def main():
    url = get_meme_images()
    download_meme_image(url)

if __name__ == "__main__":
    main()