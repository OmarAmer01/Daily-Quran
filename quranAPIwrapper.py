import requests as r
import ast

def getVerseARen(surah: int, aya: int) -> str:
    # Gets a verse from the Quran and returns it as a tuple (Arabic, English)
    url = f"https://api.mp3quran.net/api/aya?surah={surah}&language=en&aya={aya}"
    req = r.request("GET",url=url)
    try:
        ayaDict = ast.literal_eval(req.text) # From string to dictionary
        arEnDict = {"AR": ayaDict["ayah_text"], "EN": ayaDict["ayah_text_lang"]}
    except:
        raise Exception("INVALID AYAH/SURAH")

    return arEnDict


