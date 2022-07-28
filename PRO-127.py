
from bs4 import BeautifulSoup
import requests

try:
   response=requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
   soup=BeautifulSoup(response.text,'html.parser')
   #print(soup)
   stars=soup.find('tbody',class_="wikitable_sortable_jquey-tablesorter").find_all("td")

   for star in stars:
  #  print(movie)
    proper_name=star.find('th',class_="headerSort").get_text(strip=True).split(',')[0]
    distance=star.find('th',class_="headerSort").a.text
    mass=star.find('th',class_="headerSort").strong.text
    radius=star.find('th',class_="headerSort").span.text.replace('(',"")
    #year=year.replace(')',"")
    print(proper_name, distance, mass, radius)

except Exception as e:
    print(e)