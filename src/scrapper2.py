import requests
from bs4 import BeautifulSoup as BS

def weekArtists():

  url = "https://www.last.fm/user/Henriquesans"
  page_response = requests.get(url)
  page = BS(page_response.text, 'lxml')
  table = page.find ('ol')
  rows = table.find_all('li')
  artistas = []
  for row in rows[0:]: 
      cols = row.find_all("a")
      
      artista = {}
      artista["nome"] = cols[0].get_text().strip()
      artista["plays"] = cols[1].get_text().strip()
      artistas.append(artista)

  return artistas

print(weekArtists())