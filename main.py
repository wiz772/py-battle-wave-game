import random

# options 
    # list dict associations name, function

# Récupérer un choix valide parmi les options(options)
    # while True
        # afficher options numérotées: print_options(options)
        # récupérer choix: input()
        # si choix valide: is_choice_valid(choix, 1, len(options)
            # return choix en int

# print_options(options):
    # récupérer liste des "name"
    # pour chaque index, option dans enumerate(options_names) commençant à 1
        # afficher option numérotée de l'indice

# is_choice_valid(choice, min, max):
    # vérifier si le choix contient seulement des entiers
        # convertir str to int
        # vérifier si le choix est compris entre min et max
            # return True
    # return False

# Main
    # choice = Récupérer choix valide parmi les options(options)
    # Lancer le processus associé au choix : options[choice - 1]["function"]()

TEAM_SIZE = 3


# Créer une équipe
        # characters = get la collection charachters
        # available_chars = copy characters
        # equipe = []
        # tant que len equipe< TEAM_SIZE
            # afficher available chars
            # choisir parmis les options 
            # valider choix, si valide:
                # append choix à equipe
                # remove choix à available_characters()
        # return equipe
def create_team(characters):
    available_chars = characters.copy()
    team = []
    while len(team) < TEAM_SIZE:
        choice = get_valid_choice(available_chars)
        team.append(choice - 1)
        available_chars.pop(choice - 1)
    return team

def is_team_alive(team):
   return any(character["pv"] > 0 for character in team)

def new_wave(monsters):
    available_monsters = monsters.copy() 
    new_wave = random.sample(available_monsters, 3)
    return new_wave
    #Nouvelle liste wave:
    # pick 3 monsters
    # append à new wave
    # return new wave

def fight(team, wave):
    ...
    # while is_team_alive(wave):
    #     if not is_team_alive(team):
    #         return False
    #     for monster in wave:
    #         for character in team:
    #             print(f"{character}")
    # tant que les monstres ne sont pas tous mort
        # si les perso sont pas alive:
            # return false
        # pour chaque monstre
            # chaque character attack monstre
    # return trues

def recalculate_score(wave):
    ...

def save_score(score):
    ...

def play():
    characters = [
    {"_id": 1, "name": "Gobelin", "atk": 10, "def": 5, "pv": 50},
    {"_id": 2, "name": "Orc", "atk": 20, "def": 8, "pv": 120},
    {"_id": 3, "name": "Dragon", "atk": 35, "def": 20, "pv": 300},
    {"_id": 4, "name": "Zombie", "atk": 12, "def": 6, "pv": 70},
    {"_id": 5, "name": "Troll", "atk": 25, "def": 15, "pv": 200},
    {"_id": 6, "name": "Spectre", "atk": 18, "def": 10, "pv": 100},
    {"_id": 7, "name": "Golem", "atk": 30, "def": 25, "pv": 250},
    {"_id": 8, "name": "Vampire", "atk": 22, "def": 12, "pv": 150},
    {"_id": 9, "name": "Loup-garou", "atk": 28, "def": 18, "pv": 180},
    {"_id": 10, "name": "Squelette", "atk": 15, "def": 7, "pv": 90}
]
    monsters = [
    {"_id": 1, "name": "Gobelin", "atk": 10, "def": 5, "pv": 50},
    {"_id": 2, "name": "Orc", "atk": 20, "def": 8, "pv": 120},
    {"_id": 3, "name": "Dragon", "atk": 35, "def": 20, "pv": 300},
    {"_id": 4, "name": "Zombie", "atk": 12, "def": 6, "pv": 70},
    {"_id": 5, "name": "Troll", "atk": 25, "def": 15, "pv": 200},
    {"_id": 6, "name": "Spectre", "atk": 18, "def": 10, "pv": 100},
    {"_id": 7, "name": "Golem", "atk": 30, "def": 25, "pv": 250},
    {"_id": 8, "name": "Vampire", "atk": 22, "def": 12, "pv": 150},
    {"_id": 9, "name": "Loup-garou", "atk": 28, "def": 18, "pv": 180},
    {"_id": 10, "name": "Squelette", "atk": 15, "def": 7, "pv": 90}
]

    team = create_team(characters)
    score = 0
    while is_team_alive(team):
        wave = new_wave(monsters)
        team_win = fight(team, wave)
        if team_win:
            score = recalculate_score(wave)

    save_score(score)
    # tant que tout les persos sont en vie:
        # nouvelle vague
        # combat équipe et current vague
        # recalculer score
    # save_score
    ...

def show_leaderboard():
    print("leaderboard")

def quit():
    ...

options = [{"name": "Jouer", "func": play}, {"name": "Leaderboard", "func": show_leaderboard}, {"name": "Quitter", "func": quit}]

def get_options_name(options):
    return [option.get("name", "inconnu") for option in options]

def print_options(options_name):
    for index, option_name in enumerate(options_name, start=1):
        print(f"{index}. {option_name}")

def is_choice_valid(choice, min, max):
    if choice.isdigit():
        choice = int(choice)
        if choice >= min and choice <= max:
            return True
    return False

def print_error(message):
    print(f"Erreur: {message}")

def get_valid_choice(options):
    options_name = get_options_name(options)
    while True:
        print_options(options_name)
        choice = input("\nEntrez votre choix: ")
        if is_choice_valid(choice, 1, len(options)):
            return int(choice)
        else:
            print_error("Choix invalide")

def handle_choice(choice, options):
    options[choice - 1]["func"]()

def main():
    choice = get_valid_choice(options)
    handle_choice(choice, options)

if __name__ == "__main__": 
    main()
