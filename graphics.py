from traceback import print_tb
import flickrapi as f
import os
import requests as r
import random as rand
import quranUtils as q
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap

def downloadBKGND(flickr, searchTerm):
    try:
        extras='url_l'
        print(f"[BKGND] Searching: {searchTerm}")

        searchRes = flickr.photos.search(text=searchTerm, per_page = 30, extras=extras, safe_search=3, content_type=1, privacy_filter=1)
        print("[BKGND] Image found.")

        image = open("image.jpg", "wb")
        
        print("[BKGND] Downloading...")
        image.write(r.get(searchRes["photos"]["photo"][rand.randint(0,29)][extras]).content)
        image.close()
    except:
        print("Failed. Restarting...")
        downloadBKGND(flickr,searchTerm)
    print("[BKGND] Download Complete")

def prepareGraphic(img, ayaListAREN):
    pic = Image.open("image.jpg")
    WIDTH = pic.width
    HEIGHT = pic.height
    picEdit = ImageDraw.Draw(pic)
    enFont = ImageFont.truetype('bahnschrift.ttf', 25)
    text = ""
    for aya in ayaListAREN:
        text = text + aya["EN"] + "*"

    wrappedList = textwrap.wrap(text, 50)

    wrappedText = "\n".join([i for i in wrappedList[0:]])

    picEdit.text((50,50),text=wrappedText, font=enFont, fill=(255,255,255))
    print(f"START NORMAL {text} \n START WRAPPED {wrappedText}")
    pic.show()


FLICKR_KEY = os.environ['FLICKR_KEY']
FLICKR_SECRET = os.environ["FLICKR_SECRET"]

flickr = f.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format="parsed-json")

downloadBKGND(flickr, "Space Galaxy Nebula")

ayaListAREN = q.getWird()

prepareGraphic(None, ayaListAREN)


