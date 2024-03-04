import requests

url = "https://media.licdn.com/dms/image/D4D03AQHnO4ZA4_ET8w/profile-displayphoto-shrink_200_200/0/1708194147603?e=1715212800&v=beta&t=PMR0I9D3rUt6L6lep2pySZFHzvmC4kiLBHMzpjr5CkE"

r = requests.get(url)

with open("philip.jpg", mode = "wb") as bobby:
    bobby.write(r.content)

