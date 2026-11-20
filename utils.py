def print_error(message):
    print(f"Erreur: {message}")

def print_end(score, wave_number):
    print(f"\n Vous êtes morts! Vous avez fait : {score} de score en {wave_number} vagues.")

def print_wave_win():
    print(f"Vous avez gagné une manche!")

def print_entity_death(target):
    print(f"L'unité: {target["name"]} est tombé au combat!")

def print_exit_message():
    print(f"""

        BYE BYE BYE BYE DOIGBYE BYE

    """)

def print_scores(top_scores):
    print("\nVoici les scores:")
    for index, score in enumerate(top_scores):
        print(f"{index + 1} - {score}")
    print("\n")