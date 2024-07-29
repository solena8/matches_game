# On décrit le jeu des allumettes : au départ, il y a un tas de 50 allumettes, (ou tout autre objet :
# cailloux, jetons, . . .). Chacun à son tour, les deux joueurs ôtent obligatoirement entre 1 et 6 allumettes.
# Celui qui ôte la dernière allumette gagne.
# Une fonctionnalité = une fonction.

# Étape 1
# Faire une fonction qui prend en paramètre le nombre d'allumettes à enlever du reste.
# Étape 2
# Demander a l'utilisateur combien d'allumettes il souhaite retirer tant qu’il y a des allumettes dans le tas.
# Étape 3
# Limiter le nombre d’allumettes à pouvoir être retirées de 1 à 6.
# Ajouter a votre jeu la notion de victoire.
# Étape 4
# Rajouter un 2eme joueur à votre jeu.
# Étape 5
# Proposer un mode multi-joueur. Demander à l’utilisateur, combien il y a de joueur et gérer la partie en conséquence.
# Étape 6
# Libre à vous de faire une interface graphique à votre goût !


matches_stack = 50


def remove_matches_3(matches) -> int:
    while True:
        try:
            removed_match_nb = int(input("How many matches do you want to take out (must be between 1 and 6)? "))
            if 1 <= removed_match_nb <= 6:
                if removed_match_nb <= matches:
                    return matches - removed_match_nb
                else:
                    print(f"Not enough matches left, remove {matches} matches or less")
            else:
                print("Invalid number. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


def game_won(matches: int) -> bool:
    return matches == 0


def number_of_players() -> list:
    while True:
        try:
            num_of_players = int(input("How many players will enter the game? "))
            if num_of_players > 1:
                players = [input(f"Player {i+1}, what is your name? ") for i in range(num_of_players)]
                print(players)
                return players
            else:
                print("Number of players must be at least 2.")
        except ValueError:
            print("Invalid input. Please enter an integer greater than 0.")


def game(matches: int):
    game_matches = matches
    players = number_of_players()
    while True:
        for player in players:
            print(f"{game_matches} matches left, your turn {player}!")
            game_matches = remove_matches_3(game_matches)
            if game_won(game_matches):
                print(f"You won, {player}!!!")
                return


game(matches_stack)
