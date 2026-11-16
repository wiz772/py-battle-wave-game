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




def play():
    print("play")

def show_leaderboard():
    print("leaderboard")

def quit():
    ...

options = [{"name": "Jouer", "func": play}, {"name": "Leaderboard", "func": show_leaderboard}, {"name": "Quitter", "func": quit}]

def get_options_name(options):
    return [option.get("name", "inconnu") for option in options]

def print_options(options):
    options_name = get_options_name(options)
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
    while True:
        print_options(options)
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
