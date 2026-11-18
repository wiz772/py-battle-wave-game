import random
import utils
import models
import time
import copy
import sys

from constants import TEAM_SIZE, WAVE_SIZE, SECONDS_BETWEEN_ROUNDS


# =================================game logic===========================================


# Créer une équipe
        # initialiser available_chars = copy characters
        # initialiser equipe = []
        # tant que len equipe< TEAM_SIZE
            # choisir parmis les options 
            # valider choix, si valide:
                # append choix à equipe
                # remove choix à available_characters()
        # return equipe
def create_team(characters):
    available_chars = copy.deepcopy(characters)
    team = []
    while len(team) < TEAM_SIZE:
        choice = get_valid_choice(available_chars)
        team.append(available_chars[choice - 1])
        available_chars.pop(choice - 1)
    return team

def is_team_alive(team) -> bool:
    # pour chaque personnage dans team
        # si un personnage a des pv supérieur à 0
            # return True
        # sinon
            # False
    for character in team:
        if character["pv"] > 0:
            return True
    return False

def new_wave(monsters):
    # initaliser new_wave avec un sample de monsters de len WAVE_SIZE
    # return new wave
    available_monsters = copy.deepcopy(monsters)
    wave = random.sample(available_monsters, WAVE_SIZE)
    return wave

def start_fight(team, monsters):
    # initaliser le score et le nombre de vague à 0
    # tant que tout les characters dans l'équipe sont en vie:
        # créer une nouvelle vague -> renvoie une liste de monsters de len WAVE_SIZE
        # incrémenter nombre de vague
        # combat entre notre équipe et new wave -> renvoie un bool: True si notre équipe gagne, False si elle a perdu
            # si equipe gagne
                # recalculer score
            # sinon
                # sortir de la boucle while
    # return score, wave_number
    score = 0
    wave_number = 0

    while is_team_alive(team):
        current_wave = new_wave(monsters)
        wave_number += 1
        team_win = fight_wave(team, current_wave)
        if team_win:
            score = recalculate_score(wave_number, score)
            utils.print_wave_win()
        else:
            break
        time.sleep(SECONDS_BETWEEN_ROUNDS)
    return score, wave_number

def get_alive_entities(entities):
    return [ entity for entity in entities if entity["pv"] > 0 ]
    # return tout entity dans entities qui ont pv > 0

def is_alive(entity):
    return entity["pv"] > 0

def get_next_target(targets):
    ...

def attack(attacker, target):
    ...

def check_entity_death(entity):
    if not is_alive(entity):
        utils.print_target_killed(entity)

def get_new_health_of_target_after_attack(attacker_atk, target_pv, target_def):
    damage = max(1, attacker_atk // target_def)
    return target_pv - damage

def fight_round(attackers, targets):
    # get attackers alive
    # Pour chaque attacker dans alive attackers
        # get target alive
        # si aucun target alive return
        # get current target dans alive_targets aléaoitrmet
        # attack une parmis target alive
    alive_attackers = get_alive_entities(attackers)
    for attacker in alive_attackers:
        alive_targets  = get_alive_entities(targets)
        if len(alive_targets) == 0:
            return
        
        current_target = get_next_target(alive_targets)
        attack(attacker, current_target)

        check_entity_death(current_target)            

def fight_wave(team, wave) -> bool:
    # tant que vrai
        # wave = tour de l'équipe encore en vie contre les monstres encore en vie
        # si wave est morte:
            # return True

        # team = tour de la wave encore en vie contre les joueurs encore en vie
        # si team est mort:
            # return false
    while True:
        fight_round(team, wave)
        if not is_team_alive(wave):
            return True

        fight_round(wave, team)
        if not is_team_alive(team):
            return False
        

def recalculate_score(wave_number, score) -> int:
    # return score + wave * 2
    return score + wave_number * 2

# ================================persistence============================================

def save_score(score):
    ...

# ============================================================================

def play():
    # récupérer les collections monstres et characters de la DB
    # créer une équipe : create_team() -> renvoie une liste de characters
    # lancer le combat : start_fight(team) -> qui return score et wave_number
    # envoyer un message de fin avec score et nombre de vague
    # sauvegarder les scores
    characters, monsters = models.characters, models.monsters
    team = create_team(characters)
    score, wave_number = start_fight(team, monsters)
    utils.print_end(score, wave_number)
    save_score(score)

def show_leaderboard():
    ...
    
def quit():
    utils.print_exit_message()
    sys.exit()

# ============================================================================

def get_options_name(options):
    return [option.get("name", "inconnu") for option in options]

def print_options(options_name):
    # print_options(options):
    # pour chaque index, option dans enumerate(options_names) commençant à 1
        # afficher option numérotée de l'indice
    for index, option_name in enumerate(options_name, start=1):
        print(f"{index}: {option_name}")

def is_choice_valid(choice, minimum, maximum) -> bool:
    # is_choice_valid(choice, min, max):
    # vérifier si le choix contient seulement des entiers
        # convertir str to int
        # vérifier si le choix est compris entre min et max
            # return True
    # return False
    if choice.isdigit():
        choice = int(choice)
        if choice >= minimum and choice <= maximum:
            return True
    return False

def get_valid_choice(options):
    # Récupérer un choix valide parmi les options(options)
        # Récupérer une liste des noms d'options
        # while True
            # afficher options numérotées: print_options(options)
            # récupérer choix: input()
            # si choix valide: is_choice_valid(choix, 1, len(options)
                # return choix en int
            # sinon 
                # afficher erreur
    options_name = get_options_name(options)
    while True:
        print_options(options_name)
        choice = input("\nEntrez votre choix: ")
        if is_choice_valid(choice, 1, len(options)):
            return int(choice)
        else:
            utils.print_error("Choix invalide")

def handle_choice(choice, options):
    options[choice - 1]["func"]()

def main():
    # Main
    #  Tant que vrai
        # choice = Récupérer choix valide parmi les options(options)
        # Lancer le processus associé au choix : options[choice - 1]["function"]()
    
    # main_options 
    # list dict associations name, func
    main_options = [{"name": "Jouer", "func": play}, {"name": "Leaderboard", "func": show_leaderboard}, {"name": "Quitter", "func": quit}]
    while True:
        choice = get_valid_choice(main_options)
        handle_choice(choice, main_options)

if __name__ == "__main__": 
    main()