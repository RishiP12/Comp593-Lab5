import sys
from poke_api import get_pokemon_info
from pastebin_api import post_new_paste

def get_pokemon_name():
   
    if len(sys.argv) < 2:
        print("Error: No Pokémon name given.")
        sys.exit(1)
    return sys.argv[1]

def construct_paste_content(pokemon_info):
  
    name = pokemon_info['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    title = f"{name}’s Abilities"
    body_text = '\n'.join(f"- {ability}" for ability in abilities)
    return title, body_text

def main():
    pokemon_name = get_pokemon_name()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        title, body_text = construct_paste_content(pokemon_info)
        paste_url = post_new_paste(title, body_text, expiration='1M', listed=False)
        if paste_url:
            print(paste_url)
        else:
            print("Failed to  paste.")
    else:
        print(f"Failed to fetch Info on {pokemon_name}.")

if __name__ == "__main__":
    main()
