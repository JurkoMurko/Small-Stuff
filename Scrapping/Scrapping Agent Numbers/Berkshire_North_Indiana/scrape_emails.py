from bs4 import BeautifulSoup
import requests as r
import re
import csv

with open('sites.txt', 'r') as f:
    sites = list(filter(None, f.read().splitlines()))

pattern = re.compile(r'[a-zA-Z.-_]+@[a-zA-Z.-_]+\.[a-z]{3}', re.MULTILINE | re.DOTALL)
pattern2 = re.compile(r'forbiden', re.I)

with open('emails2.csv', 'a', newline='\n') as file:
    csv_writer = csv.writer(file)

    for site in sites:
        print('\n',site)
        try:
            soup = BeautifulSoup(r.get(site).content, 'html.parser') 
        except:
            print('ERROR')

        text = soup.text
        if len(text) < 500 and pattern2.match(text):
            print('FORBIDDEN')
            csv_writer.writerow([site, "FORBIDEN"])

        matches = pattern.finditer(text)

        for match in matches:
            print('\t',match.group(0))
            csv_writer.writerow([site, match.group(0)])
