# Import package requests dan Beutifulsoup
from queue import PriorityQueue
from textwrap import indent
from traceback import print_tb
import requests
from bs4 import BeautifulSoup
# Request ke Website
page = requests.get("https://republika.co.id/")

# Extract konten menjadi objek Beautiful Soup
obj = BeautifulSoup(page.text,'html.parser')
print('Menampilkan objek html')
print('======================')
print(obj)
print('Menampilkan title browser dengan tag')
print('====================================')
print(obj.title)
print('\nMenampilkan title browser tanpa tag')
print('====================================')
print(obj.title.text)

print('Menampilkan semua tag h2')
print('========================')
print(obj.find_all('h2'))

print('\nMenampilkan semua teks h2')
print('===========================')
for headline in obj.find_all('h2'):
    print(headline.text)

print('\nMenampilkan headline berdasarkan div class')
print('============================================')
print(obj.find_all('div',class_='bungkus_txt_headline_center'))

print('\nMenampilkan semua teks headline')
print('=================================')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    print(headline.find('h2').text)

print('\nMenyimpan headline pada file text')
print('===================================')
f=open('headline.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    f.write(headline.find('h2').text)
    f.write('\n')
f.close()

print("\n Menampilkan Kategori berdasarkan div class")
print("=================================")
for category in obj.find_all('div',class_='teaser_conten1_center'):
    print(category.find('p').text)

# Import Package json
import json
from datetime import datetime
# Deklarasi list kosong
data=[]
now = datetime.now()
# Lokasi file json
f=open('headline.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"Judul":publish.find('h2').text,
                 "Kategori":publish.find('a').text,
                 "WaktuPublish":publish.find('div',class_='date').text,
                 "WaktuScraping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps = json.dumps(data, indent=1)
f.writelines(jdumps)
f.close()

