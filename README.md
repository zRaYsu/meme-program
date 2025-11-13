# meme-program 🎭

Es un programa que creé por aburrimiento, espero que os divirtáis leyendo chistes de Reddit o X :D.

## 📖 Descripción

Un generador de memes aleatorios que obtiene contenido de Reddit (tanto en español como en inglés), muestra el título traducido al español en la consola y guarda la imagen del meme localmente.

## ✨ Características

- 🎲 Obtiene memes aleatorios de múltiples subreddits
- 🌍 Soporta memes en español e inglés
- 🔄 Traduce automáticamente los títulos al español
- 💾 Guarda la imagen del meme como `meme.jpg`
- 🚀 Fácil de usar, solo ejecuta y disfruta

## 📋 Requisitos

- Python 3.6 o superior
- Conexión a Internet

## 🔧 Instalación

1. Clona o descarga este repositorio
2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

O en Windows:

```bash
py -m pip install -r requirements.txt
```

## 🚀 Uso

Simplemente ejecuta el programa:

```bash
python meme.py
```

O en Windows:

```bash
py meme.py
```

El programa:
1. Obtendrá un meme aleatorio de Reddit
2. Mostrará el título original y su traducción al español en la consola
3. Guardará la imagen como `meme.jpg` en el mismo directorio

## 📦 Subreddits incluidos

### En Español 🇪🇸
- SpanishMeme
- memexico
- Argentina
- chile
- Colombia
- espanol
- MemesEnEspanol
- dankgentina
- yo_elvr

### En Inglés 🇬🇧
- memes
- dankmemes
- wholesomememes
- PrequelMemes
- MemeEconomy
- funny
- AdviceAnimals
- me_irl

## 📝 Changelog

### Versión 1.2
- ✅ Añadidos memes en español de múltiples subreddits
- ✅ Soporte para memes en inglés con traducción automática
- ✅ Mejorado el manejo de errores
- ✅ Interfaz más clara y organizada
- ✅ Eliminado ASCII art (ahora solo muestra el título)

## 🛠️ Estructura del proyecto

```
memee2/
├── meme.py          # Programa principal
├── requirements.txt # Dependencias
├── README.md        # Este archivo
└── meme.jpg         # Imagen guardada (se genera al ejecutar)
```

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal. ¡Disfruta de los memes!

## 🤝 Contribuciones

Siéntete libre de mejorar este programa o añadir más subreddits. ¡Toda ayuda es bienvenida!

---

**Nota:** Este programa utiliza la API pública de [meme-api.com](https://meme-api.com) para obtener los memes de Reddit.

