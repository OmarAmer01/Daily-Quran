import requests as rq

def getVerse(surah: int, aya: int, lang: str):
    # Gets a verse from the Quran
    url = f"https://api.mp3quran.net/api/aya?surah={surah}&language={lang}&aya={aya}"
    req = 
