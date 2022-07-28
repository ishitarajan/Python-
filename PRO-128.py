
#enter to venv to check the ouput and put the downloaded chromedriver  in vs
from bs4 import BeautifulSoup
import requests,openpyxl
import re

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="DWARF STARS"
sheet.append(['Name','Distance','Mass','Radius'])


try:
  response=requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
  soup=BeautifulSoup(response.text,'html.parser')
  stars=soup.find("table",class_="wikitable_sortable_jquery-tablesorter").find_all("table",class_="wikitable_sortable_jquery-tablesorter")
 
  for star in stars:
  #  print(movie)
    name=star.find('th').a.text
    distance=star.find('th',class_='headerSort').strong.text
    mass = star.find('th', class_ = 'headerSort').span.text
    radius = star.find('th', class_='headerSort').span.text
    sheet.append([name,distance,mass,radius])
 #   break

except Exception as e:
    print(e)

excel.save("DWARF_STARS.xlsx")