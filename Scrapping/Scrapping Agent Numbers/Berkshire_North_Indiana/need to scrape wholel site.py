from bs4 import BeautifulSoup
import requests as r
import csv
import re

url = 'https://www.bhhsnorthernindianarealestate.com/real-estate-agents'

# html = ''
# with open('properites_realtors.html', 'r') as f:
#     html = f.read()

 
soup = BeautifulSoup(r.get(url).content, 'html.parser')
# pattern = re.compile(r'\.val\("([^@]+@[^@]+\.[^@]+)"\);', re.MULTILINE | re.DOTALL)

script_tag = soup.find_all("script")
for tag in script_tag:
    if tag:
        # contains all of the script tag, e.g. "jQuery(window)..."
        script_tag_contents = tag.string
        try:
            # from there you can search the string using a regex, etc.
            email = re.search(r'"email":".+@atproperties.com"', script_tag_contents).group()
            print(email)
        except AttributeError as err:
            print(err)
        except TypeError as err:
            print(err)






# links = soup.findAll('a')

# array = []
# for link in links:
#     url = link.get("href")
#     if "https" in url:
#         array.append(url)

# array = set(array)
# print((array))

# agents = soup.find_all("div", class_="agent-card-container")
# print("Number of Agents" + str(len(agents)))

# with open('agent_data.csv', 'w', newline='\n') as file:
#     writer = csv.writer(file)
#     for agent in agents: 
#         try:
#             name = agent.find('span', class_="agent-name").a.get("title").strip("\n")
#         except AttributeError:
#             name = ""
#         email = agent.find('a', class_="agent-email").get("title")
#         try:
#             phone_number = agent.find('a', class_="non-link").text
#         except AttributeError:
#             phone_number = 0

        
#         writer.writerow([name, email, phone_number])
