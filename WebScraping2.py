from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "C:\Java\Web Scrapping 2\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.billboard.com/charts/year-end/hot-100-songs/")

songlist = []
now = datetime.now()
i = 1
while i<=100:
    for song in driver.find_elements_by_class_name("o-chart-results-list-row-container"):
        print(song.text.split("\n"))
        for img in song.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".jpg")
            i = i+1
            songlist.append(
                {
                    "No": song.text.split("\n")[0],
                    "Song": song.text.split("\n")[1],
                    "Singer": song.text.split("\n")[2],
                    "ScrappingTime": now.strftime("%d %B %Y %H:%M:%S"),
                    "Image": img.get_attribute("src")
                }
            )
hasil_scraping = open("hasilscraping2.json", "w")
json.dump(songlist, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.quit()