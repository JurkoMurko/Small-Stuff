from bs4 import BeautifulSoup
import requests as r
import csv

path_to_html_file = 'G:\My Drive\juraj@andrews\Code\Small Shit\Scrapping Agent Numbers\html_flies\idk.html'

html = ''
with open(path_to_html_file, 'r') as f:
    html = f.read()

    
soup = BeautifulSoup(html, 'html.parser')

elements = soup.find_all("div")
for element in elements:
    print(element.content)