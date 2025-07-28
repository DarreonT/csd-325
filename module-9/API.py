import requests

# Get data from the API
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

# Check status
if response.status_code == 200:
    data = response.json()
    
    print(f"\nTotal number of people in space: {data['number']}\n")
    print("Here are the astronauts currently in space:\n")

    # Loop through and print each astronaut's name and craft
    for person in data['people']:
        print(f"Name: {person['name']}, Craft: {person['craft']}")
else:
    print("Failed to retrieve data from the API.")
    print("Status Code:", response.status_code)
