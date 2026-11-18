def print_error(message):
    print(f"Erreur: {message}")

def print_end(score, wave_number):
    print(f"\n Vous êtes morts! Vous avez fait : {score} de score en {wave_number} vagues.")

def print_wave_win():
    print(f"Vous avez gagné une manche!")

def print_target_killed(target):
    print(f"L'unité: {target["name"]} est tombé au combat!")

def print_exit_message():
    print(f"""

        BYE BYE BYE BYE DOIGBYE BYE

    """)