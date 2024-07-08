import requests

def get_pokemon_info(pokemon):
    

    pokemon = str(pokemon).strip().lower()
    print(f"Getting information on {pokemon}...")

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully fetched Pokémon Info")
        return response.json()
    else:
        print(f"Failed to fetch Pokémon. Status code: {response.status_code}")
        return None
