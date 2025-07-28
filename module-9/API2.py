import requests

# Step 1: Connect to the Fireball API
url = "https://ssd-api.jpl.nasa.gov/fireball.api"
response = requests.get(url)

# Step 2: Print raw response text
print("Raw Response:\n")
print(response.text)

# Step 3: Print formatted response if successful
if response.status_code == 200:
    data = response.json()
    print("\nFormatted Response:\n")
    
    print(f"Total Fireball Records: {data['count']}\n")
    
    print("Sample Records:")
    for fireball in data['data'][:3]:  # Print only first 3 for sample
        print(f"Date: {fireball[0]}")
        print(f"Energy (kt): {fireball[1]}")
        print(f"Impact-E: {fireball[2]}")
        print(f"Lat: {fireball[3]} {fireball[4]}")
        print(f"Lon: {fireball[5]} {fireball[6]}")
        print(f"Altitude (km): {fireball[7]}")
        print("-" * 40)
else:
    print("Failed to connect to NASA Fireball API.")
    print("Status code:", response.status_code)

