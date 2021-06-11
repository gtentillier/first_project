# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:34:24 2021

@author: gtent
"""

import requests
from bs4 import BeautifulSoup
import urllib.request

#SCRAPING
url="https://www.amazon.fr/s?k=chaussure"

response = requests.get(url)

soup=BeautifulSoup(response.content, "html.parser")

#print(soup.prettify())

images = soup.find_all( "img" )

#, {"class" : "_1cnjm"}
    
number = 1

if (len(images)<5) :
    print("captcha detected")
else :
    for image in images:
        image_src=image["src"]
        urllib.request.urlretrieve(image_src, "test_1/"+str(number))
        print(number)
        number+=1

# image : <img alt="Geox U Wells C, Sneaker Homme" class="s-image" data-image-index="48" data-image-latency="s-product-image" data-image-load="" data-image-source-density="1" loading="lazy" src="https://m.media-amazon.com/images/I/81tdSn6yt5L._AC_UL320_.jpg" srcset="https://m.media-amazon.com/images/I/81tdSn6yt5L._AC_UL320_.jpg 1x, https://m.media-amazon.com/images/I/81tdSn6yt5L._AC_UL480_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81tdSn6yt5L._AC_UL640_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81tdSn6yt5L._AC_UL800_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81tdSn6yt5L._AC_UL960_QL65_.jpg 3x"/>

# image_src : https://m.media-amazon.com/images/I/81tdSn6yt5L._AC_UL320_.jpg
