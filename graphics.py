from traceback import print_tb
import flickrapi as f
import os
import requests as r
import random as rand

def downloadBKGND(flickr, searchTerm):
    try:
        extras='url_o'
        print(f"[BKGND] Searching: {searchTerm}")

        searchRes = flickr.photos.search(text=searchTerm, per_page = 30, extras=extras, safe_search=3, content_type=1, privacy_filter=1)
        print("[BKGND] Image found.")

        image = open("image.jpg", "wb")
        
        print("[BKGND] Downloading...")
        image.write(r.get(searchRes["photos"]["photo"][rand.randint(0,29)]["url_o"]).content)
        image.close()
    except:
        print("Failed. Restarting...")
        downloadBKGND(flickr,searchTerm)
    print("[BKGND] Download Complete")

FLICKR_KEY = os.environ['FLICKR_KEY']
FLICKR_SECRET = os.environ["FLICKR_SECRET"]

flicker = f.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format="parsed-json")

downloadBKGND(flicker, "space galaxy nebula")




