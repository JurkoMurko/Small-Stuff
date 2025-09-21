from bs4 import BeautifulSoup
import requests as r
import csv
import re

urls = {'https://www.atproperties.com/teams/331/chris-marzke-team', 'https://www.atproperties.com/teams/221/wortman-real-estate-group', 'https://www.atproperties.com/agents/8190/shelle-dragomer', 'https://www.atproperties.com/agents/10685/austin-grall', 'https://www.atproperties.com/agents/11593/drew-hedstrom', 'https://www.atproperties.com/agents/1656/santiago-moreno', 'https://www.atproperties.com/agents/20865/jamie-kastelic', 'https://www.atproperties.com/agents/10260/thomas-summers', 'https://www.atproperties.com/agents/3755/jackson-matson', 'https://www.atproperties.com/agents/22885/anthony-clark', 'https://www.atproperties.com/agents/6358/jaimie-lenardson', 'https://www.atproperties.com/agents/10261/michelle-priefer', 'https://www.atproperties.com/agents/7063/michael-mccausland', 'https://www.atproperties.com/agents/3912/anne-gain', 'https://www.atproperties.com/agents/4501/april-moon', 'https://www.atproperties.com/agents/4123/stacey-melgard', 'https://www.atproperties.com/agents/6954/gary-depa', 'https://www.atproperties.com/agents/8202/gretta-volkenstein', 'https://www.atproperties.com/agents/4894/victoria-krause-schutte', 'https://www.atproperties.com/agents/4067/bob-walck', 'https://www.atproperties.com/teams/489/anne-gain-group', 'https://www.atproperties.com/agents/8194/amber-dragomer', 'https://www.atproperties.com/teams/1038/anderson-moon-group', 'https://www.atproperties.com/agents/20115/cori-hatheway', 'https://www.atproperties.com/agents/7279/lauren-potts', 'https://www.atproperties.com/agents/7503/dana-riley', 'https://www.atproperties.com/agents/6099/david-hammerschmidt', 'https://www.atproperties.com/agents/7896/joseph-flood', 'https://www.atproperties.com/agents/22072/kimberly-fenech', 'https://www.atproperties.com/agents/12996/kira-kelley', 'https://www.atproperties.com/agents/8596/forest-burczak', 'https://www.atproperties.com/agents/8404/donna-shafer', 'https://www.atproperties.com/agents/6742/michele-kaiser', 'https://www.atproperties.com/teams/1292/jardine-group', 'https://www.atproperties.com/agents/6393/don-kamp', 'https://www.atproperties.com/agents/19180/joely-gibson', 'https://www.atproperties.com/agents/5083/kathy-l-virgil', 'https://www.atproperties.com/agents/23256/gary-hardina', 'https://www.atproperties.com/agents/14104/chuck-anderson', 'https://www.atproperties.com/teams/592/shelle-dragomer-team', 'https://www.atproperties.com/agents/5293/cynthia-adent', 'https://www.atproperties.com/agents/11084/arielle-ringer', 'https://www.atproperties.com/agents/7161/dayna-kozminski', 'https://www.atproperties.com/agents/19408/joan-armon', 'https://www.atproperties.com/agents/21075/anne-odden', 'https://www.atproperties.com/agents/3370/chris-marzke', 'https://www.atproperties.com/agents/7065/bill-achterberg', 'https://www.atproperties.com/agents/12881/connie-peet', 'https://www.atproperties.com/agents/22911/juli-milnikel', 'https://www.atproperties.com/agents/16510/maggie-ahern', 'https://www.atproperties.com/agents/3774/mark-wortman', 'https://www.atproperties.com/agents/8203/joel-kruggel', 'https://www.atproperties.com/teams/593/gretta-volkenstein-team', 'https://www.atproperties.com/agents/18321/jill-drebing', 'https://www.atproperties.com/agents/5669/david-kaminski', 'https://www.atproperties.com/agents/18861/amy-neal', 'https://www.atproperties.com/agents/18860/david-jardine', 'https://www.atproperties.com/agents/7064/patricia-bowman', 'https://www.atproperties.com/agents/3005/john-park', 'https://www.atproperties.com/agents/6373/doug-wortman', 'https://www.atproperties.com/agents/6902/erica-mantei', 'https://www.atproperties.com/agents/5110/mary-lynn-kormanik'}

print(len(urls))
html = ''
with open('properites_realtors.html', 'r') as f:
    html = f.read()

for site in urls:
    # print(site)
    soup = BeautifulSoup(r.get(site).content, 'html.parser')
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
            except AttributeError:
                pass
            except TypeError:
                pass






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
