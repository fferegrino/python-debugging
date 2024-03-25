import requests

pokemon_url = "https://pokeapi.co/api/v2/pokemon/ditto"
breakpoint()
response = requests.get(pokemon_url)

ditto_data = response.json()
print(f"The base experience of Ditto is {ditto_data['base_experience']}")
print(f"The height of Ditto is {ditto_data['height']}")
print(f"The weight of Ditto is {ditto_data['weight']}")

