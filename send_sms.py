from twilio.rest import Client
client = Client("ACddd31528236c816cd5f4ef3a852b70bd", "d124d7619a91855b5641e26fad1b38cc")

num_dict = {"Pato":"+16083452528",
            "Ya_Boi":"+16085905252",
            "Lexi":"+17162777008"}

to_num = num_dict["Ya_Boi"]
from_num = "+14159680456"

message = ""

annoyance_level = 1

for i in range(annoyance_level):
    client.messages.create(to=to_num, from_=from_num, body=message)