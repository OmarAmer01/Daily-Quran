import quranAPIwrapper as q
import random as rand
#from bs4 import BeautifulSoup
import requests as r
#import pandas as pd
import linecache

# def getNumAyaCSV() -> int:
#     # Scrapes the number of ayats in all surahs from wikipedia

#     url = "https://en.wikipedia.org/wiki/List_of_chapters_in_the_Quran"
#     webpage = r.request("GET", url=url)
#     soup = BeautifulSoup(webpage.content, "html.parser")
#     table = soup.find('table', 'wikitable sortable')
#     df = pd.read_html(str(table))
#     df = pd.concat(df)
#     df = df["Number of verses (Number of Rukūʿs)"]

#     for idx in range(0,114):
#         df[idx] = df.str.split(" ")[idx][0]

#     df.to_csv("ayat.col",header=False, index=False)

    
def getWird(wirdLen = 100):
    # Returns wirdLen chars of quran (counts arabic chars)
    # while separating ayas in an array (one for arabic and another for english)

    surah = rand.randint(1,114)
    endAya = int(linecache.getline("ayat.col", surah))
    
    startIDX = rand.randint(1,endAya-2)

    currentWirdLen = 0

    ayaListAREN = []
    iter = 0

    while currentWirdLen < wirdLen:
        try:
            currentAya = q.getVerseARen(surah,startIDX+iter)
            ayaListAREN.append(currentAya)
            iter = iter + 1
            currentWirdLen = len(currentAya["AR"]) + currentWirdLen

        except:
            startIDX = rand.randint(1,endAya-2)
            currentWirdLen = 0
            ayaListAREN = []
            iter = 0
            continue

    return ayaListAREN    


