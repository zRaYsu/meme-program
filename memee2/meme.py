import requests
from io import BytesIO
import random

SUBREDDITS_ES = [
    "SpanishMeme",
    "memexico",
    "Argentina",
    "chile",
    "Colombia",
    "espanol",
    "MemesEnEspanol",
    "dankgentina",
    "yo_elvr"
]

SUBREDDITS_EN = [
    "memes",
    "dankmemes",
    "wholesomememes",
    "PrequelMemes",
    "MemeEconomy",
    "funny",
    "AdviceAnimals",
    "me_irl"
]

ALL_SUBREDDITS = SUBREDDITS_ES + SUBREDDITS_EN

def get_meme_data():
    subreddits = ALL_SUBREDDITS.copy()
    random.shuffle(subreddits)
    
    for subreddit in subreddits:
        url = f"https://meme-api.com/gimme/{subreddit}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('url') and data.get('code') != 404:
                    title = data.get('title', 'Sin título')
                    title = title.strip()
                    if title and title != 'title.':
                        return data.get('url', ''), title, subreddit
        except Exception:
            continue
    
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        title = data.get('title', 'Sin título').strip()
        if title == 'title.':
            title = 'Sin título'
        return data.get('url', ''), title, 'random'
    except Exception:
        return '', 'Sin título', ''

def download_meme_image(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return BytesIO(response.content)
    except Exception as e:
        print(f"Error al descargar imagen: {e}")
        return None

def translate_text(text, target_lang='es'):
    if not text or text == 'Sin título':
        return text
    
    translate_url = "https://translate.googleapis.com/translate_a/single"
    params = {
        'client': 'gtx',
        'sl': 'auto',
        'tl': target_lang,
        'dt': 't',
        'q': text
    }
    
    try:
        response = requests.get(translate_url, params=params, timeout=5)
        translated = response.json()[0][0][0]
        return translated
    except Exception:
        return text

def main():
    print("=" * 60)
    print("🎭 OBTENIENDO MEME...")
    print("=" * 60)
    
    meme_url, meme_title, subreddit = get_meme_data()
    
    if not meme_url:
        print("❌ No se pudo obtener el meme")
        return
    
    if subreddit and subreddit != 'random':
        print(f"✅ Meme obtenido de r/{subreddit}")
    else:
        print("✅ Meme obtenido (fuente aleatoria)")
    
    print(f"\n📥 Descargando meme...")
    image_bytes = download_meme_image(meme_url)
    
    if not image_bytes:
        print("❌ No se pudo descargar la imagen")
        return
    
    meme_title_es = translate_text(meme_title)
    
    print("\n" + "=" * 60)
    print("📝 TÍTULO DEL MEME:")
    print("=" * 60)
    if meme_title and meme_title != 'Sin título':
        print(f"Original: {meme_title}")
        if meme_title_es != meme_title:
            print(f"Español:  {meme_title_es}")
        else:
            print(f"Español:  {meme_title_es} (ya en español)")
    else:
        print("Sin título disponible")
    print("=" * 60)
    
    try:
        image_bytes.seek(0)
        with open("meme.jpg", "wb") as f:
            f.write(image_bytes.read())
        print("\n💾 Imagen guardada como 'meme.jpg'")
    except Exception as e:
        print(f"\n⚠️  No se pudo guardar la imagen: {e}")

if __name__ == "__main__":
    main()
